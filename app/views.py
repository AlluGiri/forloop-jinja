from django.shortcuts import render

# Create your views here.
def sweety(request):
    d={'name':'Tendulkar'}
    return render(request,'forloop.html',d)
