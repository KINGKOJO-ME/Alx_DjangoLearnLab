from django.urls import path
from . import views
from .views import search_posts, posts_by_tag
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView
)

urlpatterns = [

    path('posts/', PostListView.as_view(), name='post-list'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),

    path('comments/<int:pk>/edit/', views.edit_comment, name='edit-comment'),

    path('comments/<int:pk>/delete/', views.delete_comment, name='delete-comment'),

    path('search/', search_posts, name='search-posts'),

    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
    
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

]


from .views import CommentCreateView, CommentUpdateView, CommentDeleteView


path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),

path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),