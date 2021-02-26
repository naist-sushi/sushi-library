from django.views.generic import ListView, CreateView

from .models import Book, Event, EventMessage
from .forms import BookRegistrationForm

BOOK_ARRIVE_EVENTMESSAGE_PK = 4
BOOK_ARRIVE_MSG = "Book arrive"


class IndexView(ListView):
    queryset = Book.objects.filter(event__message__message=BOOK_ARRIVE_MSG)
    template_name = "library/index.html"


class BookRegistrationView(CreateView):
    template_name = 'library/registration.html'
    form_class = BookRegistrationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        book = form.save()
        event_message = EventMessage.objects.get(pk=BOOK_ARRIVE_EVENTMESSAGE_PK)
        event = Event.objects.create(message=event_message,
                                     book=book,
                                     user=self.request.user)
        event.save()
        return super().form_valid(form)


index = IndexView.as_view()
register = BookRegistrationView.as_view()
