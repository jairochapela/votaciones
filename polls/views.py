from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from polls.forms import QuestionForm

from polls.models import Question, Vote


def index(request):
    return render(request, 'polls/index.html', {'items': Question.objects.all()})


class QuestionView(LoginRequiredMixin, View):
    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        form = QuestionForm(question)
        return render(request, 'polls/question.html', {'question': question, 'form': form})
    
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
            return HttpResponse('Gracias por votar')
        return render(request, 'polls/question.html', {'question': question, 'form': form})