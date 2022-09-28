from django.db import models


#my model
class Feature(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    date=models.IntegerField(default=1)
    month=models.IntegerField(default=1)
    year=models.IntegerField(default=1)