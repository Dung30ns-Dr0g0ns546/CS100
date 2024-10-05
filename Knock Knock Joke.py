# Create variable name
# Ask "Enter your name" -> put in name
name = input("Enter your name: ")

# Ask if they want to hear a knock knock joke -> question
question = input(f"Hello " {name} "! Would you like to hear a knock knock joke?")

if question == "yes":
    print("Alright alright alright!")
else:
    print("awww, ok. Have a good day then.")
    
    response = input ("Knock Knock... ")
    if response.upper() == "WHO'S THERE?":
        response2 = input("Never gonna… ")
    else:
        print("You were supposed to say who's there")
        
    if response2.upper() == "NEVER GONNA WHAT?":
             print("Never Gonna Give You Up, Never Gonna Let You Down, Never Gonna Run Around And Hurt You!")
    else:
             print("If you didn’t want to hear the joke, you could’ve just said no earlier…")
