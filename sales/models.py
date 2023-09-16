from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from bases.models import BaseModel
from inv.models import Product
from sales.constants import CLIENT_TYPE, NATURAL


class Clients(BaseModel):
    type = models.CharField(max_length=10, choices=CLIENT_TYPE, default=NATURAL)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    movil = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.name)

    def save(self):
        self.name = self.name.upper()
        self.last_name = self.last_name.upper()
        super(Clients, self).save()


class SalesHeader(BaseModel):
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    sub_total = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.discount
        super(SalesHeader, self).save()

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name = "Encabezado Factura"


class SalesDetail(BaseModel):
    header = models.ForeignKey(SalesHeader, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)
    price = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.product)

    def save(self):
        self.sub_total = float(float(int(self.amount)) * float(self.price))
        self.total = self.sub_total - float(self.discount)
        super(SalesDetail, self).save()

    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name = "Detalle Factura"


@receiver(post_save, sender=SalesDetail)
def detalle_fac_guardar(sender, instance, **kwargs):
    sale_id = instance.header.id

    enc = SalesHeader.objects.get(pk=sale_id)
    if enc:
        sub_total = SalesDetail.objects \
            .filter(header=sale_id) \
            .aggregate(sub_total=Sum('sub_total')) \
            .get('sub_total', 0.00)

        discount = SalesDetail.objects \
            .filter(header=sale_id) \
            .aggregate(discount=Sum('discount')) \
            .get('discount', 0.00)

        enc.sub_total = sub_total
        enc.discount = discount
        enc.save()
