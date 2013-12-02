#!/usr/bin/env python
import os
import readline
from pprint import pprint

from flask import *
from app import *

#Import Luman Utility
from app.lusponse.lusponse import Lusponse

#Import Models
from app.users.models import User
from app.books.models import Book, BookRegister

os.environ['PYTHONINSPECT'] = 'True'

