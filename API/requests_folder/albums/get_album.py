import requests

'''
requests covered:
 - get album without market
 - get album with market
'''

# def get_album_without_market(id, token):
#     header = {'Authorization': token}
#     response = requests.get(f'https://api.spotify.com/v1/albums/{id}', headers=header)
#     return response
#
# def get_album_with_market(id,token,market=""):
#     header = {'Authorization': token}
#     response = requests.get(f'https://api.spotify.com/v1/albums/{id}?market={market}', headers=header)
#     return response

def get_album(id,token,market=""):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}?market={market}', headers=header)
    return response








