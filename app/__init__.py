#-*- coding:utf8 -*-
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app.users.views import mod as usersModule
from app.books.views import mod as booksModule

app.register_blueprint(usersModule)
app.register_blueprint(booksModule)

