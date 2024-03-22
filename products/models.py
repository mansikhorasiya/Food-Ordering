from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 , editable=False ,primary_key=True)
    product_name = models.CharField(max_lenght=50)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)
