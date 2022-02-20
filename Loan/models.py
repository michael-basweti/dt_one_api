from django.db import models
from Authentication.models import User

# Create your models here.
class Payavenue(models.Model):
    payavenueid = models.AutoField(primary_key=True)
    payavenuedescription = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'payavenue'
class Loans(models.Model):
    loanid = models.AutoField(primary_key=True)
    requestedby = models.ForeignKey(User, models.DO_NOTHING, db_column='requestedby', related_name='requestedby')
    requestedon = models.DateField(auto_now=True)
    requestedat = models.TimeField(auto_now=True)
    amountrequested = models.DecimalField(max_digits=28, decimal_places=2)
    amountdispatched = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    amountpaid = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    approved = models.BooleanField(default=False)
    remainingamount = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    approvedby = models.ForeignKey(User, models.DO_NOTHING, db_column='approvedby', blank=True, null=True, related_name='appreovedby')
    description = models.CharField(max_length=500)
    payavenue = models.ForeignKey(Payavenue, models.DO_NOTHING, db_column='payavenue')
    paymentdate = models.DateField(blank=True, null=True)
    denied = models.BooleanField(blank=True, null=True)
    deniedreason = models.CharField(max_length=500, blank=True, null=True)
    approvalcomments = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loans'


class Payments(models.Model):
    paymentid = models.AutoField(primary_key=True)
    processedby = models.ForeignKey(User, models.DO_NOTHING, db_column='processedby')
    processedon = models.DateField(auto_now=True)
    processedat = models.TimeField(auto_now=True)
    amountpaid = models.DecimalField(max_digits=28, decimal_places=2)
    paymenttype = models.ForeignKey('Paymenttype', models.DO_NOTHING, db_column='paymenttype')
    payavenue = models.ForeignKey(Payavenue, models.DO_NOTHING, db_column='payavenue')

    class Meta:
        managed = False
        db_table = 'payments'


class Paymenttype(models.Model):
    paymenttypeid = models.AutoField(primary_key=True)
    paymentypedescription = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'paymenttype'

