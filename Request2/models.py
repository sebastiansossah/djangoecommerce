
from django.db import models
from django.contrib.auth import get_user_model
from store.models import productModel
from django.db.models import F, Sum, FloatField

# Create your models here.
userF= get_user_model()



class requestCla(models.Model):
    userVar= models.ForeignKey(userF, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.RequestType_set.aggregate(
            total=Sum(F("price")*F("amount"), output_field= FloatField())
        )["total"] or FloatField(0)

    def __str__(self):
        return str(self.id)


    class Meta:
        db_table= 'request'
        verbose_name='request'
        verbose_name_plural='requests'
        ordering=['id']


class RequestType(models.Model):
    userVar= models.ForeignKey(userF, on_delete=models.CASCADE)
    producto= models.ForeignKey(productModel, on_delete=models.CASCADE)
    requestVar= models.ForeignKey(requestCla, on_delete=models.CASCADE)
    amount= models.IntegerField(default= 1)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'{str(self.amount)} de {str(self.producto)}'

    class Meta:
        db_table= 'Request type'
        verbose_name='request'
        verbose_name_plural='requests types'
        ordering=['id']



    
