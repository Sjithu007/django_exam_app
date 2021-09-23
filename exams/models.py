from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Exam(models.Model):
    exam_id = models.CharField(primary_key=True, max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    exam_name = models.CharField(max_length=120)
    semester = models.PositiveIntegerField()
    date_and_time = models.DateTimeField()
    duration = models.PositiveIntegerField(help_text="Exam Duration in Minutes")
    total_questions = models.PositiveIntegerField(help_text="Total Number of Questions in Exam")
    total_assigned_marks = models.PositiveIntegerField(help_text="Total Assigned Marks")
    pass_mark = models.PositiveIntegerField(help_text="Required Score to Pass Exam")

    def __str__(self):
        return f"{self.exam_name}"

    def get_questions(self):
        return self.question_set.all()[:self.total_questions]

    class Meta:
        verbose_name_plural = 'Exams'
