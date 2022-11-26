from django.db import models
from django.conf import settings
# Create your models here.
class Lance(models.Model):
  jogador = models.ForeignKey(
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE 
    )
  valor = models.FloatField()
  


