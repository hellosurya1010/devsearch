# Generated by Django 4.1.1 on 2022-10-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
