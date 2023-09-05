from django.contrib import admin

# Register your models here.
 # admin.site.register(models.taskModel)
from django.contrib import admin
from . import models 

# Register your models here.
@admin.register(models.taskModel)
class taskModelAdmin(admin.ModelAdmin):
    list_display = ('taskNo', 'taskTitle', 'taskDescription', 'is_completed')