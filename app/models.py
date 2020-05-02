from django.db import models

# Create your models here.


class Province(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=10, verbose_name="省份")
    createTime = models.DateTimeField(auto_now=True, verbose_name="入库时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "省份管理"
        verbose_name_plural = "省份管理"


class Goods(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    provice = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name="产品产地")
    name = models.CharField(max_length=20, verbose_name="产品名字")
    createTime = models.DateTimeField(auto_now=True, verbose_name="入库时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "特色管理"
        verbose_name_plural = "特色管理"
