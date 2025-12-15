import requests

def get_several_albums(id_list,token,market=""):
		header = {'Authorization': token}
		response = requests.get(f'https://api.spotify.com/v1/albums?ids={id_list}&market={market}',headers=header)
		return response


