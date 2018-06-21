"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class modelset:
     class demom(models.Model):
         """demom description)"""


         class demoform:
             fname=models.CharField();
      lname=models.CharField();
       email=models.CharField();
        pno=models.numbers();
         country=models.CharField();
          city=models.CharField();
         def __unicode__(self):
             return udemom"
