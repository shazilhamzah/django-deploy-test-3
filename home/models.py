from django.db import models


class UserInformation(models.Model):
    username = models.CharField(max_length=50)
    level = models.IntegerField()
    progress = models.IntegerField()    