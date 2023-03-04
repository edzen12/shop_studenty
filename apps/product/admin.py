from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from apps.product.models import Category, Product

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

admin.site.register(Product, ProductAdmin)