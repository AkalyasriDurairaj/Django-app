from django.urls import path
from .views import signup_view, login_view, change_password_view, post_message_view, home_view, logout_view, edit_post_view, delete_post_view, add_comment_view, edit_comment_view, delete_comment_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('change-password/', change_password_view, name='change_password'),
    path('post-message/', post_message_view, name='post_message'),
    path('edit-post/<int:post_id>/', edit_post_view, name='edit_post'),
    path('delete-post/<int:post_id>/', delete_post_view, name='delete_post'),
    path('add-comment/<int:post_id>/', add_comment_view, name='add_comment'),
    path('edit-comment/<int:comment_id>/', edit_comment_view, name='edit_comment'),
    path('delete-comment/<int:comment_id>/', delete_comment_view, name='delete_comment'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
]