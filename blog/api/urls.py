from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^posts/$', views.posts, name="posts"),
    # re_path(r'^post/?p<pk>/$')
]
