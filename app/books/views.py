#-*- coding:utf8 -*-
from flask import Blueprint, request

from flask.views import View
from app.lusponse.lusponse import Lusponse
from app.books.models import Book, BookRegister

mod = Blueprint('books', __name__, url_prefix='/books')

class BookShared(View):
	methods = ['POST']

	def dispatch_request(self):
		try:
			user_id = int(request.form['userID'])
			title = request.form['bookTitle'].encode('utf-8')
			publish = request.form['bookPublish'].encode('utf-8')
			status = request.form['bookStatus'].encode('utf-8')
			author = request.form['bookAuthor'].encode('utf-8')
			sharing = request.form['bookSharing'].encode('utf-8')

			b = Book('', title, author, publish, status, sharing)
			b.commit()

			b = Book.get_book_with_title(title)
			b = b.pop()

			br = BookRegister(b.id, user_id)
			br.commit()

			response = Lusponse.make_success_response('success book share', '')
			return response

		except Exception, e:
			response = Lusponse.make_fail_response('fail book share', "%r"%e)
			return response

class BookSearch(View):
	methods = ['POST']

	def dispatch_request(self):
		try:
			bookname = request.form['bookName'].encode('utf-8')

			books = Book.search_books_with_title(bookname)
			response = Lusponse.make_success_response('success book search', books)
			return response

		except Exception, e:
			response = Lusponse.make_fail_response('fail book search', "%r"%e)
			return response

mod.add_url_rule('/share/', view_func=BookShared.as_view('bookshared'))
mod.add_url_rule('/search/', view_func=BookSearch.as_view('booksearch'))