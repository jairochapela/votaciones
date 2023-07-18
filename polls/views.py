from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from polls.models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionView(View):
    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        return render(request, 'polls/question.html', {'question': question})