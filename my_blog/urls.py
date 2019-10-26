from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from my_blog import views

urlpatterns = [
    path('/',views.PostListView.as_view(),name="post_list"),
    path('about/',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="post_detail"),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
]
