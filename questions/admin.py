from django.contrib import admin
from django import forms
from .models import Question, Answer

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    max_num=4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline] 

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
