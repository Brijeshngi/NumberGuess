import random
import math

lower = int(input("Enter the starting range value")) # taking input for lower bound.

upper = int(input("Enter the final range value")) # taking input for upper bound.

x = random.randint(lower, upper)    # taking x as variable to store random integer
									# generated by random function

print("\n\tYou have only ",
	round(math.log(upper - lower + 1, 2)),    # creating the number of chances
	  " chances to guess the integer!\n")	  # that user can input the number to guess
											  # the round function used to calculate the exact number of times.


count = 0										# taking count is equal to zero

while count < math.log(upper - lower + 1, 2):	# here 0 < that number of guesses
	count = count + 1
	guess = int(input("Guess a number "))		#number entered here to guess
	if x == guess:								# if guessed number equals to random number generated.
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:								# guessing number
		print("You Guessed too high!")

if count >= math.log(upper - lower + 1, 2):		# here count is getting greater than the calculated number of guess.
	print("\nThe number is %d" % x)				#if greater than print the number which is generated by randon function.
	print("\tBetter Luck Next time!")

