from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Phone(models.Model):
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex],
        max_length=16,
        unique=True,
        help_text="Phone number must be entered in the format: '+999999999'.",
        error_messages={
            'unique': "This Phone has been used already",
        },
        ) # validators should be a list
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone
    

class Prayer(models.Model):
    name = models.CharField(max_length=250)
    prayer = models.TextField()
    
    def __str__(self):
        return self.name
    