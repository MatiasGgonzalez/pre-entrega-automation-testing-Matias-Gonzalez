#free_user_3LcDiPCRP33JWwthbRPNtqJY7C5   GETreqres.in/api/users?page=2  GETreqres.in/api/collections/products/recordsñ
import requests
import pytest






def test_obtener_usuario(base_url, headers):
    
    url = f"{base_url}/users/2"
    
    response = requests.get(url, headers=headers)

    # NIVEL 1: Código 200
    assert response.status_code == 200, f"Error: Código esperado es 200, el obtenido es {response.status_code}"

    # NIVEL 2: Headers
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3: Estructura
    data = response.json()
    
    # El json completo es un diccionario
    assert isinstance(data, dict)
    assert "data" in data
    
    # El valor de "data" es un diccionario que contiene los detalles del usuario
    assert isinstance(data["data"], dict)
    
    assert "id" in data["data"]
    assert "email" in data["data"]

    # NIVEL 4: Datos del usuario 
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"


    # NIVEL 5 DE VALIDACION : Tiempo de respuesta
    
    assert response.elapsed.total_seconds() < 2


def test_crear_usuario(base_url, headers):
    
    url = f"{base_url}/users"

    usuario = {
        "name": "morpheus",
        "first_name": "morpheus",
        "last_name": "morpheus",
        "email": "morpheus@reqres.in"
    }

    response = requests.post(url, headers=headers, json=usuario)

    # NIVEL 1: Código 201
    assert response.status_code == 201, f"Error: Código esperado es 201, el obtenido es {response.status_code}"
    
    # NIVEL 2: Headers
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3: Estructura
    data = response.json()
    assert "email" in data
    assert "id" in data
    assert "last_name" in data

    #NIVEL 4: Contenido 

    assert data["email"] == usuario["email"]
    assert data["last_name"] == usuario["last_name"]
    assert data["id"] is not None


    #NIVEL 5 DE VALIDACION : Tiempo de respuesta
    assert response.elapsed.total_seconds() < 2



 
def eliminar_usuario(base_url, headers):
    
    url = f"{base_url}/users/2"

    response = requests.delete(url, headers=headers)


    #NIVEL 1 : STATUS CODE 

    assert response.status_code == 204, f"Error: Código esperado 204, obtenido {response.status_code}"

    #NIVEL 2 : HEADERS

    assert "Content-Type" not in response.headers

    #NIVEL 3 Y 4 : ESTRUCTURA Y CONTENIDO

    assert len(response.content) == 0

    #NIVEL 5 DE VALIDACION : Tiempo de respuesta

    assert response.elapsed.total_seconds() < 2

    

