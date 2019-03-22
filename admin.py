from django.contrib import admin
from .models import Category, Product,BGImagesModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

    

admin.site.register(Product, ProductAdmin)



class BGImagesAdmin(admin.ModelAdmin):
    list_display = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6'] 

admin.site.register(BGImagesModel, BGImagesAdmin)