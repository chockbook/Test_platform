from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Api_test(models.Model):
    product = models.ForeignKey(Product,related_name="product_api_test",on_delete=models.CASCADE,null=True,verbose_name="所属项目")
    api_test_name = models.CharField("接口名称",max_length=64)
    api_test_desc = models.TextField("接口描述",blank=True,default=" ")
    api_test_user = models.ForeignKey(User,verbose_name="测试人员",on_delete=models.CASCADE,max_length=64)
    api_test_url = models.CharField("url地址",null=False,max_length=100)
    api_test_value = models.TextField("请求参数",null=False,default="{ }")
    header = models.TextField(null=False,verbose_name="请求头",default="{ }")
    REQUEST_METHOD=(("get","get"),
                    ("post","post"))
    api_test_method = models.CharField("请求方法",choices=REQUEST_METHOD,default="get",max_length=16,null=True)
    api_test_result = models.TextField("测试结果",blank=True,default=" ")
    Bug = (("null"," "),("是","是"),("否","否"))
    api_test_bug = models.CharField("是否有Bug",choices=Bug,default="null",max_length=4)
    create_time = models.DateTimeField("创建时间",auto_now=True)

    class Meta():
        verbose_name = "接口测试"
        verbose_name_plural = "接口测试"

    def __str__(self):
        return self.api_test_name




# Create your models here.
