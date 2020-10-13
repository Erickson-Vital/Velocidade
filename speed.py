from PySimpleGUI import PySimpleGUI as sg
from speedtest import Speedtest

st = Speedtest()
mb = 10**-6
# layout
sg.theme('Reddit')
layout = [
    [sg.Button('Testar')],
    [sg.Output(size=(40, 10))]
]
# Janela
janela = sg.Window('Testando Velocidade', layout)
#Extrair dados da tela

# Eventos
while True:
    janela.read()
    print('Testando Velocidade...')
    print('Velocidade de Download: ', st.download()) #Velocidade de Download
    print('Velocidade de Upload: ', st.upload()) #Velocidade de Upload
    print('Teste Finalizado !!')