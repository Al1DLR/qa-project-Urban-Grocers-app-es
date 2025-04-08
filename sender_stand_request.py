import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json()["authToken"])

authtoken = response.json()["authToken"]
def post_new_client_kit(kit_body, authtoken):
    header1 = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {authtoken}' }
    return  requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                           json= kit_body,
                           headers=header1)
response = post_new_client_kit(data.kit_body, authtoken)
print(response.status_code)

