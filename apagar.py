import tkinter as tk
from tkinter import * 
from tkinter import ttk 

def recuperar():
    input = (mensagem).get("1.0", 'end-1c')
    #print(input) #verificar se a mensagem está sendo captada

def fechar():
    janela.destroy()

def espaço_branco():
    vazio = Label()
    vazio.pack()

def resposta_console():
    frase = cbox.get()
    print(frase)

def mudar_coisa():
    surpresa.config(text="Poha menó, falei pra não clicar", width= 30, fg="white",bg="black")

janela = Tk() #cria a janela
janela.title("Amor Doce 2.0") #altera o título da janela
janela.geometry("250x250") #define as dimensões da janela (largura x altura)

barra = Menu(janela) #esse é o MENU completo  #barra.add_command(label="hmmmm") #adiciona uma aba ("hmmmm") no menu principal (barra)
MenuCont = Menu(barra, tearoff=0) #essa vai ser uma das abas do menu  #tearoff=0 tira uma linha por padrão
MenuCont.add_command(label="Novo", command=espaço_branco) #essa e as debaixo são as funções dentro dessa barra (MenuCont)
MenuCont.add_command(label="Pesquisar", command=espaço_branco) 
MenuCont.add_command(label="Remover", command=espaço_branco)
MenuCont.add_separator() #adiciona uma linha que separa
MenuCont.add_command(label="Fechar", command=janela.quit) #janela.quit fecha a janela
barra.add_cascade(label="Contatos", menu=MenuCont) #adiciona o nome à barra e as lista a partir dessa (os add.command acima)
janela.config(menu=barra)

surpresa = Button(text="NÃO CLICA", fg="black", bg="yellow", command=mudar_coisa)
saudacao = Label(text="H-Henrik-chan? ", fg="red", bg="black")      #fg = muda a cor do texto     bg = muda a cor do fundo
continuacao = Label(text="O-Ohayou...", fg="#FC7F3F", bg="black", relief=RAISED) #a cor pode ser em sistema RGB hexadecimal
mensagem = Text(height=1, width=10)
ListCham = Label(text="Opções de diálogo", fg="green", width=25)
ListResp = ["Olá, me chamou?","Karina, é você meu amor?","Alô, quem fala?","Oi, desculpa, não te vi"]
cbox = ttk.Combobox(values=ListResp, width=25)
cbox.set("Olá, me chamou?")
botao = Button(text="Conversar", fg="medium violet red", bg="white", command=resposta_console)
saudacao.pack()
continuacao.pack()
espaço_branco()
#mensagem.pack()
#botao.pack()
ListCham.pack()
cbox.pack()
espaço_branco()
botao.pack()
espaço_branco()
surpresa.pack()
janela.mainloop()