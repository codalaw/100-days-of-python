
import functions as game

game.game_intro()
game.story_element1()

if game.crossroads():
    game.story_element2()

    if game.lake_crossing():
        game.story_element3()

        if game.treasure_room():
            print("Congratulations! You completed Adventure Island!")
