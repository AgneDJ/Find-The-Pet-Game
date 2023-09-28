import os
import random
import time

def pet():
    '''Creates a random pet (cat, dog or other) every new game'''   
    return random.choice(["🐈","🪳","🐕","🐩","🐁","🦜","🐇","🐟"])


def greeting():
    '''This function prints greeting for the user'''
    human_name = random.choice(["Steve", "Alice", "Robert", "Julia", "Kyle", "Emily" ])

    def printing_greeting(text,t_sleep=1):
        print(text)
        time.sleep(t_sleep)
        print()
        os.system("clear")

    def greet_with_inpt(text):
        print(text)
        user_input = input(">")
        return user_input
        
    os.system('clear')

    printing_greeting(f"Hello. I am {human_name}")
    user_name = greet_with_inpt("What is your name?").title()
    printing_greeting(f"Hello dear, {user_name}")
    printing_greeting("I've lost my pet...")
    user_answer = greet_with_inpt("Please, help me find it... y/n")
    if user_answer == "y":
        printing_greeting("Great! Let's go!")
        printing_greeting("Guide me by entering letters: u - up, d - down, r - right, l - left",2)
        print("loading game...")
    else:
        print("Sorry to bother you... Have a nice day...")
        exit()
    return user_name 


def human():
    '''Creates human figure'''
    print ("🧍", end="")


def block():
    '''Creates an enemy figure'''
    print("🔲", end="")


def human_coord():
    '''Generates human coordinates on the board'''
    return {
        "y": 15, 
        "x": 5
    }


def pet_coord():
    '''Generates pet coordinates on the board'''
    return {
        "y": random.randint(2,15),
        "x": random.randint(51,61)
    }


def block_coord():
    '''Generates evil block coordinates on the board'''
    return {
        "y": random.randint(1,17), 
        "x": random.randint(12,50)
    }            
   

def list_of_blocks(a):
    '''Generates the whole list of blocks coordinates'''
    blocks = []
    for i in range(a):
        blocks.append(block_coord())

    return blocks


def try_print_block(x,y):
    '''Checks if blocks are being printed'''
    for bl in group_of_blocks:
        if bl["x"] == x and bl["y"] == y:
            block()
            return True
    return False


def gameboard_print(rnd_pet):
    '''Printing a gameboard'''
    for y in range(-1,18):
        for x in range(-1,66):
          if human_coordinates["x"] == x and human_coordinates["y"] == y:
            human()
          elif x == -1:
            print("|", end="")       
          elif y == -1 or y == 17:
            print("-", end="") 
          elif pet_coordinates["x"] == x and pet_coordinates["y"] == y:
            print(rnd_pet, end="")
          elif try_print_block(x,y): 
            pass
          else:
            print(" ", end="")
        print("")


def control():
    '''Handles user input to control human place'''
    human_move = input("Where should I go now? ").lower()
  
    x, y = human_coordinates["x"], human_coordinates["y"]
    print(human_move)
    if human_move == "left" or human_move == "l":
        if x > 0:
            human_coordinates["x"] = x-1
    elif human_move== "right" or human_move == "r":
        if x < 65:
            human_coordinates["x"] = x+1
    elif human_move == "up" or human_move == "u":
        if y > 0:
            human_coordinates["y"] = y-1
    elif human_move== "down" or human_move == "d":
        if y < 16:
            human_coordinates["y"] = y+1
    elif human_move == "quit" or human_move == "q":
        os.system('clear')
        print("Goodbye!")
        exit()   
    else:
        print("Wrong instruction. Try again.")
        time.sleep(1)
        return
    
    moving_block()


def moving_block():
    '''Handles enemy block movement based of human movement'''
    for bl in group_of_blocks:
        x, y  = bl["x"], bl["y"]
        if human_coordinates["x"] > x:
            bl["x"] = x+1
        elif human_coordinates["x"] < x:
            bl["x"] = x-1
        elif human_coordinates["y"] > y:
            bl["y"] = y+1
        elif human_coordinates["y"] < y:
            bl["y"] = y-1


def check_for_end(user_nm):
    '''Checks if level or game end'''
    global group_of_blocks
    for bl in group_of_blocks:
        if human_coordinates["x"] == bl["x"] and human_coordinates["y"] == bl["y"]:
            print(f"You lose {user_nm}...")
            print("Play again? y/n")
            return True
        elif human_coordinates["x"] == pet_coordinates["x"] and human_coordinates["y"] == pet_coordinates["y"]:
            group_of_blocks = list_of_blocks(len(group_of_blocks)+1)
            print(f"You win, {user_nm}!")
            print("Next level? y/n")
            return True
    return False


def the_game():
    '''Starts the game'''
    user_name = greeting()
    random_pet = pet()
    while True:
        time.sleep(2)
        os.system('clear')
        random_pet = pet()
    
        while True:
            gameboard_print(random_pet)
            print("|  l - left     |   u - up       |  r - right    |   d - down     |")
            print("")
            control()
            os.system('clear')
            if check_for_end(user_name):
                break        
        
        new_random_pet = pet()
        random_pet = new_random_pet
        human_coordinates["x"] = random.randint(1,15)
        human_coordinates["y"] = random.randint(1,15)
        user_answer2 = input()
        if user_answer2 == "n":
          print(f"Sad to see you go, {user_name}...")
          break



human_coordinates = human_coord()
pet_coordinates = pet_coord()
block_coordinates = block_coord()
group_of_blocks = list_of_blocks(1)
the_game()