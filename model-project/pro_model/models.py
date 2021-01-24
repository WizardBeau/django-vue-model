from django.db import models

# Create your models here.

class Test(models.Model):
    user = models.CharField('用户名', max_length=50, primary_key=True)
    password = models.CharField('密码', max_length=50, blank=False)
    name = models.CharField('昵称', max_length=50)
