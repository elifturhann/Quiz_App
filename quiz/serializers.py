#-- Oluşturulan tabloları listeleyebilmek görüntüleyebilmek ve API oluşturabilemek için serializers.py file oluşturduk
from rest_framework import serializers
from .models import Category, Questions, Quizzes, Answers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )
class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Quizzes
        fields = (
            'title',
            'date_created',
            'category',
            'category_id',

        )


class QuestionSerializer(serializers.ModelSerializer):
    quiz_id = serializers.IntegerField(write_only=True)
    quiz = serializers.StringRelatedField()


    class Meta:
        model = Questions
        fields = (
            'date_updated',
            'title',
            'difficulty',
            'date_created',
            'quiz',
            'quiz_id',
        )

class AnswerSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(write_only=True)
    question = serializers.StringRelatedField()
 
    class Meta:
        model = Answers
        fields = (
           '__all__'
        )



class StaffQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = (
            'title',
            'date_created',
            'category',
            'category_id',

        )