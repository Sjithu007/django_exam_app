from django.shortcuts import render
from .models import Result

# Create your views here.

def my_results(request):
    user = request.user
    results = Result.objects.all().filter(user=user)
    return render(request, 'results/results.html', {'results': results})