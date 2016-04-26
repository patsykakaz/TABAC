#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import *
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.models import upload_to

# bobby du mois
# société du mois

# class Marque():

class Topic(Page):
    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Topic, self).save(*args, **kwargs)

class Company(Page):
    topic = models.ManyToManyField('Topic')
    adress = models.CharField(max_length=255, null=False,blank=False)
    zipCode = models.CharField(max_length=255, null=False,blank=False)
    area = models.CharField(max_length=255, null=False,blank=True)
    city = models.CharField(max_length=255, null=False,blank=False)
    country = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(null=False,blank=True)
    tel = models.CharField(max_length=20, null=False,blank=True)

    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Company, self).save(*args, **kwargs)

class Person(Page):
    # BOBBY DU MOIS
    companies = models.ManyToManyField(Company,through='Job')
    email = models.EmailField(null=False,blank=True)
    tel = models.CharField(max_length=20, null=False,blank=True)
    # adresse (full + département)

    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Person, self).save(*args, **kwargs)

class Job(models.Model):
    person = models.ForeignKey(Person)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=255,null=False,blank=True)
    since = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
    until = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
