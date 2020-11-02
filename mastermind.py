import random
# resubmit with comment
""" resubmitting with comment"""

def run_game():
    """
    TODO: implement Mastermind code here
    """
    #1 - guess a code
    secret = [] 
    while len(secret) < 4: 
        n = str(random.randint(1, 8))
        if n not in secret:
            secret.append(n)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    #2- get a guess
    turns = 12
    while True and turns >0:
        guess = input("Input 4 digit code: ")
        if not guess.isdigit():
            print("Please enter exactly 4 digits.")
            continue
        if len(guess) != 4:
            print("Please enter exactly 4 digits.")
            continue
        guess = list(guess)

    #3- evaluate input

        correct_digit = 0
        correct_place = 0
        for x in range(len(secret)):
            if guess[x] == secret [x]:
                correct_place +=1
        print("Number of correct digits in correct place:     " +str(correct_place))                

        for x in range(4):
            if guess[x] in secret:
                correct_digit += 1
        correct_digit -= correct_place
        print("Number of correct digits not in correct place: " +str(correct_digit))

        if str(guess) == str(secret):
            print("Congratulations! You are a codebreaker!")
            print("The code was: " + ''.join(secret))
            break
    
    #4- count guesses
        turns -=1
        print("Turns left: " +str(turns))
            

if __name__ == "__main__":
    run_game()
 
