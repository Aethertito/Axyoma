
# ---------------------------------------------------------------------------- #

from django.urls import path
from . import views

# ---------------------------------------------------------------------------- #


app_name = 'public'

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
]

# ---------------------------------------------------------------------------- #