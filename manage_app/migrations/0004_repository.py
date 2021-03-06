# Generated by Django 2.2.4 on 2019-08-16 04:15

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_app', '0003_delete_repository'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('text', markdownx.models.MarkdownxField(default=None)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('edited_date', models.DateTimeField(blank=True, null=True)),
                ('repository_url', models.URLField(blank=True, default=None, null=True)),
                ('started', models.CharField(blank=True, default=None, max_length=7, null=True)),
                ('finished', models.CharField(blank=True, default=None, max_length=7, null=True)),
                ('technique', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('role', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
