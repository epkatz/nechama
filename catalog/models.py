from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.URLField()
    tag_list = models.ManyToManyField('Tag', through='BookTag')
    #MetaData
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)


class BookTag(models.Model):
    Book = models.ForeignKey(Book)
    Tag = models.ForeignKey(Tag)
    #Metadata
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField(null=True, blank=True)


class Location(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)

    def __str__(self):
        return "%s in %s" % (self.name, self.school)


class BookCopy(models.Model):
    Book = models.ForeignKey(Book)
    Location = models.ForeignKey(Location)

    def __str__(self):
        return "%s located at %s in %s" % (self.Book.title, self.Location.name, self.Location.school)