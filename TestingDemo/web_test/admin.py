from django.contrib import admin
from .models import Web_test
from django.contrib import messages
from web_test.views import WebTest

@admin.register(Web_test)
class Web_testAdmin(admin.ModelAdmin):
    list_display = ["web_test_name","product","web_test_user","web_test_bug","create_time"]



    actions = ['running']
    def running(self, request, queryset):
        
        if len(queryset) == 1:
            web_test_queryset = queryset[0]
            a = Web_test.objects.get(pk=web_test_queryset.id)
            result = WebTest(request,web_test_queryset)

            a.web_test_result_finaly = result
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
