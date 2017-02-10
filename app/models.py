"""
Definition of models.
"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.gdal import *
from django.contrib.gis.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class CitiesCity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    country_code = models.ForeignKey('CitiesCountry', db_column='code',blank=True, null=True)
    region_province = models.TextField(blank=True,null=True)
    population = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'cities_city'


class CitiesCountry(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(primary_key=True,unique=True, max_length=2)
    code3 = models.CharField(unique=True, max_length=3)
    population = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    currency_name = models.CharField(max_length=50, blank=True, null=True)
    language_codes = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20)
    tld = models.CharField(max_length=5)
    capital = models.CharField(max_length=100)
    continent = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'cities_country'






class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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



class Mothers(models.Model):
    id = models.BigIntegerField(primary_key = True,default=1)    
    maiden = models.TextField(blank=True, null=True)
    first = models.TextField(blank=True, null=True)
    middle = models.TextField(blank=True, null=True)
    city_of_birth = models.TextField(blank=True, null=True)
    country_of_birth = models.ForeignKey(CitiesCountry,blank=True, null=True)
    region_of_birth = models.TextField(blank=True,null=True)
    year_born = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.first +" "+ self.maiden

    class Meta:
        managed = True
        db_table = 'mothers'
        verbose_name = 'Mother'
        verbose_name_plural = 'Mothers'


class Fathers(models.Model):
    id = models.BigIntegerField(primary_key = True,default=1)    
    last = models.TextField(blank=True, null=True)
    first = models.TextField(blank=True, null=True)
    middle = models.TextField(blank=True, null=True)
    city_of_birth = models.TextField(blank=True, null=True)
    country_of_birth = models.ForeignKey(CitiesCountry,blank=True, null=True)
    region_of_birth = models.TextField(blank=True,null=True)
    year_born = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.first +" "+ self.last

    class Meta:
        managed = True
        db_table = 'fathers'
        verbose_name = 'Father'
        verbose_name_plural = 'Fathers'

class Person(models.Model):
    id = models.BigIntegerField(primary_key = True,default=1)
    family = models.TextField(blank=True, null=True)
    first = models.TextField(blank=True, null=True)
    middle = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    country = models.ForeignKey(CitiesCountry,related_name='curcountry',blank=True, null=True)
    region = models.TextField(blank=True,null=True)
    city = models.TextField(blank=True, null=True)
    city_of_birth = models.TextField(blank=True, null=True)
    country_of_birth = models.ForeignKey(CitiesCountry,related_name='country_of_birth',blank=True, null=True)
    region_of_birth = models.TextField(blank=True,null=True)
    birth_mother = models.ForeignKey(Mothers,blank=True, null=True,db_column='mothers')
    birth_father = models.ForeignKey(Fathers,blank=True, null=True,db_column='fathers')
    place_to_stay = models.NullBooleanField(blank=True,null=True)
    year_born = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.first +" "+ self.family

    class Meta:
        managed = True
        db_table = 'person'
        verbose_name = 'Person'
        verbose_name_plural = 'People'