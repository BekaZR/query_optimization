import random
from django.core.management.base import BaseCommand
from mainapp.models import Author, Store, Book
from mainapp.select_related_test import book_list, book_list_select_related
from mainapp.prefetch_related import store_list, store_list_prefetch_related

class Command(BaseCommand):
    """
    Эта команда предназначена для вставки издателя, книги, магазина в базу данных.
    Добавляет 5 издателей, 100 книг, 10 магазинов.
    """

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        # создать 5 издателей
        author = [Author(name=f"Author{index}") for index in range(1, 6)]
        Author.objects.bulk_create(author)

        # создать по 20 книг для каждого издателя
        counter = 0
        books = []
        for author in Author.objects.all():
            for i in range(20):
                counter = counter + 1
                books.append(Book(name=f"Book{counter}", price=random.randint(50, 300), author=author))

        Book.objects.bulk_create(books)

        # создать 10 магазинов и вставить по 10 книг в каждый магазин
        books = list(Book.objects.all())
        for i in range(10):
            temp_books = [books.pop(0) for i in range(10)]
            store = Store.objects.create(name=f"Store{i+1}")
            store.books.set(temp_books)
            store.save()

print("This is a normal query to the database\n")
print(book_list())

print("\n"*5, "This is a query to the database using select_related\n")
book_list_select_related()

print("\n"*5, "This is a normal query to the database\n")
store_list()

print("\n"*5, "This is a query to the database using select_related\n")
store_list_prefetch_related()