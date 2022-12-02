from django.contrib import admin

from mainapp.models import Author, Book, Store

admin.site.register(Store)
admin.site.register(Author)
admin.site.register(Book)
