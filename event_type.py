# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:51:25 2021

@author: LiaoHungYi
"""
from django.db import models
import uuid # Required for unique book instances
   
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