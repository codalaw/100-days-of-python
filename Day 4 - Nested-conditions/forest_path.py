print("welcome to the Enchanted Forest!")

while True:
    forest_answer = input("Do you want to enter the forest? (yes/no): ").strip().lower()

    if forest_answer == "yes":
        print("You enter the dark forest")
        while True:
            adventure_route_2 = input(
                "You come to a fork in the road. "
                "One path leads to a river, and the other to a mountain. "
                "Which do you choose? (river/mountain/leave): "
            ).strip().lower()
    
            if adventure_route_2 == "river":
                print("You found a peaceful waterfall!")                   
                break
            elif adventure_route_2 == "mountain":
                print("You encountered a sleeping dragon!")
                break
            elif adventure_route_2 == "leave":
                print("You left the enchanted forest.")
                break
            else:
                print("Invalid choice! Please pick river, mountain, or leave.")
        break
    elif forest_answer == "no":
        print("You decided to stay home. Adventure over!")
        break
    else:
        print("Please enter yes or no.")
        continue
    

