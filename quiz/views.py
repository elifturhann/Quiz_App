from django.shortcuts import render
from rest_framework import generics
from .models import Category, Questions, Quizzes, Answers
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from .permission import IsStafforReadOnly

#*ListAPIView
#? Used for read-only endpoints to represent a collection of model instances.
#? Provides a get method handler.


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsStafforReadOnly, )


class QuizView(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsStafforReadOnly, ) 

    def get_queryset(self):
        category = self.kwargs['category']
        return Quizzes.objects.filter(category__name__iexact=category)


class QuestionView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsStafforReadOnly, )   

class AnswerView(generics.ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsStafforReadOnly, )        

