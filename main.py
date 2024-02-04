import requests

def pesquisar_animais(API_KEY, nome_do_bicho):

    api_url = f'https://api.api-ninjas.com/v1/animals?name={nome_do_bicho}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    
api = input("Digite a sua chave API ")
bicho = input("Digite o nome do bicho ")
pesquisar_animais(api, bicho)
pesquisar_outro = input("Gostaria de ver mais bicho?")
while pesquisar_outro == "s":
    pesquisar_animais(api,input("Coloca o nome então"))
    pesquisar_outro = input("Qué mais?")
print("Obrigado")