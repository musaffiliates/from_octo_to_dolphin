import requests


def get_dolphin_token(login, password):
    json_data = {
        'username': DOLPHIN_LOGIN,
        'password': DOLPHIN_PASSWORD,
    }
    response = requests.post('http://142.132.182.77:81/auth/login', json=json_data)
    return response.json()['token']
# ⛔️ Don't touch the code above


DOLPHIN_LOGIN = 'jilam44457@lenfly.com'  # 👈 Replace <dolphin_login> to login for Dolphin Anty
DOLPHIN_PASSWORD = 'qwerty12345'  # 👈 Replace <dolphin_password> to password for Dolphin Anty
OCTO_TOKEN = '02efcad322fa4332a3da04d4dc6c07a3'  # 👈 Replace <octo_token> to token from Octo Browser

# ⛔ Don't touch the code below
DOLPHIN_TOKEN = f'Bearer {get_dolphin_token(DOLPHIN_LOGIN, DOLPHIN_PASSWORD)}'
