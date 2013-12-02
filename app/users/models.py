#-*- coding:utf8 -*-
from app import db
import base64

from app.books.models import BookRegister

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(40))
	password = db.Column(db.String(30))
	phone = db.Column(db.String(15))

	book_register = db.relationship('BookRegister', backref='user', lazy='dynamic')

	def __init__(self, id=None, name=None, password=None, phone=None):
		self.id=id
		self.name=base64.encodestring(name)
		self.password=password
		self.phone=phone

	def __repr__(self):
		return '<User %d : %r : %r>' % (self.id, self.name, self.phone)

	def get_name(self):
		return base64.decodestring(self.name)

	def commit(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def get_user(cls, id, password):
		password = password
		u=User.query.filter_by(id=id, password=password).first()
		return u
