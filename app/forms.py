"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class demoform(myform):
    """Authentication form which uses boostrap CSS."""
    fname = form.CharField(max_length=254,
                               widget=form.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'fname'}))
lname = form.CharField(max_length=254,
                           widget=form.TextInput({
                               'class': 'form-control',
                               'placeholder': 'lname'}))
email = form.CharField(max_length=254,
                           widget=form.TextInput({
                               'class': 'form-control',
                               'placeholder': 'email'}))
    pno= form.CharField(max_length=254,
                               widget=form.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'pno'}))
    country = form.CharField(max_length=254,
                               widget=form.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'country'}))                                                               
city= form.CharField(max_length=254,
                           widget=form.TextInput({
                               'class': 'form-control',
                               'placeholder': 'city'}))
