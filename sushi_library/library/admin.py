from django.contrib import admin
from .models import Book, BookRequest, BookRequestImportance

admin.site.register(Book)
admin.site.register(BookRequest)
admin.site.register(BookRequestImportance)
