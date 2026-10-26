grade = int(input("What grade did you recieve?"))

if grade > 100:
    print("invalid grade, highest score is 100")
elif grade < 0:
    print("Invalid grade, lowest score is '0'") 
elif grade == 100:
    print("a perfect score!")
    print("You scored an 'A'!")
elif grade >= 90:
    print("You scored an 'A'!")
elif grade >= 80:
    print("You scored a 'B'!")
elif grade >= 70:
    print("you scored a 'C'!")
elif grade >= 60:
    print("You scored a 'D', better luck next time!")
else:
    print("You scored an 'F'!")
    print("Please see me after class.")
