from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Ubications(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    latitud = models.DecimalField(max_digits=1000, decimal_places=16, verbose_name="Latitud")
    altitud = models.DecimalField(max_digits=1000, decimal_places=16, verbose_name="Altitud")
    img = CloudinaryField("image", default="")
    description = models.TextField(verbose_name="Descripción", default="")
    tramites = models.TextField(verbose_name="Tramites", default="")
    documentacion = models.TextField(verbose_name="Documentacion", default="")

    def __str__(self):
        return self.name