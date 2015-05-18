from django import forms


class ISBNForm(forms.Form):
    isbn = forms.CharField()