#-*- coding:utf8 -*-
import unittest

from flask.ext.testing import TestCase

from app import app, db
from app.users.models import User
from app.books.models import Book, BookRegister

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

    def test_book_search(self):

        title_list = ['hi', 'manhi', 'hihi', 'manh', 'adsf']
        for title in title_list:
            b = Book('', title, 'a', 'b', '1', '1')
            b.commit()

        rv = self.book_search('hi')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'success'

    def test_book_shared(self):
        rv = self.sign_up(131072, '조성환', '2074', '01087662074')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'success'

        rv = self.book_share(131072, 'Jo', 'Sung', 'hwan', '0', '1')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'success'

        assert Book.query.count() == 1
        assert BookRegister.query.count() == 1

        rv = self.book_share(131072, '조', '성', '환', '0', '1')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'success'

    def test_sinup(self):
        #Sign Up Test
        rv = self.sign_up(131072, '조성환', '2074', '01087662074')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'success'

        rv = self.sign_up(131072, '조성환', '2074', '01087662074')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'fail'
        
        #Sign In Test
        rv = self.sign_in(131072,'WrongPassword')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'fail'

        rv = self.sign_in(131072,'2074')
        rv = json.loads(rv.data)
        assert rv.get('code') == 'success'
        

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

    def book_share(self, user_id, title ,author ,publish ,status , sharing):
        return self.client.post('/books/share/', data = dict(
            userID=user_id,
            bookTitle=title,
            bookAuthor=author,
            bookPublish=publish,
            bookStatus=status,
            bookSharing=sharing
            ), follow_redirects=True)
    def book_search(self, bookname):
        return self.client.post('/books/search/', data=dict(
            bookName = bookname
            ), follow_redirects=True)
if __name__ == '__main__':
    unittest.main()
