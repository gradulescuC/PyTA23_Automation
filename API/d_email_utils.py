import time

def wait_for_new_email(service, query, last_message_id=None, timeout=60, interval=5):
    """
    Așteaptă până apare un email nou care corespunde query-ului dat.
    """
    print("Aștept un email nou...")
    start_time = time.time()
    new_message = None

    while (time.time() - start_time) < timeout:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=1
        ).execute()

        messages = results.get('messages', [])
        if messages:
            message_id = messages[0]['id']

            # dacă e diferit de ultimul mesaj procesat — e unul nou!
            if message_id != last_message_id:
                new_message = service.users().messages().get(
                    userId='me',
                    id=message_id
                ).execute()
                print("Email nou găsit!")
                return new_message

        print("Niciun email nou, mai aștept...")
        time.sleep(interval)

    print("Timeout — nu a venit niciun email nou.")
    return None