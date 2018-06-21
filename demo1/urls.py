"""
Definition of urls for python_webapp_django.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),

        django.contrib.auth.views.login,
        {
            'template_name': 'app/home.html',
            'authentication_form': app.form.myform,
            'extra_context':
            {
                'title': 'details',
                'year': datetime.now().year,
            }
        },
        name='myform'),
    url(r'^$', app.views.see, name='see')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
