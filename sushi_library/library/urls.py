from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/register/', login_required(views.register), name='register'),
]
