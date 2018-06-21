"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    def demoview(request):

    if request.method == 'POST':

        form = myform(request.POST)

        if form.is_valid():

            fname= request.POST.get('fname','')
lname= request.POST.get('lname','')
email= request.POST.get('email','')
pno= request.POST.get('pno','')
country= request.POST.get('country','')
city= request.POST.get('city','')


            form.save()

            return HttpResponse("home.html")

    else:

        form = myform()

    return render(request,'app/home.html',{'form':form,})
