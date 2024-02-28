import requests #importa o banco de dados chamado REQUESTS

def pesquisar_animais(API_KEY, nome_do_bicho): #função pede por 2 parâmetros (chave API e nome do animal)

    api_url = f'https://api.api-ninjas.com/v1/animals?name={nome_do_bicho}' #o nome do animal, colocado na função pesquisar_animais entra nesse espaço {nome_do_bicho} e busca por ele no banco de dados referenciado no url
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY}) 
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    
api = input("Digite a sua chave API ") #variável api
bicho = input("Digite o nome do bicho ") #variável bichog
pesquisar_animais(api, bicho) #novamente, pede por 2 parâmetros até então

pesquisar_outro = input("Gostaria de ver mais bicho? ") #LEMBRAR que é executado em sequência, ele executa esta daqui depois de rodar um pesquisar_animais
while pesquisar_outro == 's' or 'sim': #determina uma CONDIÇÃO, nesse caso, a resposta ser " s ". Caso seja atendido o critério, repete o bloco de códigos da l17 e l18
    pesquisar_animais(api,input("Coloca o nome então ")) #api já está definido, portanto o input é apenas para o animal (único parâmetro)
    pesquisar_outro = input("Qué mais? ")
print("Obrigado por usar nossos serviços, adeus") #essa função irá rodar assim que o loop do while terminar ou não for executado
