
import random

print ("Rock-Paper-Scissors Game!\n")
picks = ["rock", "paper", "scissors"]
your_pick = picks.index (input("Enter your pick:"))  #value from variable "picks" converted to int for the index

computer_pick = random.randint (0,2)  
print ("\nComputer Picks: " + picks[computer_pick])

 
if your_pick == 0 and computer_pick == 1 or your_pick == 1 and computer_pick == 2 or your_pick == 2 and computer_pick == 0:
	print ("You Lose!")
elif your_pick == 1 and computer_pick == 0 or your_pick == 2 and computer_pick == 1 or your_pick == 0 and computer_pick == 2:
	print ("You Win!")
else:
	print ("It's a TIE!")

# For Improvements: able to accept the inputs even if it has a uppercase letter.
# place a limit of wins between player to declare the final loser.