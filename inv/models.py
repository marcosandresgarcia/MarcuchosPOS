from django.contrib.auth.models import User

from bases.models import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=100, help_text="Nombre", unique=True)
    creation_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_products', null=True)
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='updated_products', blank=True,
                                    null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Categorias"


class Product(BaseModel):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products_category")
    creation_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_categories', null=True)
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='updated_categories', blank=True,
                                    null=True)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        super(Product, self).save()

    class Meta:
        verbose_name_plural = "Productos"