import PySimpleGUI as sg

def func(message):
    print(message)

layout = [[sg.Button('1'), sg.Button('2'), sg.Exit()] ]

window = sg.Window('ORIGINAL').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == '1':
        func('Pressed button 1')
    elif event == '2':
        func('Pressed button 2')
window.Close()