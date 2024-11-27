import requests


class Auth:

    def __init__(self):
        self.response = None

    def login(self) -> requests:
        self.response = requests.post(
            url='https://uauirt-admin.bars.group/api/Security/Login',
            json={
                'Login': 'admin',
                'Password': 'root'
            }
        )
        
    
    def get_token(self) -> str:
        return self.response.json().get('AccessToken')
    
user = Auth()
user.login()

print(user.get_token())

