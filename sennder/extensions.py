# Extensions
import flask
from celery import Celery
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from studio_ghibli import StudioGhibli


class FlaskCelery(Celery):
    '''
    FlaskCelery object that can be properly set with
    the Flask app context.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patch_task()

        if 'app' in kwargs:
            self.init_app(kwargs['app'])

    def patch_task(self):
        TaskBase = self.Task
        _celery = self

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                if flask.has_app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
                else:
                    with _celery.app.app_context():
                        return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def init_app(self, app):
        '''
        Initialize Celery application.
        '''
        self.app = app
        self.config_from_object(app.config)


sg_client = StudioGhibli()
celery = FlaskCelery()
db = SQLAlchemy()
migrate = Migrate()
