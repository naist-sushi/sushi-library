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
