def get_average():
    with open('/Users/krishtanwar/Desktop/Python/app/files/data.txt', 'r') as file_local:
        temp_local = file_local.readlines()
        list = temp_local[1:]

    sum = 0
    for i in list:
        i = i.strip('\n')
        i = float(i)
        sum = i + sum

    average = sum/len(list)
    return average

average = get_average()
#print(average)

def strength(password):
    if len(password) > 8:
        truth.append(True)

    upper = False
    for i in password:
        if i.isupper():
            upper = True
    truth.append(upper)

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    truth.append(digit)

#password = input('Type in a password: ')
truth = []

#strength(password)

def greeting(name):
    return print(f'Hi {name}')

#greeting(name = 'Andy')

def longestCommonPrefix(strs):
    #small_lists = [[word] for word in strs]
    #print(small_lists)
    for i in strs:
        k = (len(i))
        for index, j in enumerate(i):
            print(index+1, j)


#longestCommonPrefix(['flower', 'flow'])

import FreeSimpleGUI as sg
 
 
def km_to_miles(km):
    return float(km) / 1.6
 
 
label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")
 
output = sg.Text(key="output")
 
 
window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))
 
while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = values["kms"]
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break
 
window.close()