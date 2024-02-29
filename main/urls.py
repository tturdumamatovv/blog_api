from django.urls import path, include

from . import views

# №3 способ CRUD
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='Post')
# ===================================================================

# http://localhost:8000/api/v1/post/ --> views.PostListView

urlpatterns = [
    path('', include(router.urls)),   # №3 способ CRUD
    path('categories/', views.CategoryListView.as_view()),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]