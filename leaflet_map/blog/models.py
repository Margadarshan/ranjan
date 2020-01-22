from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import forms
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField



# Create your models here.
class Post(gis_models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	img=models.FileField(upload_to='gallery/',null=True,blank=True)
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	location=LocationField(based_fields=['pulchowk campus'],zoom=7,default=Point(27.6828417,85.3178166))
	class Meta:
		ordering=['-date_posted',]

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog-home')

# class LocationPost(forms.Form):
# 	# location=gis_models.PointField(srid=4326)
# 	location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
# 	# name=models.CharField(max_length=20)

# 	# def __str__(self):
# 	# 	return self.name


