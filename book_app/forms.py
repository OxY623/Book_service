from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Book
        fields = ['title', 'authors']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']