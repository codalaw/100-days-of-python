
import time

# Terminal colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"


def game_intro():
    print(f"{CYAN}Welcome to Adventure Island!{RESET}")
    time.sleep(2)
    print("Your mission is to find the hidden treasure.")
    time.sleep(2)
    print(f"{RED}Be careful! Every decision has consequences.{RESET}")
    time.sleep(2)

    for i in range(3):
        time.sleep(0.5)
        print("...")


def story_element1():
    print("Your player has arrived on Adventure Island.")
    time.sleep(2)
    print("After walking through the jungle, you reach a crossroads.")
    time.sleep(2)
    print("One path leads toward a mysterious lake. The other leads to a dangerous cliff.")
    time.sleep(2)
    print("You must choose...")


def crossroads():
    while True:
        choice = input("Do you choose the lake or the mountain? ").strip().lower()

        if choice == "lake":
            print(f"{GREEN}You safely arrive at a mysterious lake.{RESET}")
            return True

        elif choice == "mountain":
            print(f"{RED}You fell off a cliff! Game Over.{RESET}")
            return False

        else:
            print("Invalid option. Choose lake or mountain.")


def story_element2():
    print("You have survived the crossroads and arrived at the lake.")
    time.sleep(2)
    print("There's an island in the middle of the water. You can see something shining in the distance. There is an old dishevelled boat on the shore")
    time.sleep(2)
    print("How do you get across?")


def lake_crossing():
    while True:
        choice = input("Do you swim across the lake, or do you take the boat? ").strip().lower()

        if choice == "swim":
            print(f"{RED}You were attacked by a deadly lake fish. Game Over!{RESET}")
            return False

        elif choice == "boat":
            print(f"{GREEN}You trust the old boat and paddle across the lake, reaching the opposite shore just in time!{RESET}")
            return True

        else:
            print("Invalid option. Choose swim or take the boat.")


def story_element3():
    print("You have crossed the lake and reached a mysterious stone temple.")
    time.sleep(2)
    print("Inside are three doors.")
    time.sleep(1)
    print(f"{RED}Red{RESET}")
    time.sleep(1)
    print(f"{CYAN}Blue{RESET}")
    time.sleep(1)
    print(f"{YELLOW}Yellow{RESET}")


def treasure_room():
    while True:
        choice = input("What door do you choose? ").strip().lower()

        if choice == "red":
            print(f"{RED}You open the door and are quickly engulfed in flames! Game Over.{RESET}")
            return False

        elif choice == "blue":
            print(f"{RED}The room is full of deadly beasts! One grabs you and closes the door. Game Over.{RESET}")
            return False

        elif choice == "yellow":
            print(f"{YELLOW}Congratulations! You found the treasure! YOU WIN!{RESET}")
            return True

        else:
            print("Invalid option. Choose red, blue, or yellow.")
