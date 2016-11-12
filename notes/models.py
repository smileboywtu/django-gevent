from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NotesType(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField()


class Notes(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    type = models.ForeignKey(NotesType, db_column='noteType', on_delete=models.CASCADE)
