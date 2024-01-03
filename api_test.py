import requests

# Función para obtener datos de la API y convertirlos a una lista


def get_api_data(url):
    try:
        # solicitud HTTP para obtener el JSON de la URL
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()  # Convertir JSON a un diccionario
        result = []  # Para que sea una lista
        for key, value in json_data.items():  # Recorrer el diccionario y agregar cada par clave-valor a la lista
            result.append((key, value))
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return None


# URL's
url_person = "https://randomuser.me/api/"
url_dog_breed = "https://api.thedogapi.com/v1/breeds/1"
url_random_data_en = "https://jsonplaceholder.typicode.com/posts/1"

# Obtener datos de la API
result_person = get_api_data(url_person)
result_dog_breed = get_api_data(url_dog_breed)
result_random_data_en = get_api_data(url_random_data_en)

# Imprimir resultados
if result_person is not None:
    print("Person Result:")
    for item in result_person:
        print(f"('{item[0]}', {item[1]})")

if result_dog_breed is not None:
    print("\nDog Breed Result:")
    for item in result_dog_breed:
        if isinstance(item[1], list):
            print(f"('{item[0]}', {item[1]})")
        else:
            print(f"('{item[0]}', '{item[1]}')")

if result_random_data_en is not None:
    print("\nRandom Data in English Result:")
    for item in result_random_data_en:
        if isinstance(item[1], list):
            print(f"('{item[0]}', {item[1]})")
        else:
            print(f"('{item[0]}', '{item[1]}')")
