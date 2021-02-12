import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def get_file_path(instance, filename):
    image_dir = 'images/'
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(image_dir, filename)


class Book(models.Model):
    class Meta:
        db_table = "book"

    name = models.CharField(verbose_name="name",
                            max_length=255,
                            null=False,
                            unique=True,
                            db_index=True,
                            blank=False,
                            default="BOOK_NAME")
    author = models.CharField(verbose_name="author",
                              max_length=255,
                              null=False,
                              blank=False,
                              default="AUTHOR")
    isbn = models.CharField(verbose_name="isbn",
                            max_length=255,
                            null=True)
    cover = models.ImageField(verbose_name="cover",
                              upload_to=get_file_path,
                              null=True)
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToFill(200, 200)],
                                     format='JPEG',
                                     options={'quality': 85})

    page_num = models.IntegerField(verbose_name="page_num",
                                   null=True)
    price = models.IntegerField(verbose_name="price",
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookRequestImportance(models.Model):
    class Meta:
        db_table = 'book_request_importance'

    value = models.IntegerField(verbose_name="value",
                                null=False,
                                unique=True,
                                blank=False,
                                db_index=True)
    message = models.CharField(verbose_name="message",
                               max_length=255,
                               null=False,
                               unique=True,
                               blank=False)

    def __str__(self):
        return self.message


class BookRequest(models.Model):
    class Meta:
        db_table = 'book_request'

    reason = models.TextField(verbose_name="reason",
                              null=False,
                              blank=False)
    importance = models.ForeignKey(BookRequestImportance,
                                   verbose_name="importance",
                                   on_delete=models.PROTECT)
    book = models.ForeignKey(Book,
                             verbose_name="book",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventMessage(models.Model):
    class Meta:
        db_table = "event_message"

    message = models.CharField(verbose_name="message",
                               max_length=255,
                               null=False,
                               unique=True,
                               blank=False)

    def __str__(self):
        return self.message


class Event(models.Model):
    class Meta:
        db_table = "event"

    message = models.ForeignKey(EventMessage,
                                verbose_name="message",
                                on_delete=models.PROTECT)
    book = models.ForeignKey(Book,
                             verbose_name="book",
                             on_delete=models.PROTECT)
    user = models.ForeignKey(User,
                             verbose_name="user",
                             on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.name + "-" + self.message.message
