import requests

def remove_user_saved_albums(ids, token):
		header = {'Authorization': token}
		request_body = {
				"ids":[ids]
		}
		response = requests.delete("https://api.spotify.com/v1/me/albums",json= request_body,headers=header)
		return response