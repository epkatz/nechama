from django.contrib import admin
from catalog.models import Book, Tag, BookTag, Location, BookCopy, Checkout

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(BookTag)
admin.site.register(Location)
admin.site.register(BookCopy)
admin.site.register(Checkout)

