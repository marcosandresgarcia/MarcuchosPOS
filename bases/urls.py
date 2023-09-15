from django.urls import path
from django.contrib.auth import views as aut_views
from bases.views import Home, HomeUnauthorizedView

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('login/', aut_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', aut_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
    path('unauthorized/', HomeUnauthorizedView.as_view(), name='unauthorized')
]