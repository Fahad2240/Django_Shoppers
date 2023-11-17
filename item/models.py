import imp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=255)
    class Meta:
        ordering=['name']
        verbose_name_plural='Categories'
    def __str__(self) -> str:
        return self.name
class Item(models.Model):
    # id=models.AutoField(primary_key=True)
    category=models.ForeignKey(category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()   
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='product_images',blank=True,null=True)
    created_by=models.ForeignKey(User,related_name='name',on_delete=models.CASCADE)
    is_sold=models.BooleanField(default='False')
    # pk=models.Primarykey(category,related_name='items',on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name