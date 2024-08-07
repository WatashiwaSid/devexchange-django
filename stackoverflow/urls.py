"""
URL configuration for stackoverflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from stackusers import views as user_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stackbase.urls')),
    path('about/', views.about, name="about"),

    #Authentication
    path('register/', user_view.register, name="register"),
    path('login/', auth_view.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name="logout.html"), name="logout"),

    #Profile
    path('profile/', user_view.profile, name="profile"),
    path('profile/profileUpdate', user_view.profileUpdate, name="profileUpdate"),

    #Tailwind Browser Reload
    path("__reload__/", include("django_browser_reload.urls")),

    #CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
