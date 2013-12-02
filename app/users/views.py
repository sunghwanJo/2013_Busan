#-*- coding:utf8 -*-
from flask import Blueprint, request
from flask.views import View

from app.users.models import User
from app.lusponse.lusponse import Lusponse

from sqlalchemy.exc import IntegrityError
from app import db

mod = Blueprint('users', __name__, url_prefix='/users')

class SignUp(View):
	methods = ['POST']

	def dispatch_request(self):
		try:
			id = int(request.form['userID'])
			name = request.form['userName'].encode('utf-8')
			password = request.form['userPassword'].encode('utf-8')
			phone = request.form['userPhone'].encode('utf-8')

			if User.query.filter_by(id=id).first() != None:
				raise Exception('IntegrityError')

			u = User(id, name, password, phone)
			u.commit()

			response = Lusponse.make_success_response('success sign up', '')
			return response

		except Exception, e:
			response = Lusponse.make_fail_response('fail sign up', "%r"%e)
			return response

class SignIn(View):
	methods = ['POST']

	def dispatch_request(self):
		try:
			id = int(request.form['userID'])
			password = request.form['userPassword']

			u = User.get_user(id, password)
			if u == None:
				raise Exception('NotExistUser')

			response = Lusponse.make_success_response('success sign in', '')
			return response
		except Exception, e:
			response = Lusponse.make_fail_response('fail sign in', "%r"%e)
			return response


mod.add_url_rule('/signup/', view_func=SignUp.as_view('signup_user'))
mod.add_url_rule('/signin/', view_func=SignIn.as_view('signin_user'))

