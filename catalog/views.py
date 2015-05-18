from django.shortcuts import render
from catalog.forms import ISBNForm
import openlibrary



def index(request):
    form = ISBNForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def search(request):
    form = ISBNForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        api = openlibrary.Api()
        book = api.get_book(cd['isbn'])
        context = {'book': book}
    else:
        context = {'book': 'error'}
    return render(request, 'book.html', context)

