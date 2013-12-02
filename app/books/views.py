from flask import Blueprint, request

from flask.views import View

mod = Blueprint('books', __name__, url_prefix='/books')
"""
class SignUp(View):
	methods = ['POST']

	def dispatch_request(self):
		try:
			pass
		except Exception, e:
			pass

class SignIn(View):
	methods = ['POST']

	def dispatch_request(self):
		try:
			pass
		except Exception, e:
			pass


mod.add_url_rule('/signup/', view_func=SignUp.as_view('signup_user'))
mod.add_url_rule('/signin/', view_func=SignIn.as_view('signin_user'))
"""