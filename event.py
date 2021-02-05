# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:08:38 2021

@author: LiaoHungYi
"""

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

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

  
