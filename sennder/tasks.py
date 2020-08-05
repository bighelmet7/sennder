# Celery tasks
from celery.signals import task_postrun


from movies.models import Film, People
from sennder import create_app
from sennder.extensions import db, sg_client, celery

app = create_app()


@celery.task(name='update_db')
def update_db():
    '''
    Update every minute the database with the values
    fetched from the StudioGhibli database.
    '''
    films_dict = {
        f["id"]: f["title"] for f in sg_client.films(fields=["id", "title"])
    }
    peoples = sg_client.people(fields=["id", "name", "films"])
    for people in peoples:
        people_obj = People.get_or_create(id=people["id"], name=people["name"])
        for film_url in people["films"]:
            film_id = film_url.split('/')[-1]  # https://hst.com/films/<str:id>
            film_obj = Film.get_or_create(
                id=film_id, title=films_dict[film_id]
            )
            if film_obj not in people_obj.films:
                people_obj.films.append(film_obj)
        people_obj.save()
    return


@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()
