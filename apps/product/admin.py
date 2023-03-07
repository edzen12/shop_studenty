from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from apps.product.models import Category, Product, Images

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title', 
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields = {'slug':('name',)}
)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    list_filter = ('product',)

class ImageAdminLine(admin.TabularInline):
    model = Images
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug':('name',)}
    inlines = [ImageAdminLine,]

admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImageAdmin)