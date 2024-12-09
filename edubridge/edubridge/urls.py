"""
URL configuration for edubridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

 path('', views.login, name='login'),  # Login page path('signup/', views.signup_view, name='signup'),  # Signup page

path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard after signup
path('home/', views.home, name='home'),  # Home page after login
     path('Donate/', views.Donate, name='Donate'),
     path('receive/', views.receive, name='receive'),
      path('alumini/', views.alumini, name='alumini'),

path('admin/', admin.site.urls),
]
