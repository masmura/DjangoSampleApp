from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
from datetime import datetime 


class Review(models.Model):
	text = models.TextField(max_length=200, validators=[MinLengthValidator(15)])
	sentiment = models.IntegerField(blank=True)
	date = models.DateTimeField('date published', default=datetime.now())

