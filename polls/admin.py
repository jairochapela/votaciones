from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    can_delete = True
    extra = 0
    fields = ['choice_text']

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    #inline fields for Choice
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
