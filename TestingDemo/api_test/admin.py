from django.contrib import admin
from api_test.models import Api_test
from django.shortcuts import render
from django.contrib import messages
from api_test.views import ApiTest

@admin.register(Api_test)
class Api_testAdmin(admin.ModelAdmin):
    list_display = ["api_test_name","product","api_test_user","api_test_bug","create_time"]


    actions = ['running']

    def running(self, request, queryset):
        
        if len(queryset) == 1:
            api_test_queryset = queryset[0]
            a = Api_test.objects.get(pk=api_test_queryset.id)
            #api_test_name = queryset[0].api_test_name
            #print(api_test_name)
            #调用接口测试
            result = ApiTest(request,api_test_queryset)
            a.api_test_result = result
            a.save()

            messages.add_message(request, messages.SUCCESS,result)

        else:
            messages.add_message(request, messages.ERROR, '现阶段只能支持运行一个用例')
            

    # 显示的文本，与django admin一致
    running.short_description = '  运行'
    # icon，参考element-ui icon与https://fontawesome.com
    running.icon = 'fas fa-play'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    running.type = 'success'

    # 给按钮追加自定义的颜色
    #running.style = 'color:black;'

# Register your models here.


