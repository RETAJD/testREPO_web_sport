from django.contrib import admin

# Register your models here.
from books.models import Book # nowe

admin.site.register(Book) # nowe
