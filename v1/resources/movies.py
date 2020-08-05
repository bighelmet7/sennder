
from flask import request
from flask_restful import Resource

from movies.models import Film
from sennder.extensions import sg_client


class MoviesResource(Resource):

    '''
    Resource for the movies model.
    '''

    def get(self):
        films = Film.query.all()
        movies = list()
        for film in films:
            movies.append(
                {'title': film.title, 'people': [p.name for p in film.peoples]}
            )
        return movies
