# from django import forms 
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ['name', 'price']
        fields = "__all__"
