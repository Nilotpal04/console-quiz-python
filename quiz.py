print("Welcome to the quiz game: ")
name = input("What is your name: ")
print("Hello " + name)
us1 = "sam altman"
us2 = "microsoft"
us3 = "mojang"
cout = 0
try:
 print("Who is the CEO of OpenAI: ")
 ans1 = input("Your answer here: ")
 print("Who owns linkedIn: ")
 ans2 = input("Your answer here: ")
 print("Which game studio runs minecraft: ")
 ans3 = input("Your answer here: ")

 if us1 == ans1.lower():
    cout += 1
 if us2 == ans2.lower():
    cout += 1
 if us3 == ans3.lower():
    cout += 1
 else:
     cout = 0
 print(f"you have scored: {cout}")
 if cout == 3:
     print("Congratulations " +  name + ", you have scored the most.")
 elif cout == 2:
     print("You will won next time for sure.")
 elif cout == 1:
     print("keep the good work up.")
 else:
     print("You have lost the game, better luck next time!")
except ValueError:
    print("You are supposed to give an string")