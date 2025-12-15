import requests

def get_album_tracks(id,token,market="", limit=20, offset=0):
		header = {'Authorization': token}
		response = requests.get(f"https://api.spotify.com/v1/albums/{id}/tracks?market={market}&limit={limit}&offset={offset}",headers=header)
		return response