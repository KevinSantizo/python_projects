from django.urls import path
from . import views

app_name = 'voluntary'
urlpatterns = [
    path('<int:pk>/', views.ListActivities.as_view(), name='list_activities'),
    path('', views.IndexView.as_view(), name='index'),
]