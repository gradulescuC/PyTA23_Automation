# environment.py
from b_generate_token import Generate_token

def get_token():
    token_object = Generate_token()
    token = token_object.authorization()
    token_object.close()
    return token

