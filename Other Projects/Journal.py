date = input("What is today's date? ")
mood = input('Rate your mood today (from 1 to 10): ')
thoughts = input('Let your thoughts flow: \n')

with open(f'/Users/krishtanwar/Desktop/Python/journal/{date}.txt', 'w') as file:
    file.write(mood + '\n')
    file.write(thoughts)