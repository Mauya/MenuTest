# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def welcome_all(request):
    return render(request, "sitepage/home.html",
                  {"a_variable": "I've been rendered in the child template",
                   "another_variable": "Me too!"})

def about_me(request):
    return render(request, "sitepage/about.html",
                  {"a_variable": "I've been rendered in the child template",
                   "another_variable": "Me too!"})

def my_contact(request):
    return render(request, "sitepage/contact.html",
                  {"a_variable": "I've been rendered in the child template",
                   "another_variable": "Me too!"})
