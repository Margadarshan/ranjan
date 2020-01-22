from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class DestinationModel(models.Model):
	source= models.CharField(max_length=20)
	destination = models.CharField(max_length=20)

	def __str__(self):
		return self.destination 

 