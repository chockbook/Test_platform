from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Web_test(models.Model):

    product = models.ForeignKey(Product,related_name="product_web_test",on_delete=models.CASCADE,null=True,verbose_name="所属项目")
    web_test_name = models.CharField("Web用例名称",max_length=64)
    web_test_desc = models.TextField("用例描述",default=" ")
    web_test_user = models.ForeignKey(User,verbose_name="测试人员",on_delete=models.CASCADE,max_length=64)
    web_test_url = models.CharField("页面地址",null=False,max_length=100)
    web_test_elem = models.TextField("定位语句",default=" ")
    elem_method = (("ID","ID"),
                   ("classname","classname"),
                   ("Xpath","xpath"),
                   ("css_seletor","css_seletor"))
    web_test_method = models.CharField("定位方式",choices=elem_method,default="ID",max_length=30,null=False)
    web_test_input = models.CharField("输入值",max_length=100,null=True)
    web_test_plural = models.CharField("单数或复数",choices=(("singular","singular"),("plural","plural")),default="singular",max_length=20)
    web_test_result  = models.TextField("预期测试结果",default=" ")
    web_test_result_finaly = models.TextField("最终测试结果",default=" ")
    Bug = (("null"," "),("是","是"),("否","否"))
    web_test_bug = models.CharField("是否有Bug",choices=Bug,default="null",max_length=4)
    create_time = models.DateTimeField("创建时间",auto_now=True)

    class Meta():
        verbose_name = "Web测试"
        verbose_name_plural = "Web测试"

    def __str__(self):
        return self.web_test_name
class Web_bug(Web_test):
    class Meta():
        verbose_name = "Web测试Bug"
        verbose_name_plural = "Web测试Bug"
        proxy = True







# Create your models here.
