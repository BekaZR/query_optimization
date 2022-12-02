from mainapp.models import Store
from mainapp.services import query_debugger


#this is normal request from db
@query_debugger
def store_list():

    queryset = Store.objects.all()

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return stores

#this is request from db using prefetch related
@query_debugger
def store_list_prefetch_related():

    queryset = Store.objects.prefetch_related('books')

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return stores
