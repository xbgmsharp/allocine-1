# -*- coding:Utf-8 -*-
import unittest

from allocine import AllocineApi


class TestApi(unittest.TestCase):
    """ Test the Allocine API wrapper. """

    def setUp(self):
        self.api = AllocineApi()

    def test_search(self):
        """ Test the search methods. """
        #Tests the ``search_movie`` method
        response = self.api.search_movie("Django unchained")
        self.assertEqual(response["feed"]["movie"][0]["code"], 190918)
        #Tests the ``search_theater`` method
        response = self.api.search_theater("pathé chavant")
        self.assertEqual(response["feed"]["theater"][0]["city"], "Grenoble")
        #Tests the ``search_person`` method
        response = self.api.search_person("Quentin Tarantino")
        self.assertEqual(response["feed"]["person"][0]["birthDate"], "1963-03-27")
        #Tests the ``search_news`` method
        response = self.api.search_news("pulp fiction")
        self.assertEqual(response["feed"]["news"][0]["code"], 18614628)
        #Tests the ``search_tvserie`` method
        response = self.api.search_tvserie("game of thrones")
        self.assertEqual(response["feed"]["tvseries"][0]["code"], 7157)
        #Tests the ``search`` method
        response = self.api.search("Inglorious bastards")
        self.assertEqual(response["feed"]["movie"][0]["code"], 60208)

    def test_get_infos(self):
        """ Test the get infos methods. """
        #Tests the ``get_movie_infos`` method
        response_movie = self.api.get_movie_infos(190918)
        self.assertEqual(response_movie["movie"]["castMember"][2]["person"]["name"], "Christoph Waltz")
        #Tests the ``get_theater_infos`` method
        response = self.api.get_theater_infos("P1032")
        self.assertEqual(response["theater"]["address"], u"21 bd Marechal Lyautey")
        #Tests the ``get_person_infos`` method
        response = self.api.get_person_infos(15570)
        response_large = self.api.get_person_infos(15570, profile="large")
        self.assertEqual(len(response["person"].keys()), 14)
        self.assertEqual(len(response_large["person"].keys()), 16)
        #Tests the ``get_news_infos`` method
        response = self.api.get_news_infos(18614628)
        self.assertEqual(response["news"]["title"], u'"Pulp Fiction" en mode remix ! [VIDEO]')
        #Tests the ``get_tvserie_infos`` method
        response = self.api.get_tvserie_infos(7157)
        self.assertEqual(response["tvseries"]["tag"][0]["$"], u"adaptation de roman")
        #Tests the ``get_infos`` method
        response = self.api.get_infos(190918, "movie")
        self.assertEqual(response, response_movie)

    def test_get_movie_reviews(self):
        """ Test the get movie reviews methods. """
        #Tests the ``get_movie_press_reviews`` method
        response = self.api.get_movie_press_reviews(190918)
        self.assertEqual(response["feed"]["totalResults"], 29)
        #Tests the ``get_movie_public_reviews`` method
        response = self.api.get_movie_public_reviews(190918)
        self.assertTrue(response["feed"]["totalResults"] > 29)

    def test_get_movies_times(self):
        """ Test the get movies times methods. """
        #Tests the ``get_movies_times_in_city`` method
        response_1 = self.api.get_movies_times_in_city(26200)
        self.assertEqual(response_1["feed"]["totalResults"], 4)
        #Tests the ``get_movies_times_in_theaters`` method
        response_2 = self.api.get_movies_times_in_theaters(["P1032"])
        self.assertEqual(response_2["feed"]["totalResults"], 1)
        #Tests the ``get_movies_times_in_theater`` method
        response_3 = self.api.get_movies_times_in_theater(theater_code="P1032")
        self.assertEqual(response_2, response_3)
        theater_name = u"Path\xe9 Grenoble - Chavant (ex Nef Chavant) "
        response = self.api.get_movies_times_in_theater(theater_name=theater_name)
        self.assertNotEqual(response.get("error"), None)
        movie = response_3["feed"]["theaterShowtimes"][0]["movieShowtimes"][0]["onShow"]["movie"]["code"]
        response_4 = self.api.get_movies_times_in_theater(theater_code="P1032", movie=movie)
        response_5 = self.api.get_movies_times_in_theater(theater_name=theater_name, movie=movie)
        self.assertEqual(response_4, response_5)
        #Tests the ``get_movies_times_near_coordinate`` method
        response_6 = self.api.get_movies_times_near_coordinate(44.560631, 4.749126, 5)
        self.assertEqual(len(response_6["feed"]["theaterShowtimes"]), 3)


if __name__ == "__main__":
    unittest.main()
