from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
"""from django.http import HttpResponse
from django.utils import timezone
from .models import Post

def post_list(request):
    name = 'Django'
    return HttpResponse('''<h1>Hello Django</h1>
                        <p>{name}</p>'''.format(name=name))
"""
def post_list(request):
    return render(request,'blog/post_list.html')