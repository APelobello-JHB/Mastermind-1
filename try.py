import random


secret = []
while len(secret) < 4: 
    n = random.randint(1, 8)
    if n not in secret:
        secret.append(n)
print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

guess = input("Input 4 digit code: ")
if guess.isdigit() and len(guess) is 4:
    guess =[]
    print(guess)
else: 
    print("Please enter exactly 4 digits.")



if guess == secret:
    print("Congratulations! You are a codebreaker!""\n""The code was:" +secret)
else:
    for n in guess:
        guess.index():
    print("Number of correct digits in correct place:")

    #print("Number of correct digits not in correct place:")
    #print("Wrong. Guess again.")
