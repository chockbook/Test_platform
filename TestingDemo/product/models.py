from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_name=models.CharField("项目名称",max_length=64)
    product_desc=models.TextField("项目描述",blank=True,default=" ")
    producter=models.ForeignKey(User,verbose_name="项目负责人",on_delete=models.CASCADE,max_length=64)
    create_time=models.DateTimeField("创建时间",auto_now=True)
    class Meta:
       
        verbose_name_plural="项目管理"
    def __str__(self):
        return self.product_name
# Create your models here.
