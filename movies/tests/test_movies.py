import unittest

import sqlalchemy
from movies.tests.factories import FilmFactory, PeopleFactory
from movies.models import Film, People
from sennder.common import Session


class FilmTest(unittest.TestCase):

    def setUp(self):
        self.engine = sqlalchemy.create_engine('sqlite://')
        Session.configure(bind=self.engine)
        self.session = Session()

    def test_film_creation(self):
        # Having a dict that contains a film information.
        json_response = {'id': '1234-asdf-1234', 'title': 'World of tests'}
        # The film should be created in our database as a Film object.
        film = FilmFactory.create(**json_response)
        # Then the Film ID should be the same as the inside json_response.
        expected = json_response['id']
        self.assertEqual(expected, film.id)

    def test_adding_peoples_to_film(self):
        # Having a dict that contains a film information and a people
        # information.
        json_film = {'id': '1234-asdf-1234-asdf', 'title': 'Test Test'}
        json_people = {'id': '1234-asdf-1234-asdf', 'name': 'Test Character'}
        # The film should be created in our database as a Film object
        # with the given people.
        people = PeopleFactory.create(
            id=json_people['id'],
            name=json_people['name'],
        )
        film = FilmFactory.create(
            id=json_film['id'],
            title=json_film['title'],
            peoples=(people,)
        )
        # Then the people should be added to the film object.
        expected_len = 1
        self.assertEqual(expected_len, len(film.peoples.all()))

    def tearDown(self):
        # No changes in the database.
        self.session.rollback()
        # Remove session for nexts test cases.
        Session.remove()


class PeopleTest(unittest.TestCase):

    def setUp(self):
        self.engine = sqlalchemy.create_engine('sqlite://')
        Session.configure(bind=self.engine)
        self.session = Session()

    def test_people_creation(self):
        # Having a dict that contains a people information.
        json_response = {'id': '1234-asdf-1234-asdf', 'name': 'Japanse name'}
        # The people should be created in our database as a People object.
        people = PeopleFactory.create(**json_response)
        # Then the People ID should be the same as the inside of the
        # json_response.
        expected = json_response['id']
        self.assertEqual(expected, people.id)

    def test_adding_films_to_people(self):
        # Having a dict that contains a people information and a film
        # information.
        json_people = {'id': '1234-asdf-1234-asdf', 'name': 'JapanaseName'}
        json_film = {'id': '1234-asdf-1234-asdf', 'title': 'World of tests'}
        # The people should be created in our database as a People object
        # with the given film.
        film = FilmFactory.create(**json_film)
        people = PeopleFactory.create(
            id=json_people['id'],
            name=json_people['name'],
            films=(film,)
        )
        # Then the film should be added to the people object.
        expected_len = 1
        self.assertEqual(expected_len, len(people.films.all()))

    def tearDown(self):
        # No changes in the database.
        self.session.rollback()
        # Remove session for nexts test cases.
        Session.remove()
