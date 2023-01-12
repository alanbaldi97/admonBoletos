from flask import Flask
from utils.db import db
from routes.eventos import eventos
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

with app.app_context():
    db.create_all()


print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

app.register_blueprint(eventos)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
