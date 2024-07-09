import requests


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': 'a0ZGEN85wwKRoRX/pNb9eQ==QwE9jROfxws2oVNM'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data:
            return data
        else:
            return None
    else:
        print("Error:", response.status_code, response.text)
        return []
