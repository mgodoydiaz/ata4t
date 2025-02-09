from .xAPIConnector import *
from . import file_tools
#from xAPIConnector import *
#import file_tools
def login(userId, password):
    """En base a un archivo json de credenciales se loguea en la API de xAPI"""

    # Crear una instancia de cliente de API
    client = APIClient()

    login_response = client.execute(loginCommand(userId=userId, password=password))
    if not login_response.get('status'):
        raise(Exception("Login failed:", login_response.get('errorCode')))
    return client, login_response.get('streamSessionId')

if __name__ == '__main__':
    
    # Cargar credenciales
    credentials = file_tools.read_credentials('../../credentials.json')

    # Credenciales de inicio de sesión
    userId = credentials['userID']
    password = credentials['password']

    _, streamSessionId = login(userId, password)
    print("StreamSessionId:", streamSessionId)

