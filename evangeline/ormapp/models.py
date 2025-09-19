
from django.db import models
from django.contrib import admin
class car(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    price=models.IntegerField()
    year=models.IntegerField()
    horsepower=models.FloatField()

class carAdmin(admin.ModelAdmin):
    list_display=('cid','cname','price','year','horsepower')


