from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/graphql-flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/initialize_database')
def initialize_database():
    with app.app_context():
        db.create_all()
        return 'Database initialized successfully'


@app.route('/')
def hello():
    return "My first API!"


if __name__ == '__main__':
    app.run(debug=True)
