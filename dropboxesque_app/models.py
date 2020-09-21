from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class DropboxesqueModel(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
