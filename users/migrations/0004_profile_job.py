# Generated by Django 4.1.1 on 2022-10-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
