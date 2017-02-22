from copy import deepcopy

from django.contrib import admin
from django.db.models import ImageField

from mezzanine.core.admin import (DisplayableAdmin, TabularDynamicInlineAdmin)
from mezzanine.pages.admin import PageAdmin

from .forms import ImageWidget
from .models import (Product, ProductImage, Variation)



class ProductImageInline(TabularDynamicInlineAdmin):
    model = ProductImage
    formfield_overrides = {ImageField: {"widget": ImageWidget}}

class VariationInline(TabularDynamicInlineAdmin):
    model = Variation

product_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
product_fieldsets[0][1]['fields'].insert(2, 'available')
product_fieldsets[0][1]['fields'].extend(['content',])
product_fieldsets = list(product_fieldsets)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['admin_thumb', 'title', 'price', 'available', 'status', 'admin_link']
    list_display_links = ('admin_thumb', 'title')
    list_filter = ['available', 'status', 'publish_date', 'expiry_date']
    list_editable = ['available', 'status']
    inlines = [ProductImageInline, VariationInline]
    fieldsets = product_fieldsets
