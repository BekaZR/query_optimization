from mainapp.services import query_debugger
from mainapp.models import Book

#function without select related
#this decorator out time working 
@query_debugger
def book_list():
    
    queryset = Book.objects.all()
    
    books = []
    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'author': book.author.name})
    
    return book

#request from db with select related
#this decorator out time working
@query_debugger
def book_list_select_related():

    queryset = Book.objects.select_related('author').all()

    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'author': book.author.name})

    return books
