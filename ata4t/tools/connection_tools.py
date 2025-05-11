from .xAPIConnector import *
from . import file_tools

if __name__ == '__main__':

    # Cargar credenciales
    credentials = file_tools.read_credentials('credentials.json')

    # Credenciales de inicio de sesión
    userId = credentials['userID']
    password = credentials['password']

    # Crear una instancia de cliente de API
    client = APIClient()

    # Intenta iniciar sesión
    login_response = client.execute(loginCommand(userId=userId, password=password))
    if not login_response.get('status'):
        print("Login failed:", login_response.get('errorCode'))
    else:
        print("Login successful")
        streamSessionId = login_response.get('streamSessionId')


