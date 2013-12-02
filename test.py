#-*- coding:utf8 -*-
import unittest

from flask.ext.testing import TestCase

from app import app, db
from app.users.models import User

import json

class ManyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        return app

    def setUp(self):
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_sinup(self):
        #Sign Up Test
        rv = self.sign_up(131072, '조성환', '2074', '01087662074')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'success'

        rv = self.sign_up(131072, '조성환', '2074', '01087662074')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'fail'
    def test_sinin(self):
        #Sign In Test
        rv = self.sign_in(131072,'WrongPassword')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'fail'

        rv = self.sign_in(131072,'2074')
        rv = json.loads(rv.data)
        print rv.get('code') == 'success'

    def sign_up(self, user_id, user_name, user_password, user_phone):
        return self.client.post('/users/signup/', data = dict(
            userID=user_id,
            userName=user_name,
            userPassword=user_password,
            userPhone=user_phone
            ), follow_redirects=True)

    def sign_in(self, user_id, user_password):
        return self.client.post('/users/signin/', data = dict(
            userID=user_id,
            userPassword=user_password,
            ), follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
