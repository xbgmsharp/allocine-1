# -*- coding:Utf-8 -*-
from allocine.api import AllocineApi


class Movie(object):
    """
    Represent a movie retrieved from the Allocine API.
    """

    def __init__(self, uid):
        """
        Retrieved the movie with the specified ID from the Allocine API.

        Param:
            ``uid`` -- The movie unique ID.

        """
        api = AllocineApi()
        self.datas = api.get_movie_infos(uid).get("movie")
        #TODO: Handle feature, tag, news, statistics, castMember

    #Base informations
    @property
    def id(self):
        return self.datas.get("code")

    @property
    def title(self):
        return self.datas.get("title")

    @property
    def type(self):
        return self.datas["movieType"].get("$")

    @property
    def nationality(self):
        return self.datas["nationality"].get("$")

    @property
    def duration(self):
        return self.datas.get("runtime") / 60

    #Production and distribution informations
    @property
    def distributor(self):
        return self.datas["release"]["distributor"].get("name")

    @property
    def production_year(self):
        return self.datas["release"].get("productionYear")

    @property
    def release_date(self):
        return self.datas.get("releaseDate")

    #Synopsis
    @property
    def synopsis_short(self):
        return self.datas.get("synopsisShort")

    @property
    def synopsis(self):
        return self.datas.get("synopsis")

    #Allocine ressources
    @property
    def poster(self):
        return self.datas["poster"].get("href")

    @property
    def trailer(self):
        return self.datas["trailer"].get("href")

    @property
    def link(self):
        return self.datas.get("link")[0]
