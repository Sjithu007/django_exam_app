from django.urls import path
from .views import result_details_view

app_name = 'resultdetails'

urlpatterns = [
    path('<pk>/', result_details_view, name='result_details_view'),
]
