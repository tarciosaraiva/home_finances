from flask_restplus import Api, Namespace

from .status import Status

ns = Namespace('health', description='API telemetry operations')

ns.add_resource(Status, '/status')