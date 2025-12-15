import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from b_generate_token import Generate_token
from requests_folder.artists.get_artist import *

'''
positive testing: get artist by valid id
negative testing: get artist by invalid id
'''

class TestArtist():

		def setup_class(self): # se execută o singură dată înaintea testelor din clasă
			self.token_object = Generate_token() # aici am instantiat un obiect din clasa Generate_token.  # un obiect este o adresa de memorie care va stoca valori individuale pentru atributele dintr-o clasa

		def teardown_class(self): # închide Chrome la final
			self.token_object.close()

		def test_get_artist_by_valid_id(self):
				token = self.token_object.authorization()
				response = get_artist("1r4hJ1h58CWwUQe3MxPuau", token)
				assert response.status_code==200,"error: status code is not correct"
				assert response.json()["name"]=="Maluma"




