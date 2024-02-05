from django.contrib import admin

# Register your models here.
from .models import Product , Brand , Review , ProductImages

class ProductImageInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','flag','price']
    list_filter = ['flag','price','quantity']
    search_fields = ['name','subtitle','description']
    inlines = [ProductImageInline]


class Reviewadmin(admin.ModelAdmin):
    list_display = ['user','product','rate','create_at']
    list_filter = ['rate','create_at']


admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review,Reviewadmin)

