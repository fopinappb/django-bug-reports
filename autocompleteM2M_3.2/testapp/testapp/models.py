from django.db import models


class Finding(models.Model):
    title = models.CharField(max_length=200)
    related_to = models.ManyToManyField('self', blank=True, help_text='Other findings related to this one')
