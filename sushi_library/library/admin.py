from django.contrib import admin
from .models import BookStatus, BookRequest, BookRequestImportance

admin.site.register(BookStatus)
admin.site.register(BookRequest)
admin.site.register(BookRequestImportance)
