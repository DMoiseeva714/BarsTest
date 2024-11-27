import requests
from endpoints import Endp
from payloads import Payload

HOST = "https://uauirt-admin.bars.group/api"

login_payload = {
    "Login": "admin",
    "Password": "root"
}

#1 Залогинились
response = requests.post(
    url=f"{HOST}/Security/Login",
    json=login_payload
)

print(response.status_code)

#Получение токена
token = response.json().get('AccessToken')

#2 Получаем список физ лиц
response = requests.post(
    url=f"{HOST}/PhysicalPerson/List",
    headers= {"Authorization": f"Bearer {token}"},
)

print(response.json())