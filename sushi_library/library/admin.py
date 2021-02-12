from django.contrib import admin
from .models import Book, BookRequest, BookRequestImportance, Event, EventMessage

admin.site.register(Book)
admin.site.register(BookRequest)
admin.site.register(BookRequestImportance)
admin.site.register(Event)
admin.site.register(EventMessage)
