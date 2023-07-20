from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    can_delete = True
    extra = 0
    fields = ['choice_text']

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'available_from', 'available_until']
    widgets = {
        'available_from': admin.widgets.AdminSplitDateTime,
        'available_until': admin.widgets.AdminSplitDateTime,
    }
    #inline fields for Choice
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
