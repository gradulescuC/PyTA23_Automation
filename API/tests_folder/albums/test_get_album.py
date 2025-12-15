import sys, os

from b_generate_token import Generate_token
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from requests_folder import get_album
from requests_folder.albums.get_album import *

'''
positive testing: get album without market: album exists, album type is correct, artist name is correct, status is correct
negative testing: get album without market: album does not exist
negative testing: get album without market: album id is invalid

'''
class TestAlbums():

    def setup_class(self):
        # se execută o singură dată înaintea testelor din clasă
        self.token_object = Generate_token()
             # aici am instantiat un obiect din clasa Generate_token
                 # un obiect este o adresa de memorie care va stoca valori individuale pentru atributele dintr-o clasa

    def teardown_class(self):
        # închide Chrome la final
        self.token_object.close()

    # @functionaltesting @positivetesting
    def test_get_album_exists(self):
        token = self.token_object.authorization()
        response = get_album('68rGH2GpyJVZb1BXaOfrcI',token=token)
        assert response.status_code == 200
        assert response.json()["name"]=="Bipolară"
        assert response.json()["total_tracks"]==1

    # @functionaltesting @negativetesting
    def test_get_album_does_not_exist(self):
        token = self.token_object.authorization()
        response=get_album('1mc8M9eR9ZIBxqWA2CA4WN',token)
        assert response.status_code == 404

    # @functionaltesting @negativetesting
    def test_get_album_invalid(self):
        token = self.token_object.authorization()
        response=get_album('*mc8M9eR9ZIBxqWA2CA4WN&',token)
        assert response.status_code == 400

    # @functional testing # positive testing
    def test_get_album_filter_by_market_song_available_in_market(self):
        token = self.token_object.authorization()
        response = get_album('1mc8M9eR9ZIBxqWA2CA4Wo',token, "BR")
        assert response.status_code == 200

#     test_get_album_filter_by_market_song_not_available_in_market
#     => BUG: ar trebui sa nu returneze nimic (status 404)
#     =>  ar trebui confirmat cu dezvoltatorul ce ar trebui sa se intample in cazul asta
#     => Actual results: albumul este returnat in mod normal, chiar daca nu exista pe piata respectiva
#     """
#     def test_get_album_filter_by_market_song_not_available_in_market(self):
#         response = get_album_with_market('1mc8M9eR9ZIBxqWA2CA4Wo', "SO")
#         assert response.status_code == 404
#     """

    # @functional testing # negative testing
    def test_get_album_filter_by_market_invalid_market(self):
        token = self.token_object.authorization()
        response = get_album('1mc8M9eR9ZIBxqWA2CA4Wo',token,"XY")
        assert response.status_code == 400
        assert response.json()['error']['message']=='Invalid market code'

# """
# alte teste recomandate:
# - check release date
# - check total_tracks
# - check number of items
# """