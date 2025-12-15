import sys, os

from b_generate_token import Generate_token
from requests_folder.albums.get_several_albums import get_several_albums

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from requests_folder.get_several_albums import *

"""
TESTS TO BE COVERED:
1. Get single album
2. Get several albums - all albums exist
3. Get several albums - one album does not exist
4. Get several albums - no album in the list exists
5. Get several albums - album list is empty
6. Get several albums - one album id is invalid
7. Get several albums - all album ids are invalid
8. Get several albums per market - market exists
9. Get several albums per market - market does not exist
10. Get several albums per market - market is invalid
11. Get several albums - exactly 20 album ids
12. Get several albums - 21 album ids supplied
13. Get several albums - 19 albums supplied 
14. Get several albums - no id supplied

Test 11-13 => 3 point BVA -> Se folosesc pentru testare:
			- valoarea de limita (20)
			- valoarea din aceeasi clasa de echivalenta imediat langa limita (19)
			- valoarea din clasa de echivalenta adiacenta (21)
			Clasa de echivalenta 1-20
			
"""


class TestAlbums():

	def setup_class(self): # se execută o singură dată înaintea testelor din clasă
		self.token_object = Generate_token() # aici am instantiat un obiect din clasa Generate_token # un obiect este o adresa de memorie care va stoca valori individuale pentru atributele dintr-o clasa

	def teardown_class(self):
		# închide Chrome la final
		self.token_object.close()

	def test_get_single_album(self):
			token = self.token_object.authorization()
			response = get_several_albums("68rGH2GpyJVZb1BXaOfrcI", token)
			assert len(response.json()["albums"])==1

	def test_get_several_albums_all_albums_exist(self):
			token = self.token_object.authorization()
			response = get_several_albums("68rGH2GpyJVZb1BXaOfrcI,50ucNngVCHhY7Ma8iTpfVl", token)
			assert len(response.json()["albums"])==2