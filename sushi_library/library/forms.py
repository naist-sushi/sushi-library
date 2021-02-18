from django import forms
from .models import Book


class BookRegistrationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'cover', 'page_num', 'price')

    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)
        self.fields['name'].widget.attrs = {'placeholder': 'book name'}
        self.fields['name'].required = True
        self.fields['name'].initial = ''
        self.fields['author'].widget.attrs = {'placeholder': 'book author'}
        self.fields['author'].required = True
        self.fields['author'].initial = ''
        self.fields['cover'].required = False
        self.fields['page_num'].widget.attrs = {'placeholder': 'book page num'}
        self.fields['page_num'].required = False
        self.fields['price'].widget.attrs = {'placeholder': 'book price'}
        self.fields['price'].required = False

    def clean(self):
        super().clean()
