from django.shortcuts import render
from .models import Result

# Create your views here.

def my_results(request):
    #checks if user is authenticated or not
    if request.user.is_authenticated:
        user = request.user
        results = Result.objects.all().filter(user=user)
    else:
        results = {}
    return render(request, 'results/results.html', {'results': results})
