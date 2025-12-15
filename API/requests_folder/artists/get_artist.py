import requests

'''
get artist by id
'''

def get_artist(id,token):
		header = {'Authorization': token}
		response = requests.get(f'https://api.spotify.com/v1/artists/{id}',header=header)
		return response
