from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from dashboard import forms
urlpatterns = [
    path('', include("dashboard.urls")),
    path('admin/', admin.site.urls),
       path('dashboard/login/',
         LoginView.as_view
         (
             template_name='dashboard/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),

    path('dashboard/logout/', LogoutView.as_view(next_page='/'), name='logout'),    
]
