from __future__ import unicode_literals # For python 2.x

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible    # for python 2.x
class Bookmark(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):      # python 2.x 에선 __unicode__(self)로 정의한다.
        return self.title





