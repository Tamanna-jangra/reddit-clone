from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView,name='home'),
    path('board/<int:id>', views.BoardView,name='board'),
    path('post/<int:id>', views.PostView,name='post'),
    path('new/<int:id>', views.PostCreateView,name='new_post'),
    path('vote/<int:id>/<path:value>/<on>/<int:pid>', views.VoteView,name='post_vote'),
    path('comment/<int:id>', views.PostCommentView,name='post_comment'),
    path('delete/<int:id>/<int:pid>/<on>', views.DeleteView,name='post_delete'),
    path('subscribe/<int:id>',views.SubscribeView,name='subscribe'),
]
