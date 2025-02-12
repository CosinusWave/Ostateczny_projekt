from django import forms
from .models import User, Book, DVD

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class BookBorrowForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(is_borrowed=False), label="Wybierz książkę do wypożyczenia")

class DVDBorrowForm(forms.Form):
        dvd = forms.ModelChoiceField(queryset=DVD.objects.filter(is_borrowed=False),
                                     label="Wybierz DVD do wypożyczenia")