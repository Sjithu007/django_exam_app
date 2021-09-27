from django.shortcuts import render
from results.models import Result

# Create your views here.

def result_details_view(request, pk):
    user = request.user
    result = Result.objects.get(pk=pk)
    response = eval(result.results)
    return render(request, 'resultdetails/resultdetails.html', {'result': result, 'response': response })