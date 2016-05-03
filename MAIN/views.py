#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.contrib.auth import logout, login, authenticate, get_backends
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required

from mezzanine.utils.urls import login_redirect, next_url
from mezzanine.pages.models import Page
from .models import *

import xml.etree.ElementTree as ET


tree = ET.parse('liste.xml')
root = tree.getroot()

def importXML(request,start,end):
    i1 = int(start)
    while i1 < int(end):
        row = root[0][0][i1]

        company = False
        person = False
        jobX = False
        rubrique = False
        subRubrique = False
        i2 = 0
        adress = False
        adress2 = False
        adress3 = False
        city = False
        country = False
        tel = False
        fax = False
        email = False
        website = False
        job = False
        person1 = False
        person2 = False
        person_tel = False

        for cell in row:
            if cell.attrib:
                for key,value in cell.attrib.items():
                    if 'Index' in key:
                        i2 = int(value) -1
            if i2 == 1: 
                rubrique = cell[0].text
            if i2 == 2:
                subRubrique = cell[0].text
            if i2 == 4:
                company = cell[0].text
            if i2 == 5:
                adress = cell[0].text
            if i2 == 6:
                adress2 = cell[0].text
            if i2 == 7:
                adress3 = cell[0].text
            if i2 == 8:
                zipcode = cell[0].text
            if i2 == 9:
                city = cell[0].text
            if i2 == 10:
                country = cell[0].text
            if i2 == 11:
                tel = cell[0].text
            if i2 == 12:
                fax = cell[0].text
            if i2 == 13:
                email = cell[0].text
            if i2 == 14:
                website = cell[0].text
            if i2 == 15:
                job = cell[0].text
            if i2 == 16:
                person1 = cell[0].text
            if i2 == 17:
                person2 = cell[0].text
            if i2 == 18:
                person_tel = cell[0].text
            i2 +=1
        try:
            company = Company.objects.get(title=company)
        except:
            company = Company(title=company)
        if adress: 
            company.adress = adress
        if adress2:
            company.adress = company.adress + ' '+ adress2
        if adress3:
            company.adress = company.adress + ' '+ adress3
        if city:
            company.city = city
        if country:
            company.country = country
        if tel:
            company.tel = tel
        if fax:
            company.fax = fax
        if email:
            company.email = email
        if website:
            company.website = website
        company.save()
        if rubrique:
            try:
                topic = Topic.objects.get(title=rubrique)
            except:
                topic = Topic(title=rubrique)
                topic.save()
            company.topic.add(topic)
        if subRubrique:
            try:
                topic = Topic.objects.get(title=subRubrique)
            except:
                topic = Topic(title=subRubrique)
                if rubrique:
                    print "fetch parent"
                    try:
                        parent = Topic.objects.get(title=rubrique)
                        topic.parent = parent
                        print 'parent = %s' % parent
                    except:
                        pass
                topic.save()
            company.topic.add(topic)
        if person1:
            try: 
                person = Person.objects.get(title=person1)
                print person
            except:
                person = Person(title=person1)
                if person2:
                    person.firstName = person2
                if person_tel:
                    person.tel = person_tel
                person.save()
        if job and person:
            try:
                jobX = Job.objects.get(title=job,person=person,company=company)
            except:
                jobX = Job(person=person,company=company,title=job)
                jobX.save()
        # Final Save()
        company.save()

        i1 +=1
    return HttpResponse("IMPORT XML process ended.")