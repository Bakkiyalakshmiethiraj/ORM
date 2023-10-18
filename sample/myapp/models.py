from django.db import models
from django.contrib import admin
class  FootBall(models.Model):
    matches=models.IntegerField()
    goals=models.IntegerField()
    age=models.IntegerField()
    name=models.CharField(max_length=20)
    fastest_goal=models.IntegerField()

class FootBallAdmin(admin.ModelAdmin):
    list_display=('matches','goals','age','name','fastest_goal')