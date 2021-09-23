from django.urls import path
from .views import (
    ExamListView,
    exam_view,
    exam_data_view,
    save_exam_view
)

app_name = 'exams'

urlpatterns = [
    path('', ExamListView.as_view(), name='main-view'),
    path('exam/<exam_id>/', exam_view, name='exam-view'),
    path('exam/<exam_id>/data/', exam_data_view, name='exam-data-view'),
    path('exam/<exam_id>/save/', save_exam_view, name='save-view')
]