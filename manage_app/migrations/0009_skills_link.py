# Generated by Django 2.2.4 on 2019-08-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_app', '0008_repository_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='link',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
