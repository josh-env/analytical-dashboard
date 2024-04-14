from django.urls import path

from . import views,forms

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"), 
    path('login/', forms.BootstrapAuthenticationForm, name="login"), 
]