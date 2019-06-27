from flask import Flask
from pony.flask import Pony

from core.database import setup_database
from apis.health import blueprint as health_api

app = Flask(__name__, instance_relative_config=True)
app.config.update(dict(
    DEBUG = False,
    PONY = dict(
        provider = 'postgres',
        host = 'localhost',
        user = 'home_finance',
        password = 'home_finance',
        database = 'home_finance'
    )
))

setup_database(app.config['PONY'])

Pony(app)

app.register_blueprint(health_api, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
