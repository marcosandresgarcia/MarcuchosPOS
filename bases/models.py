from django.contrib.auth.models import User
from django.db import models

class BaseModel(models.Model):
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_items')
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='updated_items', blank=True, null= True)

    class Meta:
        abstract = True