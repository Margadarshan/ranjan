from django.urls import path
from .views import post_list,PostCreateView,PostUpdateView,PostDeleteView


urlpatterns=[
	path('',post_list,name='blog-home'),
	path('new/',PostCreateView.as_view(),name='post-create'),
	path('<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]
