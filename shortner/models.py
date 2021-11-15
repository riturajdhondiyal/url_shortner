from django.db import models

# Create your models here.
# DB named Url has two tables: link and uuid
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
