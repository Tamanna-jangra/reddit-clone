from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView,name='home'),
    path('userhome/', views.UserHomeView,name='userhome'),
    path('all/', views.AllPostView,name='allpost'),
    path('board/<int:id>', views.BoardView,name='board'),
    path('post/<int:id>', views.PostView,name='post'),
    path('new/<int:id>', views.PostCreateView,name='new_post'),
    path('vote/<int:id>/<path:value>/<on>/<int:pid>', views.VoteView,name='post_vote'),
    path('comment/<int:id>', views.PostCommentView,name='post_comment'),
    path('delete/<int:id>/<int:pid>/<on>', views.DeleteView,name='post_delete'),
    path('subscribe/<int:id>',views.SubscribeView,name='subscribe'),
    path('unsubscribe/<int:id>',views.UnsubscribeView,name='unsubscribe'),
    #REST API urls
    path('api/',views.SubRedditList.as_view()),
    path('api/<int:pk>/', views.SubRedditDetail.as_view()),

    path('api/subscriptions/',views.SubscriptionsList.as_view()),
    path('api/subscriptions/<int:pk>/', views.SubscriptionsDetail.as_view()),

    path('api/posts/',views.PostsList.as_view()),
    path('api/posts/<int:pk>/', views.PostsDetail.as_view()),

    path('api/comment/',views.CommentsList.as_view()),
    path('api/comment/<int:pk>/', views.CommentsDetail.as_view()),

    path('api/votes',views.VotesList.as_view()),
    path('api/votes/<int:pk>/', views.VotesDetail.as_view()),
]
