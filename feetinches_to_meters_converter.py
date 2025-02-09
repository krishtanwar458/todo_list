import FreeSimpleGUI as fg
from convertor import feetinches_to_meters 

label1 = fg.Text('Enter feet')
input1 = fg.Input(key='feet')

label2 = fg.Text('Enter inches')
input2 = fg.Input(key='inches')

convert = fg.Button('Convert')
output = fg.Text(key='output')

window = fg.Window('Converter', layout=[[label1, input1], [label2, input2], [convert, output]])

while True:
    name, dictionary = window.read()
    feet = dictionary['feet']
    inches = dictionary['inches']
    meter = feetinches_to_meters(feet, inches)
    window['output'].update(value=f'{meter} m')

    match name:
        case fg.WIN_CLOSED:
            break
window.close()