from random import randint
num = randint(1,10)
run = True
guess = 0
while run == True and guess<=3:
    userGuess =int(input("what is your guess?"))
    guess+=1
    if userGuess > num:
        print("too high")
    elif userGuess < num:
        print("too low")
    elif userGuess == num:
        print("correct!")
        run = False