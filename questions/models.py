from django.db import models
from exams.models import Exam

# Create your models here.

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    #qno = models.PositiveIntegerField(primary_key=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

'''
class FillInTheBlankQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    #qno = models.PositiveIntegerField(primary_key=True)
    text = models.CharField(max_length=200)
    #answer = models.CharField(max_length=50)

    def __str__(self):
        return f"question: {self.text}"
    
    def get_fillintheblankanswers(self):
        return self.fillintheblankanswers_set.all()


class FillInTheBlankAnswer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.OneToOneField(FillInTheBlankQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.answer}"
'''