
from django.contrib.auth import get_user_model
from django.db import models


class TenantData(models.Model):
    name = models.CharField(max_length=123)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="tenant_objects")