from django.utils.deprecation import MiddlewareMixin
from .models import PasswordHistory

class InitialPasswordHistoryMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            user = request.user
            if not PasswordHistory.objects.filter(user=user).exists():
                PasswordHistory.add_password_to_history(user, user.password)
