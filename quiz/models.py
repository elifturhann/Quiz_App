from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    title = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

class Questions(models.Model):
    Difficulty = (
        ('H', 'hard'),
        ('M', 'medium'),
        ('E', 'easy'),
    )
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    difficulty = models.CharField(choices=Difficulty, max_length=2)
    date_created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title

class Answers(models.Model):
    date_updated = models.DateTimeField(auto_now=True)
    answer_text = models.CharField(max_length=50)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, related_name='answer', on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.answer_text

