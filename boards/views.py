from django.shortcuts import render,redirect,get_object_or_404
from .models import SubReddits,Subscriptions,Posts,Comments,Votes
from users.models import CustomUser
from .forms import PostForm,CommentForm
# Create your views here.

def HomePageView(request):
    return render(request,'home.html',{'boards':SubReddits.objects.all()})

def BoardView(request,id):
    s = SubReddits.objects.get(id=id)
    p=s.PostBoard.all()
    dv={}
    for i in p:
        vote=0
        for j in i.VotePost.all():
            vote+=j.value
        dv[i.id]=vote

    dc={}
    for i in p:
        c=0
        for j in i.CommentPost.all():
            c+=1
        dc[i.id]=c
    return render(request, 'Board.html', {'posts': SubReddits.objects.get(id=id),'vote':dv,'com':dc})

def PostView(request,id):
    p=Posts.objects.get(id=id)
    v=0
    for i in p.VotePost.all():
        v+=i.value
    return render(request,'Post.html',{'comment':p,'vote':v})

def PostCreateView(request,id):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            b =get_object_or_404(SubReddits,id=id)
            text = request.POST['text']
            detail = request.POST['detail']
            Posts.objects.create(board=b,text=text,detail=detail,author=str(request.user.username))
            return redirect('board',id=id)
    else:
        form=PostForm()
    return render(request,'PostCreate.html',{'form':form})    

def PostVoteView(request,id,value):
    if value=='1':
        v=1
    else:
        v=-1    
    Votes.objects.create(from_id=str(request.user.username),post_id=Posts.objects.get(id=id),value=v)
    return render(request, 'home.html', {'boards': SubReddits.objects.all()})

def PostCommentView(request,id,on):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            b = get_object_or_404(Posts, id=id)
            text = request.POST['text']
            if on=='p':
                Comments.objects.create(from_user=str(request.user.username), post_id=b, text=text)
            else:
                pass    
            return redirect('post', id=id)
    else:
        form=CommentForm()
    return render(request,'CommentCreate.html',{'form':form})    
