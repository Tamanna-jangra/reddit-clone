from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SubReddits,Subscriptions,Posts,Comments,Votes
# Create your views here.

def HomePageView(request):
    return render(request,'home.html',{'boards':SubReddits.objects.all()})

def BoardView(request,id):
    return render(request, 'Board.html', {'posts': SubReddits.objects.get(id=id)})
