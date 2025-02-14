import FreeSimpleGUI as fg
from convertor import feetinches_to_meters 

fg.theme('Black')

label1 = fg.Text('Enter feet')
input1 = fg.Input(key='feet')

label2 = fg.Text('Enter inches')
input2 = fg.Input(key='inches')

convert = fg.Button('Convert')
output = fg.Text(key='output')
exit_button = fg.Button('Exit')

window = fg.Window('Converter', layout=[[label1, input1], [label2, input2], [convert, exit_button, output]])

while True:
    name, dictionary = window.read()
    match name:
        case 'Convert':
            feet = dictionary['feet']
            inches = dictionary['inches']
            meter = feetinches_to_meters(feet, inches)
            window['output'].update(value=f'{meter} m')
        case 'Exit':
            break

window.close()