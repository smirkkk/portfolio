from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


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
    link = models.URLField(default=None, null=True, blank=True)
    icon = models.CharField(default=None, null=True, blank=True, max_length=100)


class Repository(models.Model):
    type = models.CharField(blank=True, null=True, default=None, max_length=10)
    title = models.CharField(blank=True, null=True, max_length=50)
    text = MarkdownxField(default=None)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    edited_date = models.DateTimeField(blank=True, null=True)
    repository_url = models.URLField(default=None, null=True, blank=True)
    period = models.CharField(default=None, null=True, blank=True, max_length=50)
    technique = models.TextField(default=None, null=True, blank=True)
    role = models.TextField(default=None, null=True, blank=True)

    img1 = models.ImageField(default=None, null=True, blank=True, upload_to='img/repository/%Y/%m/%d')
    img2 = models.ImageField(default=None, null=True, blank=True, upload_to='img/repository/%Y/%m/%d')
    img3 = models.ImageField(default=None, null=True, blank=True, upload_to='img/repository/%Y/%m/%d')
    img4 = models.ImageField(default=None, null=True, blank=True, upload_to='img/repository/%Y/%m/%d')
    img5 = models.ImageField(default=None, null=True, blank=True, upload_to='img/repository/%Y/%m/%d')

    def formatted_markdown(self):
        return markdownify(self.text)
