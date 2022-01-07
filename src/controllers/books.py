from flask import Flask
from flask_restx import Resource

from src.server.instance import server

api = server.api

books_db = [
    {'id': 0, 'title': 'The witcher'},
    {'id': 1, 'title': 'Modusland'}
]

@api.route('/books')
class BookList(Resource):
    def get(self):
        return books_db