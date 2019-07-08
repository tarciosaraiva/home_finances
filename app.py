from flask import Flask
from pony.flask import Pony

from core.database import db
from api import blueprint as api_bp

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

app.register_blueprint(api_bp)

# if __name__ == '__main__':
db.bind(**app.config['PONY'])
db.generate_mapping(create_tables=True)

app.run(debug=True)
