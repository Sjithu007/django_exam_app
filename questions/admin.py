from django.contrib import admin
from django import forms
from .models import Question, Answer

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    max_num=4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline] 

'''
class FillInTheBlankAnswerInline(admin.TabularInline):
    model = FillInTheBlankAnswer
    max_num=1

class FillInTheBlankQuestionAdmin(admin.ModelAdmin):
    inlines = [FillInTheBlankAnswerInline] 
'''
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
'''
admin.site.register(FillInTheBlankQuestion, FillInTheBlankQuestionAdmin)
admin.site.register(FillInTheBlankAnswer)
'''