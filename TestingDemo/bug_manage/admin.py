from django.contrib import admin
from api_test.models import Api_test
from web_test.models import Web_test


class BugAdmin(admin.ModelAdmin):
    list_display = ["bug_api_test","bug_web_test"]

    
    api_test_select = """
                        select * from 'Api_test' where 'Api_test'.'api_test_bug' = '是'
                        """
    web_test_select = """
                        select * from 'Web_test' where 'Web_test'.'web_test_bug' = '是'
                        """

    def queryset(self, request):
        qs = super(BugAdmin, self).queryset(request)
        qs = qs.extra(select={'bug_api_test': api_test_select,
                              'bug_web_test': web_test_select})
        return qs

# Register your models here.
