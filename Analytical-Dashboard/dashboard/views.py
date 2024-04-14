"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib import admin
from typing import Self

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'dashboard/index.html', {'title':'Home Page', 'year' :datetime.now().year,})

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,'dashboard/contact.html', {'title':'Contact', 'message':'Your contact page.', 'year':datetime.now().year,})

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'dashboard/about.html', {'title':'About', 'message': 'Your application description page.','year': datetime.now().year, })
