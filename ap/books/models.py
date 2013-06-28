from django.db import models

""" BOOKS models.py

The BOOKS module is a utility module that is used by other modules such as
class syllabus and life-studies. It is used primarily to represent ministry
books, but can be adapted for any book, such as non-LSM books in the library.

Data Models:
    - Book: a single title
    - Collection: a series of books, such as the Life-study
    - Publisher: a book publisher, such as LSM or A&C Press
"""

class Collection(models.Model):

    # the name of the collection, e.g. The Life-study of the Bible
    # (Life-study is a series, but LS of Genesis is not)
    name = models.CharField(max_length=100)

    # the abbreviation of this collection, e.g. LS
    code = models.CharField(max_length=10)


class Publisher(models.Model):

    # the name of the publisher
    name = models.CharField(max_length=200)

    # the abbreviation of the publisher's name
    code = models.CharField(max_length=20)

class Book(models.Model):

    # the ISBN of this book
    isbn = models.IntegerField(primary_key=True)

    # the title of the book, e.g. Young People's Training
    name = models.CharField(max_length=200)

    # the abbreviation of the book's title, e.g. YPT
    code = models.CharField(max_length=20)

    # number of messages/chapters in this volume
    chapters = models.SmallIntegerField(blank=True)

    # the collection this book belongs to, if any
    collection = models.ForeignKey(Collection, blank=True)

    # the book's publisher
    publisher = models.ForeignKey(Publisher)

