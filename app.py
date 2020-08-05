import os

from flask import Flask, render_template

from const import status_code
from sennder import create_app

env = os.environ.get('APPLICATION_ENV', 'sennder.config.DevelopmentConfig')
app = create_app(env)


@app.errorhandler(status_code.HTTP_STATUS_INTERNAL_SERVER_ERROR)
def handler_unexpected_error(error):
    return 'Unexpected error\n', status_code.HTTP_STATUS_INTERNAL_SERVER_ERROR


@app.route('/ping/')
def ping():
    return {"ping": "pong"}, status_code.HTTP_STATUS_OK


# INFO: Code snippet: http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
