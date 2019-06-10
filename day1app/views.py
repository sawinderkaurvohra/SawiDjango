from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Heloo whats up</h1>')
# Create your views here.
def home(request, id):
    if request.method == 'POST':
        context = {
            'name': request.POST['name']
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')
