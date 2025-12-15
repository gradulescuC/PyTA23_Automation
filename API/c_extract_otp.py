# gmail_helper.py
import os
import base64
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import time

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service(credentials_path='credentials.json', token_path='token.json'):
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0, prompt='consent')
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_latest_email_matching(service, query):
    results = service.users().messages().list(userId='me', q=query, maxResults=1).execute()
    messages = results.get('messages', [])
    if not messages:
        return None
    msg_id = messages[0]['id']
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    return msg

def extract_otp_from_message(msg):
    parts = msg.get('payload', {}).get('parts', None)
    body_text = ''
    if parts:
        for p in parts:
            mime = p.get('mimeType', '')
            if mime == 'text/plain' and 'data' in p.get('body', {}):
                data = p['body']['data']
                body_text = base64.urlsafe_b64decode(data).decode('utf-8')
                break
    else:
        body = msg.get('payload', {}).get('body', {}).get('data')
        if body:
            body_text = base64.urlsafe_b64decode(body).decode('utf-8')
    if not body_text:
        body_text = msg.get('snippet', '')
    m = re.search(r'\b(\d{4,8})\b', body_text)
    return m.group(1) if m else None


def get_latest_otp_with_wait(service, query='subject:"Your Spotify login code"', last_msg_id=None, timeout=60, interval=10):
    """
    Așteaptă un email nou cu OTP (max 60 secunde) și îl extrage.
    Returnează (otp, last_msg_id_nou)
    """
    print("🔄 Pornesc monitorizarea inboxului Gmail pentru un nou OTP...")

    # Pas 1: obține cel mai recent email EXISTENT (pentru a ști de unde pornim)
    if not last_msg_id:
        initial_results = service.users().messages().list(userId='me', q=query, maxResults=1).execute()
        initial_messages = initial_results.get('messages', [])
        if initial_messages:
            last_msg_id = initial_messages[0]['id']
            print(f"📬 Ultimul email existent are ID-ul: {last_msg_id}")
        else:
            print("📭 Niciun email anterior găsit pentru acest query.")
            last_msg_id = None

    # Pas 2: buclă de așteptare până apare un email NOU
    print(f"⏳ Aștept maxim {timeout} secunde pentru un email nou...")
    start_time = time.time()
    new_msg = None

    while (time.time() - start_time) < timeout:
        results = service.users().messages().list(userId='me', q=query, maxResults=1).execute()
        messages = results.get('messages', [])

        if messages:
            message_id = messages[0]['id']

            # 👉 Dacă ID-ul diferă, e un email NOU
            if message_id != last_msg_id:
                print(f"📩 Email NOU detectat! ID: {message_id}")
                new_msg = service.users().messages().get(userId='me', id=message_id).execute()
                last_msg_id = message_id
                break

        # Dacă nu e nimic nou, așteaptă câteva secunde și mai verifică
        print(f"⏱️ Niciun email nou încă... mai verific peste {interval} secunde.")
        time.sleep(interval)

    # Pas 3: dacă n-a venit nimic nou
    if not new_msg:
        raise TimeoutError(f"❌ Nu a venit niciun email nou în {timeout} secunde.")

    # Pas 4: extrage corpul emailului
    body_text = ""
    payload = new_msg.get('payload', {})

    if 'parts' in payload:
        for part in payload['parts']:
            if part.get('mimeType') == 'text/plain' and 'data' in part.get('body', {}):
                body_text = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                break
    else:
        body = payload.get('body', {}).get('data')
        if body:
            body_text = base64.urlsafe_b64decode(body).decode('utf-8')

    if not body_text:
        body_text = new_msg.get('snippet', '')

    print(f"📨 Conținutul noului email:\n{body_text}")

    # Pas 5: extrage OTP-ul (6 cifre consecutive)
    match = re.search(r'\b(\d{6})\b', body_text)
    if not match:
        raise ValueError("⚠️ Nu s-a putut extrage OTP din email!")

    otp = match.group(1)
    print(f"✅ OTP găsit: {otp}")

    return otp, last_msg_id
