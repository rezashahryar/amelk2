from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class AuthWithMobileBackend(BaseBackend):

    def authenticate(self, request, username=None, mobile=None, password=None):
        try:
            user = get_user_model().objects.get(Q(username=username) | Q(mobile=username))
        except get_user_model().DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
