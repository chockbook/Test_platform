from django.contrib import admin
from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name']
    list_display = ['product_name','product_desc','producter','create_time'] 
    def ready(self):
        pass

# Register your models here.
