import PySimpleGUI as sg
import pandas as pd
from enviar_email import enviar_email

layout = [
    [sg.Text("Título: ")],
    [sg.Input("", size=(30, 20), key="Título")],
    [sg.Text("Corpo: ")],
    [sg.Multiline("", size=(50, 10), key="Corpo")],
    [sg.Text("Imagens: ")],
    [sg.FileBrowse("Selecionar Arquivo", key="-FILE-", enable_events=True),
     sg.Button("Adicionar Imagem", key="-ADD IMAGE-")], 
    [sg.Listbox(values=[], enable_events=True, size=(40, 5), key="-FILE LIST-")],
    [sg.Text("Arquivo excel para emails"), sg.FileBrowse("Selecionar Arquivo", key="Arquivo excel para emails")],
    [sg.Button("Enviar Email", key="-SEND-")],
]

window = sg.Window(title="Bot Email", layout=layout, margins=(100, 100))

file_list = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-ADD IMAGE-":
        filename = values["-FILE-"]
        if filename:
            file_list.append(filename)
            window["-FILE LIST-"].update(file_list)

    if event == "-SEND-":
        titulo = values["Título"]
        corpo = values["Corpo"]
        caminho_excel = values["Arquivo excel para emails"]

        arquivo = pd.read_excel(caminho_excel)
        emails = arquivo["EMAIL"].tolist()

        for email in emails:
            enviar_email(email, titulo, corpo,  file_list)
            print(f"Email enviado para {email}")
        
        
window.close()
