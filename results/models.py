from django.db import models
from exams.models import Exam
from django.contrib.auth.models import User

# Create your models here.
RESULT_STATUS = [
    ('Pass', 'Pass'),
    ('Fail', 'Fail'),
]

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField()
    percentage = models.FloatField()
    result_status = models.CharField(max_length=10, choices=RESULT_STATUS)

    def __str__(self):
        return f"exam: {self.exam}, user: {self.user}"
