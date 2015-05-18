# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('cover', models.URLField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted_datetime', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted_datetime', models.DateTimeField(null=True, blank=True)),
                ('Book', models.ForeignKey(to='catalog.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='booktag',
            name='Tag',
            field=models.ForeignKey(to='catalog.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='tag_list',
            field=models.ManyToManyField(to='catalog.Tag', through='catalog.BookTag'),
            preserve_default=True,
        ),
    ]
