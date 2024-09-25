import random

fortunes = ["Yes", "No", "It's Likely", "It's Doubtful", "Absolutely Positive", "Not Going To Happen", "For Sure", "Never"]

# ask user for choice 1, 2 or 3
# 	1. Print all of the fortunes
# 	2. Print a specfic fortune
# 	3. Print a random fortune


print(" 1: print all the fortunes")
print(" 2: print a specific fortune")
print(" 3: print a random fortune")

# get string inout -> choice

choice = input("What will you do: 1, 2, or 3? ")
# If choice = 1
# 		show list of all fortunes

# if choice = 2
# 	ask which number to choose from
# 		number = specific fortune listed as number

# if choice = 3
# 	 randomly choose one fortune

print()

if choice == "1":
    print("Your Fortunes")
    for i, value in enumerate(fortune):
        print(f"{i}) (value)")
    
    print()

elif choice == "2":