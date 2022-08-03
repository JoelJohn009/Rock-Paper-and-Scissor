import random

def game(computer, my):
    if computer == my:
        return None
    elif computer == 'r':
        if my == 's':
            return False
        elif my == 'p':
            return True
    elif computer == 'p':
        if my == 's':
            return True
        elif my == 'r':
            return False
    elif computer == 's':
        if my == 'r':
            return True
        elif my == 'p':
            return False


print("Computer's turn: Rock(r) , Paper(p) or Scissor(s)?")
number = random.randint(1,3)
if number == 1:
    computer = 'r'

elif number == 2:
    computer = 'p'

elif number == 3:
    computer = "s"


my = input("Your turn: Rock(r) , Paper(p) or Scissor(s)?")

print(f"Computer chose {computer}")
print(f"You chose {my}")


a = game(computer, my)
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You have Lost! Try again.")