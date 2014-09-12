# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
import csv
import os
fp = os.path.join(request.folder,'private','test.csv')
data1 = []
data2 = []

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to Sleep Pattern Annotator!")
    return dict(form=auth.login())

def login():
 
     return dict(form=auth.login())
    
def selection():
     return dict()
    
    


def profile():

    with open(fp, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
                data1.append(float((row[0])))
                data2.append(float((row[1])))


    print data1
    return dict(data1=data1[1500:3000])

def profile():

    with open(fp, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
                data1.append(float((row[0])))
                data2.append(float((row[1])))


    print data1
    return dict(data1=data1[2000:3000])

def profile():

    with open(fp, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
                data1.append(float((row[0])))
                data2.append(float((row[1])))


    print data1
    return dict(data1=data1[3500:5000])
