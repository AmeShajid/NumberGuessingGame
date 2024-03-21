#number guessing game 

#first import random so we can use the random modules
import random

#here is an example of the random feature
#r = random.randint(-5,11) the reason I used randint is beacause includes 11 randrange doesn't include 11
#print = 4

#asking the user how much they want the range
max_range = input("Top of range: ")
#making sure the number they type in more than zero and it is a number
if max_range.isdigit():#right here checks if it IS a digit
    #if is digit is true it will continue with the rest
    max_range = int(max_range)#we have to make max_range an int because when they give us an input value it is first a string so we have to convert it
    if max_range <= 0:#so after checking if the number is a digit, they have to now check if the nubmer is less than or equal to zero(we dont want negatives or 0 )
        print("Please type a nubmer large than 0 next time.")   
        quit()#we will quit the program
else:
    print("Please type a number next time.")#this is for the first if statement and if someone types a nonnumber then we will have this given to them.
    quit()#we will quit the program

random_number = random.randint(0, max_range)#right is our random number the computer will generator the 0 is the lowest number and then the highest it will go to is the number user inputs
guesses = 0
#right here we want to keep having the user guess until they get it correct
while True:
    guesses += 1 #we want to count how many times they guessed it is at the top because of the continue loop
    user_guess = input("Make a guess: ")
    if max_range.isdigit():#right here checks if it IS a digit
    #if is digit is true it will continue with the rest
        user_guess = int(user_guess)#we have to make user_guess an int because when they give us an input value it is first a string so we have to convert it
    else:
        print("Please type a number next time.")#this is for the first if statement and if someone types a nonnumber then we will have this given to them.
        continue#what continue does is bring us back to the top of so basically its a loop
    if user_guess == random_number: # now we check if our guess equals the random number
        print("You got it right!")
        break#if we get it right then we will break the program
    else: # we can also use an elif statement here to clean it up
        if user_guess > random_number:# right here it is in the else becasue we want to tell them when they get it wrong how clsoe they are to the guess to narrow down their guesses
            print("You were above the number!")
        else:
            print("You were below the number!")
print("You got it in", guesses, "guesses.")#we print the amount of guesses it took them

















