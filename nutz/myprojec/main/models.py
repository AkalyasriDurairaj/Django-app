from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.hashers import check_password

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.content[:20]

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
    

class PasswordHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)  # Store hashed passwords
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.password}"

    @staticmethod
    def is_recent_password(user, password):
        password_histories = PasswordHistory.objects.filter(user=user).order_by('-created_at')[:3]
        for password_history in password_histories:
            if check_password(password, password_history.password):
                return True
        return False

    @staticmethod
    def add_password_to_history(user, password):
        password_history = PasswordHistory(user=user, password=password)
        password_history.save()
        PasswordHistory.clean_old_passwords(user)

    @staticmethod
    def clean_old_passwords(user):
        all_passwords = PasswordHistory.objects.filter(user=user).order_by('-created_at')
        if all_passwords.count() > 3:
            to_delete = all_passwords[3:]
            to_delete.delete()
