from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class categories(models.Model):
    Name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.Name

class post(models.Model):
    tittle=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='blog', null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category= models.ManyToManyField(categories)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.tittle
