from django import forms


class ISBNForm(forms.Form):
    isbn = forms.CharField()


class BookForm(forms.Form):
    isbn = forms.CharField()
    title = forms.CharField()
    author = forms.CharField()
    cover = forms.URLField(widget=forms.TextInput(attrs={'onchange':'readURL(this);'}))