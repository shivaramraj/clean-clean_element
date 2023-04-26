from django.shortcuts import render
from django.http import *
# Create your views here.
from app.forms import *


def Topic(request):
    TO=TopicForm()
    d={'TO':TO}
    if request.method=='POST':
        TD=TopicForm(request.POST)
        if TD.is_valid():
            return HttpResponse('data is valid')
        else:
            return HttpResponse('data is in valid')


    return render(request,'topicform.html',d)