import requests

def save_albums_for_current_user(ids, token):
		header = {'Authorization': token}
		req_body = {
				"ids": [
						ids
				]
		}
		response = requests.put("https://api.spotify.com/v1/me/albums",json=req_body, headers=header)
		return response


