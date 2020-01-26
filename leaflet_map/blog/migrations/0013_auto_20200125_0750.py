# Generated by Django 3.0.2 on 2020-01-25 07:50

import django.contrib.gis.geos.point
from django.db import migrations
import location_field.models.spatial


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(85.3178166, 27.6828417), srid=4326),
        ),
    ]
