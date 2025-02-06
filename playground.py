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
