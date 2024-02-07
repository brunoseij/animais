import requests
from tkinter import *
from tkinter import ttk

def obter_api(): #essa função coleta os 40 primeiros dígitos (0-39) postos como resposta pelo usuário 
    msg = campo_api.get("1.0",'end-1c')[:40] #o trecho >> 1.0",'end-1c' << se refere a posição espacial de onde deve ser coletado (.get) os dados
    if len(msg) == 40:
        APIKEY.set(msg) #esse comando (.set) define essa msg como variável APIKEY 
        #print(APIKEY.get()) #teste para ver se a API está salvando dentro da função obter_api
    else:
        print("Tente novamente! A chave API deve conter 40 caracteres.")
        root.mainloop()

def pesquisar_animais(nome_do_bicho):

    api_url = f'https://api.api-ninjas.com/v1/animals?name={nome_do_bicho}'
    response = requests.get(api_url, headers={'X-Api-Key': APIKEY.get()}) #esse requests.get é uma função diferente do .get tradicional!! ela puxa informação de uma url
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

def fun1():
    obter_api() #função associada ao botão de root para obter a API e deixar na memória armazenado

def fun2(): #função associado ao botão de root para fechar a telinha
    root.destroy()

def retornar():
    root.mainloop() #não tá abrindo a tela 1 -> será porque é um código anterior?
    #tela2.destroy() #fecha a tela 2
    #print("será que tá indo?")

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
Label(frm, text="Insira a sua chave API ").grid(column=0, row=0) #esse é só o texto da esquerda
Button(frm, text="Prosseguir", command=lambda: [fun1(), fun2()]).grid(column=2, row=0) #lambda permitiu usar mais de um comando para a função (fun1 e fun2) só tem que def elas
campo_api = Text(frm, height = 1, width = 41)
campo_api.grid(column=1, row=0) #esse é o espaço de texto em si, onde a pessoa vai colocar a chave API dela 
root.title("Validação da API") #o nome do arquivo da janela (nesse caso, root) + .title permite ALTERAR O NOME dele 
APIKEY = StringVar() 
root.mainloop() 

tela2 = Tk()
frm = ttk.Frame(tela2, padding=50)
frm.grid()
tela2.title("Seleção do Animal")
Label(frm, text = "Escolha o seu animal ").grid(column=0, row=0)
digitar = Text(frm, height=1, width=20)
digitar.grid(column=1, row=0)
Button(frm, text="Pronto").grid(column=1, row=1) #falta o command para pesquisar o animal
Button(frm, text="Voltar", command=retornar).grid(column=2, row=2) #falta o command para retornar
tela2.mainloop()