from django.db import models


class Command(models.Model):
    name = models.CharField(max_length=100, default='name')
    detail = models.CharField(max_length=1000, default='details')
    command = models.CharField(max_length=100, default='whoami')

    class Meta:
        ordering = ('id', )