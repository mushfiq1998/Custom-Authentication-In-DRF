from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        try:
            '''If user sends incorrect username raises exception 
            and throws to exception block'''
            user = User.objects.get(username=username)
        # Catch exception and handles it, 
        # so that the execution of the code is not stopped.
        except User.DoesNotExist:
            raise AuthenticationFailed('No such user')
        # Else block always will be executed 
        # If usename is correct, no exception is resied. and returns user.
        # If authetication succeeds returns user, None otherwise.
        return (user, None)
