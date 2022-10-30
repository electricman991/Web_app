from django.urls import path

from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name= 'data'
urlpatterns = [
    # ex: /data/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/salary/', views.SalaryView.as_view(), name='salary'),
    path('about/', views.about, name='about'),
    
    
]