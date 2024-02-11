import PySimpleGUI as sg

def create_btn(text,col,tCol):
    return sg.Button(text,size=(3, 3), expand_x = True, font=('Helvetica',12),button_color=(tCol,col))

def perform_operation(op, v1, v2):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 / v2 if v2 != 0 else 'Error'


display = sg.InputText(size=(15,5),justification='right',
                       default_text='',readonly=False,
                       key='DISPLAY',expand_x = True,
                       background_color='white',
                       font=('Helvetica',24))
display2 = sg.InputText(size=(19,3),justification='right',
                       default_text='',readonly=True,
                       key='DISPLAY2',expand_x = True,
                       background_color='white',
                       font=('Helvetica',18))

add = create_btn('+','orange','white')
sub = create_btn('-','orange','white')
multiply = create_btn('*','orange','white')
divide = create_btn('/','orange','white')
clear = create_btn('C','white','black')

One = create_btn('1','white','black')
Two = create_btn('2','white','black')
Three = create_btn('3','white','black')
Four = create_btn('4','white','black')
Five = create_btn('5','white','black')
Six = create_btn('6','white','black')
Seven = create_btn('7','white','black')
Eight = create_btn('8','white','black')
Nine = create_btn('9','white','black')
Zero = create_btn('0','white','black')

Pos_Neg = create_btn('(-)','white','black')
Comma = create_btn('.','white','black')
Equals = create_btn('=','black','white')

window=sg.Window(title='Calculator',
                 layout=[[display],
                         [display2],
                         [One, Two, Three, add],
                         [Four, Five, Six, sub],
                         [Seven, Eight, Nine, multiply],
                         [Pos_Neg, Zero, Comma, divide],
                         [Equals, clear]],
                 size=(400, 530))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Hanterar värdeändringar
    if event in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','.']:
        current_text = values['DISPLAY']
        new_text = current_text + event
        window['DISPLAY'].update(new_text)

    # Hantera växling mellan positivt och negativt tal
    elif event == '(-)':
        current_text = values['DISPLAY']
        window['DISPLAY'].update(current_text[1:] if current_text.startswith('-') else '-' + current_text)

    # Hantera rensningsknappen
    elif event == 'C':
        window['DISPLAY'].update('')
        window['DISPLAY2'].update('')

    # Hantera operatorerna och likamedstecknet
    elif event in ['+', '-', '*', '/']:
        if values['DISPLAY']:
            value1 = float(values['DISPLAY'])
            operator = event
            window['DISPLAY'].update('')
            window['DISPLAY2'].update(f"{value1} {operator}")

    elif event == '=':
        if values['DISPLAY'] and value1 is not None:
            value2 = float(values['DISPLAY'])
            result = perform_operation(operator, value1, value2)
            window['DISPLAY'].update(result)
            window['DISPLAY2'].update(f'{value1}{operator}{value2}')
            value1 = None  # Återställ för nästa beräkning
            value2 = None