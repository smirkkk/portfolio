from django.db import models

# Create your models here.
from django.utils import timezone


class AboutMe(models.Model):
    text = models.TextField(default=None, null=True, blank=True)
    img = models.ImageField(default=None, null=True, blank=True, upload_to='img/aboutme/')
    registed = models.DateTimeField(default=timezone.now)


class Career(models.Model):
    year = models.IntegerField(default=None, null=True, blank=True)
    month = models.IntegerField(default=None, null=True, blank=True)
    text = models.TextField(default=None, null=True, blank=True)
    registed = models.DateTimeField(default=timezone.now)


class Skills(models.Model):
    title = models.CharField(default=None, null=True, blank=True, max_length=100)
    point = models.IntegerField(default=None, null=True, blank=True)
    icon = models.CharField(default=None, null=True, blank=True, max_length=100)


class Repository(models.Model):
    title = models.CharField(default=None, null=True, blank=True, max_length=100)
    repository = models.URLField(default=None, null=True, blank=True)
    started = models.CharField(default=None, null=True, blank=True, max_length=7)
    finished = models.CharField(default=None, null=True, blank=True, max_length=7)
