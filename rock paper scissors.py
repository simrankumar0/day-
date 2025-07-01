from random import randint 
win = False
computer_score = 0
player_score = 0
while win == False and computer_score<3 and player_score<3:
    cp= randint (0,2)
    userimput = int(input("Pick one Rock = 0, Paper = 1, and Scissors = 2"))
    if cp == userimput:
     print("tie!")
    elif cp == 0 and userimput == 1:
     print("You win!")
     player_score +=1
    elif cp == 0 and userimput == 2:
     print("computer wins!")
     computer_score +=1
    elif cp == 1 and userimput == 0:
     print("computer wins!")
     computer_score +=1
    elif cp == 1 and userimput == 2:
      print("You win")
      player_score +=1 
    elif cp == 2 and userimput == 0:
     print("you win")
     player_score +=1
    elif cp == 2 and userimput ==1:
     print("computer wins")
     computer_score +=1
    if computer_score == 3:
        print("COMPUTER WON!")
        win = True
    elif player_score == 3:
        print("YOU WON!")
        win = True 
