from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, models.DO_NOTHING)
    public_year = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'
