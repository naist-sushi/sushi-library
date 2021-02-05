from django.db import models


class BookStatus(models.Model):
    class Meta:
        db_table = 'book_status'

    status_msg = models.CharField(verbose_name="status_msg",
                                  max_length=255,
                                  null=False,
                                  unique=True,
                                  db_index=True,
                                  blank=False)

    def __str__(self):
        return self.status_msg


class Book(models.Model):
    class Meta:
        db_table = "book"
    # TODO implement


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
