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
        return self._send(url, params)

    def _get_review(self, uid, rtype=None):
        url = "{0}{1}".format(self.base_url, "reviewlist")
        params = dict(self.base_params, **{
            "code": uid,
            "type": "movie"
        })
        if rtype is not None:
            params = dict(params, **{"filter": rtype})
        return self._send(url, params)

    def search(self, query):
        return self._search(query, ["movie", "theater", "person", "news", "tvseries"])

    def search_movie(self, query):
        return self._search(query, "movie")

    def search_theater(self, query):
        return self._search(query, "theater")

    def search_person(self, query):
        return self._search(query, "person")

    def search_news(self, query):
        return self._search(query, "news")

    def search_tvserie(self, query):
        return self._search(query, "tvseries")

    def get_infos(self, uid, otype, profile=None, media=None):
        return self._get_infos(uid, otype, profile, media)

    def get_movie_infos(self, uid, profile=None, media=None):
        return self._get_infos(uid, "movie", profile, media)

    def get_theater_infos(self, uid, profile=None, media=None):
        return self._get_infos(uid, "theater", profile, media)

    def get_person_infos(self, uid, profile=None, media=None):
        return self._get_infos(uid, "person", profile, media)

    def get_news_infos(self, uid, profile=None, media=None):
        return self._get_infos(uid, "news", profile, media)

    def get_tvserie_infos(self, uid, profile=None, media=None):
        return self._get_infos(uid, "tvseries", profile, media)

    def get_movie_review(self, uid):
        return self._get_review(uid, None)

    def get_movie_press_review(self, uid):
        return self._get_review(uid, "desk-press")

    def get_movie_public_review(self, uid):
        return self._get_review(uid, "public")