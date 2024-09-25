from flask import Flask #import flask from flask package


from flask_sqlalchemy import SQLAlchemy
#SQLAlchemy is an ORM (Object-Relational Mapping) tool, 
# which makes it easier to interact with databases using Python objects instead of writing raw SQL queries.

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'simple_key_for_project'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'instance', 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
