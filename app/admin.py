from django.contrib import admin
from app.models import *
from django.contrib.auth.models import User,Group
# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id", "provice", "name", "createTime")
    list_filter = ("provice",)
    search_fields = ("name", )

admin.site.register(Province)
admin.site.register(Goods,GoodsAdmin)

admin.site.site_header = "超级管理员后台"
admin.site.site_title = "超级管理员后台"
admin.site.unregister(User)
admin.site.unregister(Group)