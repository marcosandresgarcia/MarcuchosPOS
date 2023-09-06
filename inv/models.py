from bases.models import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=100, help_text="Nombre", unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Categorias"