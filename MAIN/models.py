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


class Brand(Page):
    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            self.parent = Page.objects.get(title='MARQUES')
        super(Brand, self).save(*args, **kwargs)

class Topic(Page):
    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            self.parent = Page.objects.get(title='RUBRIQUES')
        super(Topic, self).save(*args, **kwargs)

class Company(Page):
    topic = models.ManyToManyField('Topic',blank=True)
    brands = models.ManyToManyField('Brand',blank=True)
    adress = models.CharField(max_length=255, null=False,blank=False)
    zipCode = models.CharField(max_length=255, null=False,blank=False)
    area = models.CharField(max_length=255, null=False,blank=True)
    city = models.CharField(max_length=255, null=False,blank=False)
    country = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(null=False,blank=True)
    tel = models.CharField(max_length=20, null=False,blank=True)
    fax = models.CharField(max_length=20, null=False,blank=True)
    website = models.CharField(max_length=20, null=False,blank=True)
    highlight = models.BooleanField(default=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            self.parent = Page.objects.get(title='SOCIETES')
        # if not self.area:
            # if not self.country or self.country.lower() == "france":
                # deduce area from zipCode[:2]
        super(Company, self).save(*args, **kwargs)

class Person(Page):
    firstName = models.CharField(max_length=255,null=False,blank=True)
    companies = models.ManyToManyField(Company,through='Job')
    adress = models.CharField(max_length=255, null=False,blank=False)
    zipCode = models.CharField(max_length=255, null=False,blank=False)
    area = models.CharField(max_length=255, null=False,blank=True)
    city = models.CharField(max_length=255, null=False,blank=False)
    country = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(null=False,blank=True)
    tel = models.CharField(max_length=20, null=False,blank=True)
    highlight = models.BooleanField(default=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        print('*********************************')
        # print(str(self.title) + ' is BEING SAVED')
        print('*********************************')
        self.in_menus = []
        self.parent = Page.objects.get(title='MEMBRES')
        super(Person, self).save(*args,**kwargs)

class Job(models.Model):
    person = models.ForeignKey(Person)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=255,null=False,blank=True)
    since = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
    until = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
