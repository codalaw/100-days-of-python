print("Welcome to the movie theater!")

age = int(input("How old are you?"))
parent = input.lower()("Are you with a parent? (yes/no): ")

if age >= 18: 
    print("You may enter")
elif age in range(13, 18)  and parent == "yes":
    print("You may enter")
else:
    print("You may not enter")
