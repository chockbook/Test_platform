from django.contrib import admin
from api_test.models import Api_bug
from web_test.models import Web_bug


@admin.register(Api_bug)
class ApiBugAdmin(admin.ModelAdmin):
    list_display = ["api_test_name","api_test_user",'api_test_bug']


    def get_queryset(self,request):
        
        qs = super(ApiBugAdmin, self).get_queryset(request)
        qs = qs.filter(api_test_bug="是")
        return qs

@admin.register(Web_bug)
class WebBugAdmin(admin.ModelAdmin):
    list_display = ['web_test_name','web_test_user','web_test_bug']

    def get_queryset(self,request):

        qs = super(WebBugAdmin,self).get_queryset(request)
        qs = qs.filter(web_test_bug="是")
        return qs



# Register your models here.
