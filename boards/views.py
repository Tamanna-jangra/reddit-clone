from django.shortcuts import render,redirect,get_object_or_404
from .models import SubReddits,Subscriptions,Posts,Comments,Votes
from .forms import PostForm
# Create your views here.

def HomePageView(request):
    return render(request,'home.html',{'boards':SubReddits.objects.all()})

def BoardView(request,id):
    return render(request, 'Board.html', {'posts': SubReddits.objects.get(id=id)})

def PostView(request,id):
    return render(request,'Post.html',{'comment':Posts.objects.get(id=id)})

def PostCreateView(request,id):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            b =get_object_or_404(SubReddits,id=id)
            text = request.POST['text']
            detail = request.POST['detail']
            Posts.objects.create(board=b,text=text,detail=detail,author=request.user.username)
            return redirect('home')
    else:
        form=PostForm()
    return redirect(request,'PostCreate.html',{'form':form})    
