from django.contrib import admin
from .models import Category, Questions, Quizzes, Answers


admin.site.register(Category)
admin.site.register(Questions)
admin.site.register(Quizzes)
admin.site.register(Answers)
