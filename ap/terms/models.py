import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


""" TERM models.py

This schedules module is for representing weekly trainee schedules.

Data Models
- Term:
    a term of the full-time training, consisting of twenty weeks

"""


class Term(models.Model):
    SPRING = 'Spring'
    FALL = 'Fall'

    # a term's long name; i.e. Fall 2013, Spring 2015
    name = models.CharField(max_length=12)

    # a term's short code; i.e. Fa13, Sp15
    code = models.CharField(max_length=4, unique=True)

    # a term's season; i.e. Spring/Fall
    season = models.CharField(max_length=6,
                              choices=(
                                  (SPRING, 'Spring'),
                                  (FALL, 'Fall'),
                              ),
                              default=None)

    # first day of the term, the monday of pre-training
    start = models.DateField(verbose_name='start date')

    # the last day of the term, the sat of semiannual
    end = models.DateField(verbose_name='end date')

    @staticmethod
    def current_term():
        """ Return the current term """
        try:
            return Term.objects.get(Q(start__lte=datetime.date.today()), Q(end__gte=datetime.date.today()))
        # this will happen in cases such as in-between terms (or empty DB, possibly)
        except ObjectDoesNotExist:
            # return an obviously fake term object
            return Term(name="Temp 0000", code="TM00", start=datetime.date.today(), end=datetime.date.today())


    def getDate(self, week, day):
        """ return an absolute date for a term week/day pair """
        return self.start + datetime.timedelta(week * 7 + day)

    def reverseDate(self, date):
        """ returns a term week/day pair for an absolute date """
        if self.start <= date <= self.end:
            # days since the term started
            delta = date - self.start
            return (delta / 7, delta % 7)
        # if not within the dates the term, return invalid result
        else:
            return (-1, -1)

    def get_absolute_url(self):
        return reverse('terms:detail', kwargs={'code': self.code})

    def __unicode__(self):
        return self.name
