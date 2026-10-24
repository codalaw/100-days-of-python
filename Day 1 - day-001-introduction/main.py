
import time
name = ""
age = ""
location = ""
hobby = ""

print("Welcome to the introduction generator, I will ask you a series of questions and generate an introduction!")
name = input("What is your name? ")
print(f"Hello {name},it's nice to meet you!")
age = input(f"How old are you {name}? ")
location = input("Nice! If you don't mind me asking, what city do you live in? ")
print(f"{location}! I have never been there, it must be nice!")
hobby = input(f"{name}, what is one of your favorite hobbies? ")
print(" Thats a cool hobby! I am generating your personalized contact card!")
for i in range(3):
    time.sleep(1)
    print("...")
print(f"Your name is {name}. You are {age}. You currently live in the lovely city of {location}. In your free time, you love to {hobby}")
print("You seem like a really cool person! <3")