from django.contrib import admin
from django.utils.html import format_html
from .models import Producto, ProductImage, ProducTag


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'active', 'description',)
    list_filter = ('active', 'date_update',)
    search_fields = ('name', )


admin.site.register(Producto, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProducTag)