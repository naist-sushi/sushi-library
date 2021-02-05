from django.db import models
import uuid 

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


class event(models.Model):
    """Model representing a event ."""
    title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    eventtype = models.CharField(
        max_length=10,
        choices=EVENT_STATUS,
        blank=True,
        default='r',
        help_text='Book availability',
    )
    
    
EVENT_STATUS = (
        ('r', 'requested'),
        ('ar', 'approve the requesting'),
        ('rr', 'requesting rejected'),
        ('b', 'borrowed by someone'),
        ('s', 'stored to lab')
    )
   
    
   

   

    def __str__(self):
        """String for representing the Model object."""
        return self.title



class event_type (models.Model):
    """Model representing an event."""
    
    bookname = models.CharField(max_length=100)
    imprint = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    requested_date = models.DateField(null=True, blank=True)
    
    eventtype = models.CharField(
        max_length=10,
        choices=EVENT_STATUS,
        blank=True,
        default='r',
        help_text='Book availability',
    )
    
    
EVENT_STATUS = (
        ('r', 'requested'),
        ('ar', 'approve the requesting'),
        ('rr', 'requesting rejected'),
        ('b', 'borrowed by someone'),
        ('s', 'stored to lab')
    )



    class Meta:
        ordering = ['requested_date']

   

    def __str__(self):
       """String for representing the Model object."""
        return f'{self.event_type.eventtype} {self.id} ({self.book.title}) '