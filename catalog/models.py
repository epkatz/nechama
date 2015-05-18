from django.db import models


class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField()
    author = models.CharField
    cover = models.URLField()
    tags = models.ManyToManyField('Tag', through='BookLabel')

    #MetaData
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField(null=True, blank=True)


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
