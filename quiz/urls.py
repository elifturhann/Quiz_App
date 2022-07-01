from django.urls import path
from .views import QuestionView, QuizView, CategoryView, AnswerView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('<str:category>/<str:title>', QuizView.as_view()),
    path('question/', QuestionView.as_view()),
    path('answer/', AnswerView.as_view()),
]