from django.shortcuts import render,redirect,get_object_or_404
from .models import SubReddits,Subscriptions,Posts,Comments,Votes
from users.models import CustomUser
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def HomePageView(request):
    l=[]
    for i in Subscriptions.objects.filter(user_id=str(request.user.username)):
        l.append(i.Boards_id.id)
    return render(request, 'home.html', {'boards': SubReddits.objects.all(), 'subs':l})

@login_required
def BoardView(request,id):
    '''
    Shows the post of a board(subreddit)
    '''
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
    l=[]
    for i in Subscriptions.objects.filter(user_id=str(request.user.username)):
        l.append(i.Boards_id.id)
    return render(request, 'Board.html', {'posts': SubReddits.objects.get(id=id), 'vote': dv, 'com': dc, 'subs':l})

@login_required
def PostView(request,id):
    '''
    show detailed post view
    '''
    p=Posts.objects.get(id=id)
    pv=0
    c=0
    for i in p.VotePost.all():
        pv+=i.value
    for i in p.CommentPost.all():
        c+=1

    d={}
    for i in p.CommentPost.all():
        cv=0
        for j in i.VoteComment.all():
            cv+=j.value
        d[i.id]=cv    
    return render(request,'Post.html',{'comment':p,'vote':pv,'com':c,'comVote':d})

@login_required
def PostCreateView(request,id):
    '''
    form for creating posts
    '''
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

@login_required
def VoteView(request,id,value,on,pid):
    '''
    for voting
    '''
    if value=='1':
        v=1
    else:
        v=-1
    if on=='p':        
        Votes.objects.create(from_id=str(request.user.username),post_id=Posts.objects.get(id=id),value=v)
        return BoardView(request,pid)
    elif on=='pi':        
        Votes.objects.create(from_id=str(request.user.username),post_id=Posts.objects.get(id=id),value=v)
        return PostView(request,pid)
    else:
        Votes.objects.create(from_id=str(request.user.username),comment_id=Comments.objects.get(id=id),value=v)
        return PostView(request,pid)

@login_required
def PostCommentView(request,id):
    '''
    comment form
    '''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            b = get_object_or_404(Posts, id=id)
            text = request.POST['text']
            Comments.objects.create(from_user=str(request.user.username), post_id=b, text=text)
               
            return redirect('post', id=id)
    else:
        form=CommentForm()
    return render(request,'CommentCreate.html',{'form':form})    

@login_required
def DeleteView(request,id,pid,on):
    '''
    deleting Comment and post
    '''
    if on=='p':
        Posts.objects.get(id=id).delete()
    else:
        Comments.objects.get(id=id).delete()
        
    if on=='p':
        return BoardView(request,pid)
    else:
        return PostView(request,pid)

def SubscribeView(request,id):
    Subscriptions.objects.create(user_id=str(request.user.username),Boards_id=SubReddits.objects.get(id=id))
    return HomePageView(request)        
def UnsubscribeView(request,id):
    Subscriptions.objects.get(user_id=str(request.user.username), Boards_id=SubReddits.objects.get(id=id)).delete()
    return HomePageView(request)


@login_required
def UserHomeView(request):
    '''
    Shows the post of a board(subreddit)
    '''
    s=Subscriptions.objects.filter(user_id=str(request.user.username))
    lsubs=[]
    for i in s:
        lsubs.append(i.Boards_id.PostBoard.all())
    dv = {}
    for p in lsubs:
        for i in p: 
            vote = 0
            for j in i.VotePost.all():
                vote += j.value
            dv[i.id] = vote

    dc = {}
    for p in lsubs:
        for i in p:
            c = 0
            for j in i.CommentPost.all():
                c += 1
            dc[i.id] = c
    l=[]
    for i in lsubs:        
        l+=i
    return render(request, 'UserHome.html', {'vote': dv, 'com': dc,'subs':l})

def AllPostView(request):
    return render(request,'AllPost.html',{'post':Posts.objects.all()})   
