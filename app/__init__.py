
from flask import Flask
from config import Config
from app.extensions import db, jwt, bcrypt

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from app.auth import auth_bp
    from app.tasks import tasks_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")

    with app.app_context():
        db.create_all()

    return app
