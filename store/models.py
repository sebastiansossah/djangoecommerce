from django.db import models

# Create your models here.

class productCategory(models.Model):
    categoryName= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='productCategory'
        verbose_name_plural='productCategories'

    def __str__(self):
        return self.categoryName

class productModel(models.Model):
    productName= models.CharField(max_length=50)
    image = models.ImageField(upload_to='Store')
    description = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE)
    available= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'product'
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.productName