# -*- coding:Utf-8 -*-
import requests


class AllocineAPI(object):
    """ Allocine API wrapper. """

    def __init__(self):
        self.api_version = 3
        self.format = "json"
        self.partner = "YW5kcm9pZC12M3M"
        self.base_url = "http://api.allocine.fr/rest/v3/"
        self.base_params = {
            "format": self.format,
            "partner": self.partner
        }

    def _send(self, url, params):
        r = requests.get(url, params=params)
        return r.json()

    def _search(self, query, otype):
        url = "{0}{1}".format(self.base_url, "search")
        params = dict(self.base_params, **{
            "q": query,
            "filter": otype
        })
        return self._send(url, params)

    def _get_infos(self, uid, otype, profile=None, media=None):
        profile = profile if profile is not None else "medium"
        url = "{0}{1}".format(self.base_url, otype)
        params = dict(self.base_params, **{
            "code": uid,
            "profile": profile,
            "filter": otype
        })
        if media is not None:
            params = dict(params, **{"mediafmt": media})
        return self._send(url, params)

    def _get_reviews(self, uid, rtype=None):
        url = "{0}{1}".format(self.base_url, "reviewlist")
        params = dict(self.base_params, **{
            "code": uid,
            "type": "movie"
        })
        if rtype is not None:
            params = dict(params, **{"filter": rtype})
        return self._send(url, params)

    def _get_movies_times(self, *args, **kwargs):
        url = "{0}{1}".format(self.base_url, "showtimelist")
        params = self.base_params
        for name, value in kwargs.items():
            if value is not None:
                if name == "zip_code":
                    name = "zip"
                if name == "theater_name":
                    name = "location"
                params = dict(params, **{name: value})
        #TODO: Formats the date
        return self._send(url, params)

    def search(self, query):
        """
        Return the result of the search based on the specified query.

        The search is done for movies, theaters, news, tv series and persons.

        Param:
            ``query`` -- The search string.

        """
        return self._search(query, ["movie", "theater", "person", "news", "tvseries"])

    def search_movie(self, query):
        """
        Return the result of the *movies* search based on the specified query.

        Param:
            ``query`` -- The search string.

        """
        return self._search(query, "movie")

    def search_theater(self, query):
        """
        Return the result of the *theaters* search based on the specified query.

        Param:
            ``query`` -- The search string.

        """
        return self._search(query, "theater")

    def search_person(self, query):
        """
        Return the result of the *actors, directors, or producers* search based on the specified query.

        Param:
            ``query`` -- The search string.

        """
        return self._search(query, "person")

    def search_news(self, query):
        """
        Return the result of the *news* search based on the specified query.

        Param:
            ``query`` -- The search string.

        """
        return self._search(query, "news")

    def search_tvserie(self, query):
        """
        Return the result of the *tv series* search based on the specified query.

        Param:
            ``query`` -- The search string.

        """
        return self._search(query, "tvseries")

    def get_infos(self, uid, otype, profile=None, media=None):
        """
        Return all the informations about the specified item.

        Param:
            ``uid`` -- The item unique ID.

            ``otype`` -- The item type. Can be ``movie``, ``theater``,
            ``person``, ``news`` or ``tvseries``.

            ``profile`` -- (optional) The amount of returned informations.
            Can be ``small``, ``medium`` or ``large`` (default is medium).

            ``media`` -- (optional) The media format, see the media format's
            page for all the informations.

        """
        return self._get_infos(uid, otype, profile, media)

    def get_movie_infos(self, uid, profile=None, media=None):
        """
        Return all the informations about the specified movie.

        Param:
            ``uid`` -- The movie unique ID.

            ``profile`` -- (optional) The amount of returned informations.
            Can be ``small``, ``medium`` or ``large`` (default is medium).

            ``media`` -- (optional) The media format, see the media format's
            page for all the informations.

        """
        return self._get_infos(uid, "movie", profile, media)

    def get_theater_infos(self, uid, profile=None, media=None):
        """
        Return all the informations about the specified theater.

        Param:
            ``uid`` -- The theater unique ID.

            ``profile`` -- (optional) The amount of returned informations.
            Can be ``small``, ``medium`` or ``large`` (default is medium).

            ``media`` -- (optional) The media format, see the media format's
            page for all the informations.

        """
        return self._get_infos(uid, "theater", profile, media)

    def get_person_infos(self, uid, profile=None, media=None):
        """
        Return all the informations about the specified person.

        Param:
            ``uid`` -- The person unique ID.

            ``profile`` -- (optional) The amount of returned informations.
            Can be ``small``, ``medium`` or ``large`` (default is medium).

            ``media`` -- (optional) The media format, see the media format's
            page for all the informations.

        """
        return self._get_infos(uid, "person", profile, media)

    def get_news_infos(self, uid, profile=None, media=None):
        """
        Return all the informations about the specified news.

        Param:
            ``uid`` -- The news unique ID.

            ``profile`` -- (optional) The amount of returned informations.
            Can be ``small``, ``medium`` or ``large`` (default is medium).

            ``media`` -- (optional) The media format, see the media format's
            page for all the informations.

        """
        return self._get_infos(uid, "news", profile, media)

    def get_tvserie_infos(self, uid, profile=None, media=None):
        """
        Return all the informations about the specified tv serie.

        Param:
            ``uid`` -- The tv serie unique ID.

            ``profile`` -- (optional) The amount of returned informations.
            Can be ``small``, ``medium`` or ``large`` (default is medium).

            ``media`` -- (optional) The media format, see the media format's
            page for all the informations.

        """
        return self._get_infos(uid, "tvseries", profile, media)

    def get_movie_reviews(self, uid):
        """
        Return the reviews made by the press and the community about
        the specified movie.

        Param:
            ``uid`` -- The movie unique ID.

        """
        return self._get_reviews(uid, None)

    def get_movie_press_reviews(self, uid):
        """
        Return the reviews made by the press about the specified movie.

        Param:
            ``uid`` -- The movie unique ID.

        """
        return self._get_reviews(uid, "desk-press")

    def get_movie_public_reviews(self, uid):
        """
        Return the reviews made by the community about the specified movie.

        Param:
            ``uid`` -- The movie unique ID.

        """
        return self._get_reviews(uid, "public")

    def get_movies_times_in_city(self, zip_code, movie=None, date=None):
        """
        Return the movies times for all the theaters in the specified city.

        Param:
            ``zip_code`` -- The city zip code (ex: 26200).

            ``movie`` -- (optional) A movie uid. If provided, return only the
            schedule for the specified movie.

            ``date`` -- (optional) A date object for the research. If not provided,
            the current day is used.

        """
        return self._get_movies_times(zip_code=zip_code, movie=movie, date=date)

    def get_movies_times_in_theaters(self, theaters, movie=None, date=None):
        """
        Return the movies times for all the specified theaters.

        Param:
            ``theaters`` -- A list with theaters code (ex: ["P0728", "P0093"]).

            ``movie`` -- (optional) A movie uid. If provided, return only the
            schedule for the specified movie.

            ``date`` -- (optional) A date object for the research. If not provided,
            the current day is used.

        """
        return self._get_movies_times(theaters=theaters, movie=movie, date=date)

    def get_movies_times_in_theater(self, theater_code=None, theater_name=None, movie=None, date=None):
        """
        Return the movies times for the specified theater.
        There is two ways to specified a theater, with its code or with its name.

        One of the ``theater_code`` or ``theater_name`` parameters must be specified.

        If the ``theater_name`` is specified, the ``movie`` parameter must be specified too.

        Param:
            ``theater_code`` -- (optional) The theater code (ex: "P0728").

            ``theater_name`` -- (optional) The theater name (ex: "le palace montelimar").

            ``movie`` -- (optional) A movie uid. If provided, return only the
            schedule for the specified movie.

            ``date`` -- (optional) A date object for the research. If not provided,
            the current day is used.

        """
        if theater_name is not None:
            return self._get_movies_times(theater_name=theater_name, movie=movie, date=date)
        return self._get_movies_times(theaters=[theater_code], movie=movie, date=date)

    def get_movies_times_near_coordinate(self, lat, long, radius, movie=None, date=None):
        """
        Return the movies times for all the theaters near the specified coordinate.

        Param:
            ``lat`` -- The latitude.

            ``long`` -- The longitude.

            ``radius`` -- The radius around the specified point, in kilometers.

            ``movie`` -- (optional) A movie uid. If provided, return only the
            schedule for the specified movie.

            ``date`` -- (optional) A date object for the research. If not provided,
            the current day is used.

        """
        return self._get_movies_times(lat=lat, long=long, radius=radius, movie=movie, date=date)
