# Generated by Django 2.2.4 on 2019-08-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_app', '0009_skills_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]