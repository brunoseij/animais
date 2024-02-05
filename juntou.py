import requests
from tkinter import *
from tkinter import ttk

def obter_api(): #essa função coleta os 40 primeiros dígitos (0-39) postos como resposta pelo usuário 
    msg = campo_api.get("1.0",'end-1c')[:40] #o trecho >> 1.0",'end-1c' << se refere a posição espacial de onde deve ser coletado (.get) os dados
    APIKEY.set(msg) #esse comando (.set) define essa msg como variável APIKEY 

def pesquisar_animais(nome_do_bicho):

    api_url = f'https://api.api-ninjas.com/v1/animals?name={nome_do_bicho}'
    response = requests.get(api_url, headers={'X-Api-Key': APIKEY.get()}) #esse requests.get é uma função diferente do .get tradicional!! ela puxa informação de uma url
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Insira a sua chave API ").grid(column=0, row=0) #esse é só o texto da esquerda
ttk.Button(frm, text = "Clica", command = obter_api).grid(column=2, row=0) #nesse caso, o comando associado ao botão é de uma função definida (def obter_api)
campo_api = Text(frm, height = 1, width = 40)
campo_api.grid(column=1, row=0) #esse é o espaço de texto em si, onde a pessoa vai colocar a chave API dela 
root.title("Ohayou, Seiji-kun!") #o nome do arquivo da janela (nesse caso, root) + .title permite ALTERAR O NOME dele 
APIKEY = StringVar() 

root.mainloop() 
print(APIKEY.get()) #isso aqui é só pra confirmar que ele tá salvando a APIKEY da pessoa corretamente!!