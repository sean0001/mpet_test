from django.db import models
from django.contrib.auth.models import AbstractUser,Group


class myuser(AbstractUser):
    # 继承AbstractUser，该Model和默认User的字段方法一样，只需要添加自己需要的字段即可
    test = models.CharField(max_length=40)  # 自定义的字段
    job = models.CharField(max_length=40)
    age = models.IntegerField(default=1)
    class meta:
        db_table ="auth_user"



class Book(models.Model):
    name = models.CharField(max_length=100)
    describe  = models.CharField(max_length=100)
    sort_no = models.IntegerField(default= 0)



# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=50,null=True)
    #book = models.ForeignKey()
    address = models.CharField(max_length=40,null=True)
    tel = models.CharField(max_length=40,null=True)
    mobile = models.CharField(max_length=200,default="default@qq.com")
    birth_date = models.DateField(blank=True, null=True)
