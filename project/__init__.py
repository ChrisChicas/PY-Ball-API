from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    from . import _config
    app.config['SQLALCHEMY_DATABASE_URI'] = _config.connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def index():
        return {"message": "Welcome to the Ball-API!"}
    
    from . import animal
    app.register_blueprint(animal.bp)
    
    return app