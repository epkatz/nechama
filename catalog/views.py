from django.http import HttpResponseRedirect
from django.shortcuts import render
from catalog.forms import ISBNForm, BookForm
import openlibrary
from models import Book, BookCopy


def index(request):
    form = ISBNForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def view(request):
    books = BookCopy.objects.all()
    form = ISBNForm()
    context = {'form': form,
               'books': books}
    return render(request, 'index.html', context)


def search(request):
    form = ISBNForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        api = openlibrary.Api()
        isbn = str(cd['isbn'])
        book = api.get_book(isbn)
        title = book.get_title()
        author = book.get_authors()[0]
        cover = book.get_book_cover()['large']
        new_form = BookForm(initial={'isbn': isbn,
                                     'title': title,
                                     'author': author,
                                     'cover': cover})
        context = {'form': new_form,
                   'cover': cover}
    return render(request, 'book.html', context)


def save(request):
    form = BookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        new_book = Book(isbn=cd['isbn'],
                        title=cd['title'],
                        author=cd['author'],
                        cover=cd['cover'])
    new_book.save()
    return HttpResponseRedirect('/')


