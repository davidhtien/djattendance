#from datetime import date

from django.db import models

#from aputils.models import Address

""" utilities models.py
This provides an analytics module for utility usage

LOCATION
    This represents each unique location for which a utility bill may be issued.

BILL
    This stores utility billing information for a particular location (electricity and gas).
"""

class Location(models.Model):
    """ Stores the information for a unique billing location for tracking utility usage.
    """
    
    # billing information
    customer_id = models.IntegerField()
    location_id = models.IntegerField(primary_key=True)
    # label used to identify this billing location
    name = models.CharField(verbose_name=u'location label', max_length=64)

    def __unicode__(self):
        return u' %s' % (self.name)

class Bill(models.Model):

    location = models.ForeignKey(Location)
    start_date = models.DateField(null=True,db_index=True)
    end_date = models.DateField(null=True)

    def _get_days(self):
        diff = self.end_date - self.start_date;
        return diff.days
    # days represented by this bill
    days = property(_get_days)
    
    # kwH (kilo Watt hours) of electricity
    electricity = models.IntegerField(null=True)
    # total expense from electricity
    electricity_cost = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    # HCF (hundreds of cubic feet) of natural gas
    gas = models.IntegerField(null=True)
    # total expense from gas
    gas_cost = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    
    def __unicode__(self):
        return u' %s: %s to %s' % (self.location.name,self.start_date,self.end_date)
    