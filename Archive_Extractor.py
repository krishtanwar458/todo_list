import FreeSimpleGUI as sg
from archive_extractor_function import extract_archive

sg.theme('LightBlue7')
label1 = sg.Text('Select Archive: ')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='choose')

label2 = sg.Text('Select Destination' + '\n' 'Folder: ')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

extract_button = sg.Button('Extract')
output = sg.Text('', key='output')
exit_button = sg.Button('Exit')


window = sg.Window('Archive Extractor', layout=[[label1, input1, choose_button1], 
                                                [label2, input2, choose_button2], 
                                                [extract_button, exit_button, output]])

while True:
    event, values = window.read()
    match event:
        case 'Extract':
            archive_filepath = values['choose']
            destination_filepath = values['folder']
            extract_archive(archive_filepath, destination_filepath)
            window['output'].update(value='Extraction Completed!')
        case 'Exit':
            break
window.close()