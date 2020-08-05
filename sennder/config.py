import os

from celery.schedules import crontab


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    TESTING = False

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'exam.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery
    CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
    BROKER_URL = 'amqp://localhost:5672//'
    CELERY_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TIMEZONE = 'Europe/Madrid'
    CELERY_ENABLE_UTC = True
    CELERYBEAT_SCHEDULE = {
        'update_db_every_minute': {
            'task': 'update_db',
            'schedule': crontab(minute='*'),
        },
    }


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    BROKER_URL = 'amqp://guest:guest@broker:5672//'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sennder:sennder-test@db:5432/sennder'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
