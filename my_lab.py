import re

book_list = ['hi', 'manhi', 'hihi', 'manh', 'adsf']

title = 'hi'
pattern = '*.'+title+'*.'
for book in book_list:
	print book
	print title in book
