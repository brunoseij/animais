import requests
from tkinter import *
from tkinter import ttk

def tela1():
    global root, campo_api
    root = Tk()
    root.title("Validação da API") #o nome do arquivo da janela (nesse caso, root) + .title permite ALTERAR O NOME dele 
    root.geometry('700x200+800+250')
    frm = ttk.Frame(root, padding=80)
    frm.grid()
    Label(frm, text="Insira a sua chave API").grid(column=0, row=0) #esse é só o texto da esquerda
    campo_api = Text(frm, height = 1, width = 40)  
    campo_api.grid(column=1, row=0) #esse é o espaço de texto em si, onde a pessoa vai colocar a chave API dela 
    Button(frm, text="Prosseguir", command=obter_api).grid(column=2, row=0) #VERIFICAR se dá pra usar o obter_api direto ou armazena em fun1
    root.mainloop() 
    
def tela2():
    global root2, resposta
    root2 = Tk()
    root2.title("Seleção do Animal")
    frm = ttk.Frame(root2, padding=50)
    frm.grid()
    Label(frm, text = "Escolha o seu animal ").grid(column=0, row=0)
    resposta = Text(frm, height=1, width=20)
    resposta.grid(column=1, row=0)
    Button(frm, text="Pronto", command=search_animal).grid(column=1, row=2) #falta o command para pesquisar o animal
    Button(frm, text="Voltar", command=retornar).grid(column=2, row=2) #falta o command para retornar
    root2.mainloop()
    
def obter_api(): #essa função coleta os 40 primeiros dígitos (0-39) postos como resposta pelo usuário  #FALTA VALIDAR A SENHA
    global APIKEY
    msg = (campo_api).get("1.0",'end-1c')[:40] #o trecho >> 1.0",'end-1c' << se refere a posição espacial de onde deve ser coletado (.get) os dados
    APIKEY = StringVar()
    if len(msg) == 40:
        APIKEY.set(msg) #esse comando (.set) define essa msg como variável APIKEY 
        response = requests.get('https://api.api-ninjas.com/v1/animals?name=seahorse', headers={'X-Api-Key': APIKEY.get()})
        if response.ok == True:
            root.destroy()
            tela2()
        else: 
            print('\033[1;31mAPI Inválida\033[m')
    else:
        print("\033[31mTente novamente! A chave API deve conter 40 caracteres\033[m.") 

def pesquisar_animais(nome_do_bicho):
    global response
    api_url = f'https://api.api-ninjas.com/v1/animals?name={nome_do_bicho}'
    response = requests.get(api_url, headers={'X-Api-Key': APIKEY.get()}) #esse requests.get é uma função diferente do .get tradicional!! ela puxa informação de uma url
    if response.ok == True:
        response.text
    else:
        print("Error:", response.status_code, response.text)

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
    print("Este é um programa utilizado para pesquisar por animais.")

def print_sobre2():
    print("Idealizado por Ribeiro-chan e Seiji-kun.")

def frame_tela2():
    novo_frame = ttk.Frame(root2)
    novo_frame.grid()
    texto = response.text
    caixa_texto = Text(novo_frame, height=50, width=100, wrap="word")
    caixa_texto.grid(column=0, row=3)
    caixa_texto.insert("end-1c", texto)

#INFORMAÇÕES SOBRE A TELA INICIAL    
inicial = Tk()
inicial.title("Tela Inicial")
inicial.geometry("300x200+1000+250")

barrademenu = Menu() #criação da barra de menus
menu_sobre = Menu(barrademenu, tearoff=0) 
menu_sobre.add_command(label="Sobre", command=print_sobre1)
menu_sobre.add_command(label="Criadores", command=print_sobre2)
menu_sobre.add_separator()
menu_sobre.add_command(label="Fechar", command=inicial.quit)
barrademenu.add_cascade(label="Informações", menu=menu_sobre) #definição de uma das abas
inicial.config(menu=barrademenu)

botao_inicio = Button(inicial, text="COMEÇAR", font='Arial 20', bg="light gray", command=lambda:[fechar1(), tela1()]) #fecha a tela inicial e abre a tela 1
botao_inicio.pack(pady=70) #ipadx e ipady definem a distância do texto até a borda do widget, enquanto que padx e pady criam um espaço em branco ao redor do widget
inicial.mainloop()
