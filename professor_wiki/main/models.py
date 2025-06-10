from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

class Wiki(models.Model):
    image = models.ImageField(width_field=75, height_field=100, blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    office = models.CharField(max_length=100)
    college = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    contents = summer_fields.SummernoteTextField(default='')


# Create your models here.
