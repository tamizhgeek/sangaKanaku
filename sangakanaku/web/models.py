from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta

# Create your models here.

VALID_MONTHS = ['previous', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']

class House(models.Model):
    ACCOUNT_TYPES = (
        ('ADVE', 'Cash in Advance'),
        ('HAND', 'Cash in Hand')
    )
    name = models.CharField(max_length = 200)
    account_type = models.CharField(max_length = 4, choices = ACCOUNT_TYPES)
    members = models.ManyToManyField(User, related_name = "members")
    rent = models.IntegerField()
    admins = models.ManyToManyField(User, related_name = 'house_admins')

    def __unicode__(self):
        return self.name


    def calculate_rent(self, month = 'previous'):
        if month not in VALID_MONTHS:
            raise "Invalid month : %s"%month

        if(month == 'previous'):
            now = datetime.datetime.now()
            prev_month = (now - relativedelta(months = 1)).month
            expenses = self.expenses.all().filter(date__month = prev_month)
        else:
            month = VALID_MONTHS.index(month)
            expenses = self.expenses.all().filter(date__month = month)
        total = reduce(lambda x,y: x + y.amount, expenses, self.rent)
        each_share = total / len(self.members.all())

        member_share = {}
        for member in self.members.all():
            sum = 0
            member_share[member] = each_share - reduce(lambda x,y: x + (y.amount if y.bearer == member else 0), expenses, 0)
        print member_share
        return member_share
            

class Expense(models.Model):
    description = models.TextField()
    bearer = models.ForeignKey(User)
    amount = models.IntegerField()
    house = models.ForeignKey(House, related_name="expenses")
    date = models.DateTimeField()
    receipt = models.FileField(upload_to = "/tmp", blank = True, null = True)

    def __unicode__(self):
        return self.description
    


