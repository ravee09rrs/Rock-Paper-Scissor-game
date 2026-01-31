#Rock Paper Scessior Game

# generate random between rock paper scessior
# take input from user as rock paper scessior
# if input is equal to random
#  print draw 
# elif input is rock and random is scessior
#  print user wins 
# elif input is paper and random is rock
#  print user wins 
# elif input is scessior and random is paper
#  print user wins 
# else
#  print computer wins  
  
import random
options = ["r","p","s"]
computer = random.choice(options)

while True:
 user = input("Enter rock(r) paper(p) or scessior(s): ").lower()
 print("cpomputer choice is: ", computer)
 if user == computer:
    print("it is a draw")
 elif (user == "r" and computer == "s") or (user == "p"and computer == "r") or (user == "s" and computer == "p"):
    print("user wins") 

 else:
    print("computer wins") 