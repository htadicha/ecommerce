from django.contrib import admin
from .models import Category, Product, ProductSize, ProductGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'is_available')
    inlines = [ProductSizeInline, ProductGalleryInline]

    # --- THIS IS THE FIX ---
    # This override method ensures that the inline formsets (for images and sizes)
    # correctly handle saving new objects, which resolves the 'new_objects' error.
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)