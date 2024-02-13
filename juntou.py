import requests
from tkinter import *
from tkinter import ttk

def tela1():
    global root, campo_api, APIKEY
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    Label(frm, text="Insira a sua chave API ").grid(column=0, row=0) #esse é só o texto da esquerda
    Button(frm, text="Prosseguir", command=fun1).grid(column=2, row=0) #lambda permitiu usar mais de um comando para a função (fun1 e fun2) só tem que def elas
    campo_api = Text(frm, height = 1, width = 41)
    campo_api.grid(column=1, row=0) #esse é o espaço de texto em si, onde a pessoa vai colocar a chave API dela 
    root.title("Validação da API") #o nome do arquivo da janela (nesse caso, root) + .title permite ALTERAR O NOME dele 
    APIKEY = StringVar() 
    root.mainloop() 

def tela2():
    global root2, resposta
    root2 = Tk()
    frm = ttk.Frame(root2, padding=50)
    frm.grid()
    root2.title("Seleção do Animal")
    Label(frm, text = "Escolha o seu animal ").grid(column=0, row=0)
    resposta = Text(frm, height=1, width=20)
    resposta.grid(column=1, row=0)
    Button(frm, text="Pronto", command=search_animal).grid(column=1, row=2) #falta o command para pesquisar o animal
    Button(frm, text="Voltar", command=retornar).grid(column=2, row=2) #falta o command para retornar
    root2.mainloop()

def obter_api(): #essa função coleta os 40 primeiros dígitos (0-39) postos como resposta pelo usuário  #FALTA VALIDAR A SENHA
    msg = (campo_api).get("1.0",'end-1c')[:40] #o trecho >> 1.0",'end-1c' << se refere a posição espacial de onde deve ser coletado (.get) os dados
    if len(msg) == 40:
        APIKEY.set(msg) #esse comando (.set) define essa msg como variável APIKEY 
        pesquisar_animais
        if root.winfo_exists():
            root.destroy()
        tela2()
    else:
        print("Tente novamente! A chave API deve conter 40 caracteres.") 
        root.mainloop()

def pesquisar_animais(nome_do_bicho):
    global response
    api_url = f'https://api.api-ninjas.com/v1/animals?name={nome_do_bicho}'
    response = requests.get(api_url, headers={'X-Api-Key': APIKEY.get()}) #esse requests.get é uma função diferente do .get tradicional!! ela puxa informação de uma url
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

def fun1():
    obter_api() #função associada ao botão de root para obter a API e deixar na memória armazenado

def search_animal():
    nome = (resposta).get("1.0", 'end-1c')
    pesquisar_animais(nome) #essa função que está printando o resultado no console
    frame_tela2()

def retornar():
    root2.destroy()
    tela1()

def fechar1():
    inicial.destroy()

def espaço_branco():
    vazio = Label()
    vazio.pack()

def print_sobre1():
    print("Este é um programa utilizado para pesquisar por animais. Que tal começar buscando por 'quetzal'?")

def print_sobre2():
    print("Idealizado por Ribeiro-chan e Seiji-kun.")

def frame_tela2():
    texto = response.text
    novo_frame = ttk.Frame(root2)
    novo_frame.grid()
    caixa_texto = Text(novo_frame, height=50, width=100, wrap="word")
    caixa_texto.grid(column=0, row=3)
    caixa_texto.insert("end-1c", texto)

    #novo_label = Label(text=texto, height=100, width=200)
    #novo_label.grid(column=0, row=4)

#INFORMAÇÕES SOBRE A TELA INICIAL    
inicial = Tk()
inicial.title("Tela Inicial")
inicial.geometry("300x200")

barrademenu = Menu(inicial) #criação da barra de menus
menu_sobre = Menu(barrademenu, tearoff=0) 
menu_sobre.add_command(label="Sobre", command=print_sobre1)
menu_sobre.add_command(label="Criadores", command=print_sobre2)
menu_sobre.add_separator()
menu_sobre.add_command(label="Fechar", command=inicial.quit)
barrademenu.add_cascade(label="Informações", menu=menu_sobre) #definição de uma das abas
inicial.config(menu=barrademenu)

Times = ("Arial", 15)
botao_inicio = Button(inicial, text="COMEÇAR", font=Times, justify="center", bg="light gray", command=lambda:[fechar1(), tela1()])
espaço_branco()
espaço_branco()
espaço_branco()
botao_inicio.pack()
inicial.mainloop()