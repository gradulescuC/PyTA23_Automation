import requests

def get_user_saved_albums(limit=20, offset=0, market=""):
		header = {'Authorization': token}
		response = requests.get(f"https://api.spotify.com/v1/me/albums?limit={limit}&offset={offset}&market={market}",headers=header)
		return response