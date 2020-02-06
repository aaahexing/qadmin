from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'level']


# Register your models here.
admin.site.register(Question, QuestionAdmin)