from django.db import models
from django.conf import settings


# Create your models here.
class Monster(models.Model):
	name = models.CharField(max_length=64)
	strength = models.DecimalField()
	life = models.DecimalField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	

