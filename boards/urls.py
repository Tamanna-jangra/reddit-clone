from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView,name='home'),
    path('board/<int:id>', views.BoardView,name='board'),
]
