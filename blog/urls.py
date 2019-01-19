from django.urls import path
from . import views
appname="blog"
urlpatterns = [
    path('<int:pk>', views.post_read, name="post_read"),
    path('post_list', views.post_list, name="post_list")
]
