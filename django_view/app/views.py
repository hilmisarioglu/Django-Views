from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # print(request.GET.get('q'))
    # print(request.COOKIES)
    # print(request.path)
    # print(request.user)
    # print(request.method)
    
    # if request.method == 'GET':
    #     print('You are using GET method!')
   
    # if request.method == 'GET':
    #     print(f'You are using {request.method} method!')
    
    # print(request.META)
    
    context = {
       'title' : 'clarusway',
       'dict1' : {'title' : 'Hilmi'},
       'my_list': [2,3,4] 
    }
    return render(request, 'app/home.html', context)