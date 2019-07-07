from flask import Flask
from pony.flask import Pony

from core.database import db
from apis.health import blueprint as health_api
from apis.admin import blueprint as admin_api

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

Pony(app)

app.register_blueprint(health_api, url_prefix='/api/v1')
app.register_blueprint(admin_api, url_prefix='/api/v1/admin')

# if __name__ == '__main__':
db.bind(**app.config['PONY'])
db.generate_mapping(create_tables=True)

app.run(debug=True)
