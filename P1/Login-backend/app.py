from flask import Flask
from controller.user_controller import uc
from flask_cors import CORS
from flask_session import Session

if __name__ == "__main__":
    app = Flask(__name__)

    app.secret_key = 'lesecretleew'
    app.config['SESSION_TYPE'] = 'filesystem'

    CORS(app, supports_credentials=True)
    Session(app)

    app.register_blueprint(uc)

    app.run(port=5050, debug=True)

