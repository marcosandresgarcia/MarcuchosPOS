from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

class BaseModel(models.Model):
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user = UserForeignKey(auto_user_add=True,related_name='+')
    update_user = UserForeignKey(auto_user_add=True,related_name='+')

    class Meta:
        abstract = True