from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db import transaction
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from polls.forms import QuestionForm

from polls.models import Choice, Question, Vote


def index(request):
    return render(request, 'polls/index.html', {'items': Question.objects.all()})


class QuestionView(LoginRequiredMixin, View):
    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        vote = Vote.objects.filter(question=question, user=request.user).first()
        form = QuestionForm(question)
        return render(request, 'polls/question.html', {'question': question, 'form': form, 'voted': vote is not None})
    
    def post(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        form = QuestionForm(question, request.POST)
        if form.is_valid():
            #form.save()
            with transaction.atomic():
                choice = form.cleaned_data['choice']
                choice.votes += 1
                choice.save()
                vote = Vote(question=question, user=request.user)
                vote.save()
            return render(request, 'polls/question.html', {'question': question, 'form': form, 'voted': True})
        return render(request, 'polls/question.html', {'question': question, 'form': form})
    
def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    choices = Choice.objects.filter(question=question).all()
    return render(request, 'polls/results.html', {'question': question, 'choices': list({'choice_text':c.choice_text, 'votes':c.votes, 'id':c.id} for c in choices)})