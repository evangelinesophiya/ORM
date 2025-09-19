# Ex02 Django ORM Web Application
## Date: 19-09-2025

## AIM
To develop a Django application to store and retrieve data from a cars Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py


from django.contrib import admin
from .models import car,carAdmin
admin.site.register(car,carAdmin)


models.py

from django.db import models
from django.contrib import admin
class car(models.Model):
    mid=models.IntegerField()
    mname=models.CharField(max_length=100)
    price=models.IntegerField()
    year=models.IntegerField()
    horsepower=models.FloatField()

class carAdmin(admin.ModelAdmin):
    list_display=('cid','cname','price','year','horsepower')


~~~

## OUTPUT
![alt text](<Screenshot (35).png>)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
