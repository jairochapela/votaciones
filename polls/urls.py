from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    #path('polls/', views.index, name='index'),
    path('<int:question_id>', views.QuestionView.as_view(), name='question'),
    path('<int:question_id>/results', views.results, name='results'),
]

