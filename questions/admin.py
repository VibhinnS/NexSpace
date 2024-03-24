from django.contrib import admin

# Register your models here.

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['title', 'content']
    
admin.site.register(Question)