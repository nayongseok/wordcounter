from django.contrib import admin
from django.urls import path, include 
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include ('blog.urls')),
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
    path('make/', wordcount.views.make, name="make")
]
