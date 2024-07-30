"""
URL configuration for myprojec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('post-message/', views.post_message_view, name='post_message'),
    path('edit-post/<int:post_id>/', views.edit_post_view, name='edit_post'),
    path('delete-post/<int:post_id>/', views.delete_post_view, name='delete_post'),
    path('add-comment/<int:post_id>/', views.add_comment_view, name='add_comment'),
    path('edit-comment/<int:comment_id>/', views.edit_comment_view, name='edit_comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment_view, name='delete_comment'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),  
]


