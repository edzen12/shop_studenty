from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        max_length=100, verbose_name="название категории", unique=True
    )
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, 
        null=True, blank=True, related_name='children'
    )

    def __str__(self) -> str:
        return f"{self.name}"
    
    class MPTTMeta:
        order_insertion_by = ['name']

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="название producta")

    def __str__(self) -> str:
        return f"{self.name} | {self.category.name}"