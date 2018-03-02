from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView,name='home'),
    path('board/<int:id>', views.BoardView,name='board'),
    path('post/<int:id>', views.PostView,name='post'),
    path('new/<int:id>', views.PostCreateView,name='new_post'),
    path('vote/<int:id>/<path:value>', views.PostVoteView,name='post_vote'),
]
