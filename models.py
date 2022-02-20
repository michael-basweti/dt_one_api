# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthenticationUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    deleted = models.BooleanField()
    is_superuser = models.BooleanField(blank=True, null=True)
    usertype = models.ForeignKey('Usertypes', models.DO_NOTHING, db_column='usertype', blank=True, null=True)
    phone = models.CharField(max_length=20)
    passportno = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Authentication_user'


class AuthenticationUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Authentication_user_groups'
        unique_together = (('user', 'group'),)


class AuthenticationUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Authentication_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthenticationUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Loans(models.Model):
    loanid = models.AutoField(primary_key=True)
    requestedby = models.ForeignKey(AuthenticationUser, models.DO_NOTHING, db_column='requestedby')
    requestedon = models.DateField()
    requestedat = models.TimeField()
    amountrequested = models.DecimalField(max_digits=28, decimal_places=2)
    amountdispatched = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    amountpaid = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    approved = models.BooleanField()
    remainingamount = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    approvedby = models.ForeignKey(AuthenticationUser, models.DO_NOTHING, db_column='approvedby', blank=True, null=True)
    paymentdate = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=500)
    payavenue = models.ForeignKey('Payavenue', models.DO_NOTHING, db_column='payavenue')
    denied = models.BooleanField(blank=True, null=True)
    deniedreason = models.CharField(max_length=500, blank=True, null=True)
    approvalcomments = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loans'


class Payavenue(models.Model):
    payavenueid = models.AutoField(primary_key=True)
    payavenuedescription = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'payavenue'


class Payments(models.Model):
    paymentid = models.AutoField(primary_key=True)
    processedby = models.ForeignKey(AuthenticationUser, models.DO_NOTHING, db_column='processedby')
    processedon = models.DateField()
    processedat = models.TimeField()
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


class Usertypes(models.Model):
    usertypeid = models.AutoField(primary_key=True)
    usertype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'usertypes'
