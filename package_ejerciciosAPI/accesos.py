import requests


def accederAPI(_url):
    response = requests.get(_url)
    print(response)
    api_data = response.json()
    return api_data
