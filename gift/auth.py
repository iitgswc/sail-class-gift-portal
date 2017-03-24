import poplib

from .models import User


class WebMailAuthenticationBackend(object):

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    # error when user in database but wrong webmail login:timeout_connection error i think only in few servers
    def authenticate(self, **credentials):
        username = credentials.get('username', None)
        password = credentials.get('password', None)
        server = credentials.get('server', None)
        port = credentials.get('port', None)
        print("it is in webmail authentication part")
        try:
            user = User.objects.get(username=username)
            print("checking user in own database")
            print(user)
        except User.DoesNotExist:
            print("user not in our own database")
            return None
        try:
            print("calling pop3 function")
            response = poplib.POP3_SSL(host=server, port=port)
            response.user(user=username)
            password_string = response.pass_(pswd=password)
            print("after pop3 funtion")
            print(password_string)
            print(user)
            print("before this if condition in webmail authenticate")
            if 'OK' in str(password_string):
                print(password_string)
                print("there is ok in pop3 function")
                response.quit()
                return user

        except poplib.error_proto:
            return None
        except (ValueError, TypeError):
            return None