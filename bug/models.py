from django.db import models
from taggit.managers import TaggableManager

class Bug(models.Model):

    tags = TaggableManager()
