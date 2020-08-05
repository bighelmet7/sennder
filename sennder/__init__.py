from flask import Flask

from sennder.extensions import celery, db, migrate


def create_app(config_obj='sennder.config.DevelopmentConfig'):
    '''
    Returns a Flask application configured with the config_obj.
    '''
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(config_obj)

    from v1.blueprints import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from flask_cors import CORS
    CORS(app)

    celery.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db=db, render_as_batch=True)

    return app
