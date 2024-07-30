from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Post, Comment,User
from .models import PasswordHistory

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'is_public']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def clean_new_password1(self):
        new_password = self.cleaned_data.get('new_password1')
        if PasswordHistory.is_recent_password(self.user, new_password):
            raise forms.ValidationError("The new password cannot be one of the last three passwords.")
        return new_password