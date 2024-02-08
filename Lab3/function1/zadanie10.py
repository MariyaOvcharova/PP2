import random 

num = random.randrange(0, 21)
print('Hello! What is your name?')
name = input()

print('')

print('Well,', name, 'I am thinking of a number between 1 and 20.')
print('Take a guess.')

c = 1

while True:

    num1 = int(input())
    print("")
    
    if num > num1:
        print("Your guess is too low.")

    elif num < num1:
        print("Your guess is too big.")

    elif num == num1:
        print('Good job,', name, '! You guessed my number in ', c ,' guesses!') 
        break
    c += 1
    