from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'

    from app.routes import bp
    app.register_blueprint(bp)

    socketio.init_app(app)
    from app import events  # noqa: F401  (registers SocketIO handlers)

    return app
