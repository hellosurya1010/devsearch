# Generated by Django 4.1.1 on 2022-09-30 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('short_intro', models.CharField(blank=True, max_length=254, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/profile.png', null=True, upload_to='profiles')),
                ('social_linkedin', models.CharField(blank=True, max_length=256, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=256, null=True)),
                ('social_github', models.CharField(blank=True, max_length=256, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
