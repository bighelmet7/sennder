import factory

from movies.models import Film, People
from sennder.common import Session


class FilmFactory(factory.Factory):

    class Meta:
        model = Film

    @factory.post_generation
    def peoples(obj, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for people in extracted:
                obj.peoples.append(people)


class PeopleFactory(factory.Factory):

    class Meta:
        model = People

    @factory.post_generation
    def films(obj, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for film in extracted:
                obj.films.append(film)
