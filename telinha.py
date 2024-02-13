import tkinter
from tkinter import * #o símbolo de * significa TUDO, nesse caso importou tudo da biblioteca tkinter
from tkinter import ttk #aqui importou uma biblioteca (ttk) de dentro da outra biblioteca (tkinter)

#root = Tk() #cria uma tela vazia
#frm = ttk.Frame(root, padding=100) #cria um espaço dentro da tela #padding é o tamanho
#frm.grid() #define como grid (grade) e possibilita colocar os demais itens em posições com coluna (column) e linha (row)
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0) #cria um texto a ser visualizado
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1) #cria um botão interativo, que tem alguma função (pode ser alguma função que eu defino)
#root.mainloop() #é basicamente o executável, como se fosse um print()

def recuperar():
    hmmm = (eita).get("1.0",'end-1c')
    print(hmmm)

root = Tk() #cria uma tela vazia
frm = ttk.Frame(root, padding=100) #cria um espaço dentro da tela #padding é o tamanho
frm.grid() #define como grid (grade) e possibilita colocar os demais itens em posições com coluna (column) e linha (row)
Label(frm, text="Hello World!").grid(column=0, row=0) #cria um texto a ser visualizado
Button(frm, text="Recuperar", command=recuperar).grid(column=1, row=1) #cria um botão interativo, que tem alguma função (pode ser alguma função que eu defino)
eita = Text(frm, height=1, width=20)
eita.grid(column=1, row=0)
root.mainloop() #é basicamente o executável, como se fosse um print()