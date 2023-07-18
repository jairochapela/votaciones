

from django import forms

from polls.models import Question


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.question = question
        self.fields['choice'] = forms.ModelChoiceField(required=True, widget=forms.RadioSelect, queryset=self.question.choice_set.all())