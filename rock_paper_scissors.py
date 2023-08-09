import random

#Rock,Paper,Scissors Game

print("================================\nRock Paper Scissors\n================================")


player = int(input("1)✊ (Rock).\n2)✋ (Paper)\n3)✌️  (Scissors)\nPick a number:  "))

computer = random.randint(1,3)

print("")

if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")
else:
    print("Try again.")


if computer == 1:
    print("AI Chose: ✊")
elif computer == 2:
    print("AI Chose: ✋")
elif computer == 3:
    print("AI Chose: ✌️")
else:
    print("Try again.")


if player == 1 and computer == 1:
    print("It's a draw.")
elif player == 2 and computer == 2:
    print("It's a draw.")
elif player == 3 and computer == 3:
    print("It's a draw.")
elif player == 1 and computer == 2:
    print("AI won.")
elif player == 2 and computer == 3:
    print("AI won.")
elif player == 3 and computer == 1:
    print("AI won.")
elif player == 1 and computer == 3:
    print("You won!")
elif player == 2 and computer == 1:
    print("You won!")
elif player == 3 and computer == 2:
    print("You won!")
else:
    print("ENd game now")



