import json 
with open('app/questions.json', 'r') as file:
    content = file.read()


data = json.loads(content)

score = 0
for question in data:
    print(question["Question"])
    for index, options in enumerate(question["Options"]):
        print(f'{index + 1}. {options}')
    answer  = int(input('Enter your answer: '))
    if answer == question["Correct_Answer"]:
        print('Correct')
    else: 
        print('Incorrect')
    question["User_Choice"] = answer
    if question["User_Choice"] == question["Correct_Answer"]:
        score = score + 1
    
for index, question in enumerate(data):
    message = f'Question {index + 1}. Your Answer - {question["User_Choice"]}, Correct Answer - {question["Correct_Answer"]}'
    print(message)

print(f'{score}/{len(data)}')
    