from app import db

from datetime import datetime

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
		self.title = title
		self.author = author
		self.publish = publish
		self.status = status
		self.sharing = sharing

	def __repr__(self):
		return '<Book %r>' % (self.title)

	def commit(self):
		try:
			db.session.add(self)
			db.session.commit()
		except Exception, e:
			raise Exception('NotExistUser')

class BookRegister(db.Model):
	__tablename__ = 'book_register'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	register_date = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, id, user_id, register_date):
		self.id = id
		self.user_id = user_id
		self.register_date = register_date	

	def __repr__(self):
		return '<BookRegister %r>' % (self.title)

	def commit(self):
		db.session.add(self)
		db.session.commit()
