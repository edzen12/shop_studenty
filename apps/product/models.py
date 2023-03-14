from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(
        max_length=100, verbose_name="название категории", unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, 
        null=True, blank=True, related_name='children'
    )
    keywords = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    stat_third_block = models.CharField(max_length=10, choices=STATUS, default='False')
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])

    class MPTTMeta:
        order_insertion_by = ['name']

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="название producta")
    status = models.CharField(null=True,max_length=10, choices=STATUS, default='True')
    price = models.DecimalField(null=True,max_digits=8, decimal_places=2, default=0)
    amount= models.IntegerField(null=True,default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = RichTextField(null=True, blank=True)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.category.name}"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ['-created_at']


class Images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} | {self.product.name}"