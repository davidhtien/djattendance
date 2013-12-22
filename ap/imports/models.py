from django.db import models
from accounts.models import User
from terms.models import Term

class Import(models.Model):
    
    user = models.ForeignKey(User)
    term = models.ForeignKey(Term)
    import_date = models.DateTimeField('import date')
    comments = models.CharField(max_length=500)
    total_success = models.IntegerField(null=True, default=0)
    total_failure = models.IntegerField(null=True, default=0)

    def __unicode__(self):
        return 'Import on ' + str(self.import_date) + ' by ' + self.user.get_full_name() + '.'