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
    path('<pk>/', exam_view, name='exam-view'),
    path('<pk>/data/', exam_data_view, name='exam-data-view'),
    path('<pk>/save/', save_exam_view, name='save-view')
]