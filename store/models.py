from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=10)
    is_available = models.BooleanField(default=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=4.50)
    is_new = models.BooleanField(default=False)
    is_on_deal = models.BooleanField(default=False)
    is_clearance = models.BooleanField(default=False)

    def get_url(self):
        return reverse('store:product_detail', args=[self.category.id, self.id])

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    # THE FIX: This line is required for the admin inline to work.
    # It defines the essential link between a size and its parent product.
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='sizes', null=True, blank=True)
    size = models.CharField(max_length=10)
    def __str__(self):
        return self.size

class ProductGallery(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='gallery_images', null=True, blank=True)
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'