from django.views.generic import ListView
from .models import Book


class IndexView(ListView):
    model = Book
    template_name = "library/index.html"


index = IndexView.as_view()
