from django.urls import path

from .views import HomeView, CreateView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateView.as_view(), name='create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
]