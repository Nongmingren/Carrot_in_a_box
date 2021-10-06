import random
import time

description = """Carrot in a box

This is a bluffing game for two players. Each players has a box.
One box has the carrot in it. To win you must have the box with the carrot in it.

The game is very simple and silly game.

-The first player looks into their box (the second player must close their eyes during this).
-The first player then says "There is a carrot in my box" There is not a carrot in my box".
-The second player then get to decide if they want to swap boxes or not.
"""
print(description)

input("press enter to begin")

first_player = input("player 1, enter your name: ")
second_player = input("player 2, enter your name: ")

player_names = first_player.center(11) + "    " + second_player.center(11)

print()
print(player_names)
print()
print(f"{first_player}, you have a RED box in front of you")
print(f"{second_player}, you have a RED box in front of you")
print()
print(f"{first_player}, you will get to look into your box.")
print(f"{second_player}, close your eyes and don't look")
print()
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print(f"{first_player} here is the inside of your box")
print("Game start!")

if random.randint(1,2) == 1:
    carrot_in_first_box = True
else:
    carrot_in_first_box = False

if carrot_in_first_box:
    print("""
    ___Vv___             ________ 
    | ||||  |           |        |
    |  ||   |  RED BOX  |        | GOLD BOX
    |__()___|           |________|
    (carrot)    
        """)
else:
    print("""
        ________             ________ 
        |       |           |        |
        |       |  RED BOX  |        | GOLD BOX
        |_______|           |________|
         (no carrot)
            """)

print(player_names)
input("Press enter to continue")

print("\n"*100)
print(f"{first_player}, tell {second_player} to open their eyes")
input("Press enter to continue")

print()
print(f"{first_player}, say one of the following sentences too {second_player}.")
print("  1) There is a carrot in my box.")
print("  2) There is not a carrot in my box.")
print()
input("enter to continue")

print()
print(f"{second_player}, do you want to swap boxes with {first_player} ? YES/NO")
while True:
    response = input("> ").upper()
    if not (response.startswith("Y") or (response.startswith("N"))):
        print(f"{second_player}, please enter Yes or No")
    else:
        break

first_box = "RED"
second_box = "GOLD"

if response.startswith("Y"):
    carrot_in_first_box = not carrot_in_first_box
    first_box, second_box = second_box, first_box
    print(f"""HERE ARE TH TWO BOXES:
        ________             ________ 
        |  {first_box}         |   {second_box}
        |       |  BOX      |        | BOX
        |_______|           |________|
            """)
else:
    print(f"""HERE ARE TH TWO BOXES:
        ________             ________ 
        |  {first_box}         |   {second_box}
        |       |  BOX      |        | BOX
        |_______|           |________|
            """)

print(player_names)

input("Press enter to continue")
print()

if carrot_in_first_box:
    print(f"""
    ___Vv___                       ________ 
    | ||||  |                     |        |
    |  ||   | {first_box} BOX    |        | {second_box} BOX
    |__()___|                     |________|
        
        """)
else:
    print(f"""
        ________                        ___Vv___ 
        |       |                      |  ||||  |
        |       | {first_box} BOX     |   ||   | {second_box} BOX
        |_______|                      |___()___|
            
            """)

print(player_names)

if carrot_in_first_box:
    print(f"{first_player} is the winner")
else:
    print(f"{second_player} is the winner")
