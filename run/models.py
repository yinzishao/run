# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cal(models.Model):
    cal_id = models.AutoField(primary_key=True)
    cal_year_and_month = models.DateField(blank=True, null=True)
    cal_day = models.DateField(blank=True, null=True)
    cal_value = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cal'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

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


class Locations(models.Model):
    locations_id = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    zone = models.CharField(max_length=45, blank=True, null=True)
    running_result = models.ForeignKey('RunningResult', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class RunningResult(models.Model):
    running_result_id = models.AutoField(primary_key=True)
    running_result_distance = models.CharField(max_length=45, blank=True, null=True)
    running_result_duration = models.TimeField(blank=True, null=True)
    running_result_starttime = models.DateTimeField(blank=True, null=True)
    running_result_endtime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'running_result'
    def __str__(self):
        return str(self.running_result_id)
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
        # return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields] if attr in ["running_result_distance","running_result_duration"]]))

class UserInformation(models.Model):
    user_information_id = models.AutoField(primary_key=True)
    user_avatar = models.CharField(max_length=45, blank=True, null=True)
    user_height = models.CharField(max_length=10, blank=True, null=True)
    user_weight = models.CharField(max_length=10, blank=True, null=True)
    user_sex = models.CharField(max_length=1, blank=True, null=True)
    user_birth = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_information'
