from django.contrib.auth.models import User
from django.db import models

from bases.models import BaseModel
from sales.constants import CLIENT_TYPE, NATURAL


class Clients(BaseModel):
    type = models.CharField(max_length=10, choices=CLIENT_TYPE, default=NATURAL)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    movil = models.CharField(max_length=20, null=True, blank=True)
    creation_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_clients', null=True)
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='updated_clients', blank=True,
                                    null=True)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.name)

    def save(self):
        self.name = self.name.upper()
        self.last_name = self.last_name.upper()
        super(Clients, self).save()
