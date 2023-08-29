from django.urls import path
from .views import HomeView, ItemCreateView, ItemDetailView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('createitem/', ItemCreateView.as_view(), name = 'itemCreate'),
    path('<int:pk>/', ItemDetailView.as_view()),

]