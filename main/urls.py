from django.urls import path
from main import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('posts/', views.PostListCreateView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    # path('categories/', views.category_list),
    # path('categories1/', views.CategoryListView.as_view())
]