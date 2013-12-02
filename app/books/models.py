from app import db

from datetime import datetime
import base64

class Book(db.Model):
	__tablename__ = 'book'

	id = db.Column(db.Integer, primary_key = True)
	image = db.Column(db.String(50))
	title = db.Column(db.String(40))
	author = db.Column(db.String(15))
	publish = db.Column(db.String(40))
	status = db.Column(db.String(1))
	sharing = db.Column(db.String(1))

	def __init__(self, image=None, title='', author='', publish='', status='', sharing=''):
		self.image = image
		self.title = base64.encodestring(title)
		self.author = base64.encodestring(author)
		self.publish = base64.encodestring(publish)
		self.status = status
		self.sharing = sharing

	def __repr__(self):
		return '<Book %r>' % (base64.decodestring(self.title))

	def commit(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def get_book_with_title(cls, title):
		title = base64.encodestring(title)
		return cls.query.filter_by(title=title).all()


class BookRegister(db.Model):
	__tablename__ = 'book_register'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	register_date = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, id, user_id):
		self.id = id
		self.user_id = user_id

	def __repr__(self):
		return '<BookRegister %r %r %r>' % (self.id, self.user_id, self.register_date)

	def commit(self):
		db.session.add(self)
		db.session.commit()
