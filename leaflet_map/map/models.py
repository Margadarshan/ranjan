from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class DestinationModel(models.Model):
	source= models.CharField(max_length=40)
	destination = models.CharField(max_length=40)

	def __str__(self):
		return self.destination 

 