import requests
from tkinter import *
from tkinter import ttk

def obter_api():
    msg=campo_api.get("1.0",'end-1c')[:40]
    APIKEY.set(msg)

def pesquisar_animais(nome_do_bicho):

    api_url = f'https://api.api-ninjas.com/v1/animals?name={nome_do_bicho}'
    response = requests.get(api_url, headers={'X-Api-Key': APIKEY.get()})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Insira a sua chave API ").grid(column=0, row=0)
ttk.Button(frm, text = "Clica", command = obter_api).grid(column=2, row=0)
campo_api = Text(frm, height = 1, width = 40)
campo_api.grid(column=1, row=0)

APIKEY = StringVar()

root.mainloop() 
print(APIKEY.get())
