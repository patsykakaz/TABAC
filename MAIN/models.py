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

# !! PRODUIT !!


class Product(Page):
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Product.illustration", "product"),
        format="Image", max_length=255, null=True, blank=True)

    def __unicode__(self):
        if self.parent and self.parent.title != 'PRODUITS':
            return '%s (%s)' % (self.title.upper(), self.parent.title)
        else:
            return '%s' % (self.title.upper())

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            self.parent = Page.objects.get(title='PRODUITS')
        super(Product, self).save(*args, **kwargs)

class Brand(Page):
    products = models.ManyToManyField('Product',blank=True)
    topics = models.ManyToManyField('Topic',blank=True)
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Brand.illustration", "brand"),
        format="Image", max_length=255, null=True, blank=True)
    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            self.parent = Page.objects.get(title='MARQUES')
        super(Brand, self).save(*args, **kwargs)

class Topic(Page):
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Topic.illustration", "topic"),
        format="Image", max_length=255, null=True, blank=True)
    def __unicode__(self):
        if self.parent and self.parent.title != 'RUBRIQUES':
            return '%s (%s)' % (self.title.upper(), self.parent.title)
        else:
            return '%s' % (self.title.upper())

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            self.parent = Page.objects.get(title='RUBRIQUES')
        super(Topic, self).save(*args, **kwargs)

class Company(Page):
    subsidiaries = models.ManyToManyField('Company')
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Company.illustration", "company"),
        format="Image", max_length=255, null=True, blank=True)
    topics = models.ManyToManyField('Topic',blank=True)
    brands = models.ManyToManyField('Brand',blank=True)
    adress = models.CharField(max_length=255, null=False,blank=True)
    zipCode = models.CharField(max_length=255, null=False,blank=True)
    area = models.CharField(max_length=255, null=False,blank=True)
    city = models.CharField(max_length=255, null=False,blank=True)
    country = models.CharField(max_length=255,null=False,blank=True)
    email = models.EmailField(null=False,blank=True)
    tel = models.CharField(max_length=20, null=False,blank=True)
    fax = models.CharField(max_length=20, null=False,blank=True)
    website = models.CharField(max_length=20, null=False,blank=True)
    highlight = models.BooleanField(default=False,null=False,blank=True)

    def __unicode__(self):
        return '%s' % (self.title)

    def save(self, *args, **kwargs):
        self.in_menus = []
        if not self.parent:
            self.parent = Page.objects.get(title='SOCIETES')
        # if not self.area:
            # if not self.country or self.country.lower() == "france":
                # deduce area from zipCode[:2]
        super(Company, self).save(*args, **kwargs)

class Person(Page):
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Person.illustration", "person"),
        format="Image", max_length=255, null=True, blank=True)
    firstName = models.CharField(max_length=255,null=False,blank=True)
    companies = models.ManyToManyField(Company,through='Job')
    adress = models.CharField(max_length=255, null=False,blank=True)
    zipCode = models.CharField(max_length=255, null=False,blank=True)
    area = models.CharField(max_length=255, null=False,blank=True)
    city = models.CharField(max_length=255, null=False,blank=True)
    country = models.CharField(max_length=255,null=False,blank=True)
    email = models.EmailField(null=False,blank=True)
    tel = models.CharField(max_length=20, null=False,blank=True)
    highlight = models.BooleanField(default=False,null=False,blank=True)

    def __unicode__(self):
        return '%s %s' % (self.title.upper(), self.firstName.lower())

    def save(self, *args, **kwargs):
        self.in_menus = []
        self.parent = Page.objects.get(title='MEMBRES')
        super(Person, self).save(*args,**kwargs)

class Job(models.Model):
    person = models.ForeignKey(Person)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=255,null=False,blank=True)
    since = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
    until = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
