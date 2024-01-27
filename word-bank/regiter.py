from database import Auth

def authorize_user():
    auth = Auth()

    answer = input('are you a registered user?[Y/N]: ').lower()

    is_loggedin = auth.register() if not answer == 'y' else auth.login()
        
    return True if is_loggedin else False
    