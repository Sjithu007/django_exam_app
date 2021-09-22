from django.urls import path
from .views import my_results

urlpatterns = [
    path('results/', my_results, name='results'),
]
