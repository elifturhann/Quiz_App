from django.contrib import admin
import nested_admin
from .models import Category, Questions, Quizzes, Answers


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answers
    # extra = 1
admin.site.register(Answers)
class QuestionInline(nested_admin.NestedTabularInline):
    model = Questions
    inlines = [AnswerInline]
    extra = 1

admin.site.register(Questions)

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quizzes
    inlines = [QuestionInline]
    list_display = ('title', 'category', 'date_created')
    list_filter = ('category',)
    search_fields = ('title',)
    ordering = ('title', )     

admin.site.register(Quizzes, QuizAdmin)

class CategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuizAdmin]

admin.site.register(Category)