def get_players_damage(player_one_attack_damage: int, player_two_attack_damage: int, player_one_health: int, player_two_health: int) -> bool:
    if player_one_attack_damage > 1:
        player_two_health -= player_one_attack_damage
    
    if player_two_attack_damage > 1:
        player_one_health -= player_two_attack_damage

    return player_one_health, player_two_health

def display_intro() -> None:
    print("Hello trainer! Welcome to Pokemon Battles!")
    help = ""
    while help != "yes" and help != "no": 
        help = input("Do you already know how to play Pokemon Battles? (yes or no)\n")
        if help == "no":
            print("""\nNo worries! In Pokemon Battles, you will battle another player using pokemon which are funny looking animals. 
To win the game, you have to knock out all of your opponent's pokemon using a bunch of different attacks.
          """)
        if help == "yes":
            print("\nGreat, let's begin.")

    print("Before we start, what is your name?\n")
    player_one = input()
    print(f"Welcome {player_one}! You will be player one. \n")

    print("Hello another trainer!")
    player_two = input("What is your name?\n")
    print(f"Welcome {player_two}! You will be player two \n")

    
    return player_one, player_two

def display_player_one_control_screen(player_one: str, player_one_pokemon_name: str, player_two_health: int) -> int:
    pokemon_total_health_points = 50
    player_one_action = ""
    player_one_attack = ""
    player_one_attack_damage = 0
    
    while player_one_action != "1":
        print(f"""
-----------------------------------------
Player: {player_one}
Pokemon: {player_one_pokemon_name} {player_one_health}/{pokemon_total_health_points} health points

1 - Attacks
-----------------------------------------
          """)
        player_one_action = input()
    
    if player_one_action == "1":
        if player_one_pokemon_name == "charmanzar":
            
            fire_breath = [
                "Fire Breath", 4                
            ]

            fire_slam = [
                "Fire Slam", 5
            ]
            
            inferno = [
                "Inferno", 7
            ]
                
            print(f"""
-----------------------------------------
Attacks  {player_one_pokemon_name} - {player_one_health}/{pokemon_total_health_points}
                  
1 - Fire Breath - 4 damage
2 - Fire Slam - 5 damage
3 - Inferno - 7 damage
-----------------------------------------
                  """)
            
            player_one_action = input()
            if player_one_action == "1":
                player_one_attack, player_one_attack_damage = fire_breath
                player_two_health -= player_one_attack_damage
            elif player_one_action == "2":
                player_one_attack, player_one_attack_damage = fire_slam
                player_two_health -= player_one_attack_damage
            elif player_one_action == "3":
                player_one_attack, player_one_attack_damage = inferno
                player_two_health -= player_one_attack_damage
            
        if player_one_pokemon_name == "squirt":
            
            water_blast = [
                "Water Blast", 4
            ]

            water_bomb = [
                "Water Bomb", 5
            ]

            typhoon = [
                "Typhoon", 7
            ]

            print(f"""
-----------------------------------------
Attacks  {player_one_pokemon_name} - {player_one_health}/{pokemon_total_health_points}

1 - Water Blast - 4 damage
2 - Water Bomb - 5 damage
3 - Typhoon - 7 damage
-----------------------------------------   
              """)
            player_one_action = input()
            if player_one_action == "1":
                player_one_attack, player_one_attack_damage = water_blast
                player_two_health -= player_one_attack_damage
            elif player_one_action == "2":
                player_one_attack, player_one_attack_damage = water_bomb
                player_two_health -= player_one_attack_damage
            elif player_one_action == "3":
                player_one_attack, player_one_attack_damage = typhoon
                player_two_health -= player_one_attack_damage

        if player_one_pokemon_name == "bulbabaur":
            
            seed_strike = [
                "Seed Strike", 4
            ]
            
            seed_bomb = [
                "Seed Bomb", 5
            ]

            overgrowth = [
                "Overgrowth", 7
            ]

            print(f"""
-----------------------------------------
Attacks  {player_one_pokemon_name} - {player_one_health}/{pokemon_total_health_points}
                  
1 - Seed Strike - 4 damage
2 - Seed Bomb - 5 damage
3 - Overgrowth - 7 damage
-----------------------------------------
                  """)
            player_one_action = input() 
            if player_one_action == "1":
                player_one_attack, player_one_attack_damage = seed_strike
                player_two_health -= player_one_attack_damage
            elif player_one_action == "2":
                player_one_attack, player_one_attack_damage = seed_bomb
                player_two_health -= player_one_attack_damage
            elif player_one_action == "3":
                player_one_attack, player_one_attack_damage = overgrowth
                player_two_health -= player_one_attack_damage

        print(f"""
-----------------------------------------
{player_one_pokemon_name} used {player_one_attack} and dealt {player_one_attack_damage} damage!
It is now {player_two_name}'s turn.
-----------------------------------------
""")
        return player_one_action, player_one_attack, player_one_attack_damage, player_two_health

def display_player_two_control_screen(player_two: str, player_two_pokemon_name: str, player_one_health: int) -> int:
    pokemon_total_health_points = 50
    player_two_action = ""
    player_two_attack = ""
    player_two_attack_damage = 0
    
    while player_two_action != "1":
        print(f"""
-----------------------------------------
Player: {player_two}
Pokemon: {player_two_pokemon_name} - {player_two_health}/{pokemon_total_health_points} health points

1 - Attacks
-----------------------------------------
          """)
        player_two_action = input()
    
        if player_two_action == "1":
            if player_two_pokemon_name == "charmanzar":
            
                fire_breath = [
                    "Fire Breath", 4                
                ]

                fire_slam = [
                    "Fire Slam", 5
                ]
            
                inferno = [
                    "Inferno", 7
                ]

                print(f"""
-----------------------------------------
Attacks  {player_two_pokemon_name} - {player_two_health}/{pokemon_total_health_points}
                  
1 - Fire Breath - 4 damage
2 - Fire Slam - 5 damage
3 - Inferno - 7 damage
-----------------------------------------
                  """)
                player_two_action = input()
            
                if player_two_action == "1":
                    player_two_attack, player_two_attack_damage = fire_breath
                    player_one_health -= player_two_attack_damage
                elif player_two_action == "2":
                    player_two_attack, player_two_attack_damage = fire_slam
                    player_one_health -= player_two_attack_damage
                elif player_two_action == "3":
                    player_two_attack, player_two_attack_damage = inferno
                    player_one_health -= player_two_attack_damage
            
            if player_two_pokemon_name == "squirt":
            
                water_blast = [
                    "Water Blast", 4
                ]

                water_bomb = [
                    "Water Bomb", 5
                ]

                typhoon = [
                    "Typhoon", 7
                ]

                print(f"""
-----------------------------------------
Attacks  {player_two_pokemon_name} - {player_two_health}/{pokemon_total_health_points}

1 - Water Blast - 4 damage
2 - Water Bomb - 5 damage
3 - Typhoon - 7 damage
-----------------------------------------   
              """)
                player_two_action = input()
            
                if player_two_action == "1":
                    player_two_attack, player_two_attack_damage = water_blast
                    player_one_health -= player_two_attack_damage
                elif player_two_action == "2":
                    player_two_attack, player_two_attack_damage = water_bomb
                    player_one_health -= player_two_attack_damage
                elif player_two_action == "3":
                    player_two_attack, player_two_attack_damage = typhoon
                    player_one_health -= player_two_attack_damage

            if player_two_pokemon_name == "bulbabaur":
            
                seed_strike = [
                    "Seed Strike", 4
                ]
            
                seed_bomb = [
                    "Seed Bomb", 5
                ] 

                overgrowth = [
                    "Overgrowth", 7
                ]

                print(f"""
-----------------------------------------
Attacks  {player_two_pokemon_name} - {player_two_health}/{pokemon_total_health_points}
                  
1 - Seed Strike - 4 damage
2 - Seed Bomb - 5 damage
3 - Overgrowth - 7 damage
-----------------------------------------
                  """)
                player_two_action = input()
            
                if player_two_action == "1":
                    player_two_attack, player_two_attack_damage = seed_strike
                    player_one_health -= player_two_attack_damage
                elif player_two_action == "2":
                    player_two_attack, player_two_attack_damage = seed_bomb
                    player_one_health -= player_two_attack_damage
                elif player_two_action == "3":
                    player_two_attack, player_two_attack_damage = overgrowth
                    player_one_health -= player_two_attack_damage
            
        print(f"""
-----------------------------------------
{player_two_pokemon_name} used {player_two_attack} and dealt {player_two_attack_damage} damage!
It is now {player_one_name}'s turn.
-----------------------------------------
              
              """)
        return player_two_action, player_two_attack, player_two_attack_damage, player_one_health

def get_player_pokemon(player_one: str, player_two: str) -> str:
    player_one_pokemon = ""
    player_two_pokemon = ""
    
    
    print("Each of you will get 3 different pokemon. They are Charmanzar, Squirtle, and Bulbabaur")
    
    print(f"""Hello {player_one}. Which pokemon would you like to call on first? (1-3)

1 - Charmanzar
2 - Squirt
3 - Bulbabaur""")
    player_one_pokemon = input()

    while not is_valid_input(player_one_pokemon, player_two_pokemon):
        print(f"""Hello {player_one}. Which pokemon would you like to call on first? (1-3)

1 - Charmanzar
2 - Squirt
3 - Bulbabaur""")
        player_one_pokemon = input()

    print(f"""Hello {player_two}. Which pokemon would you like to call on first? (1-3)

1 - Charmanzar
2 - Squirt
3 - Bulbabaur""")
    player_two_pokemon = input()

    while not is_valid_input(player_one_pokemon, player_two_pokemon):
        print(f"""Hello {player_two}. Which pokemon would you like to call on first? (1-3)

1 - Charmanzar
2 - Squirt
3 - Bulbabaur""")
        player_two_pokemon = input()

    print(f"{player_one} will go first.")

    return player_one_pokemon, player_two_pokemon

def get_pokemon_name(player_one_pokemon: str, player_two_pokemon: str) -> str:
    player_one_pokemon_name = ""
    player_two_pokemon_name = ""
    #pokemon_names = [
    #    "Charmanzar",
    #    "Squirt",
    #    "Bulbabaur"
    #]

    #for pokemon_num_type in range(3):
    #    if player_one_pokemon == pokemon_num_type:
    #        player_one_pokemon = pokemon_names[pokemon_num_type]

    if player_one_pokemon == "1":
        player_one_pokemon_name = "charmanzar"
    elif player_one_pokemon == "2":
        player_one_pokemon_name = "squirt"
    elif player_one_pokemon == "3":
        player_one_pokemon_name = "bulbabaur"
    if player_two_pokemon == "1":
        player_two_pokemon_name = "charmanzar"
    elif player_two_pokemon == "2":
        player_two_pokemon_name = "squirt"
    elif player_two_pokemon == "3":
        player_two_pokemon_name = "bulbabaur"

    return player_one_pokemon_name, player_two_pokemon_name  

def get_winner(player_one_health: int, player_two_health: int):
    game_over = False
    if player_one_health <= 0:
        game_over = True
        print(f"{player_one_pokemon_name} has fainted. {player_two_name} wins!")
    elif player_two_health <= 0:
        game_over = True
        print(f"{player_two_pokemon_name} has fainted. {player_one_name} wins!")

    return game_over

def is_valid_input(player_one_pokemon: str, player_two_pokemon: str) -> bool:
    if not player_one_pokemon in "123":
        print("Invalid input. Please only enter 1, 2, or 3")
        return False
    
    if not player_two_pokemon in "123":
        print("Invalid input. Please only enter 1, 2, or 3")
        return False
    
    return True

game_over = False

play_again = "y"

while play_again.startswith("y"):
    player_one_name, player_two_name = display_intro()
    player_one_health = 50
    player_two_health = 50
    player_one_pokemon, player_two_pokemon = get_player_pokemon(player_one_name, player_two_name)
    player_one_pokemon_name, player_two_pokemon_name = get_pokemon_name(player_one_pokemon, player_two_pokemon)
    while not get_winner(player_one_health, player_two_health):
        player_one_action, player_one_attack, player_one_attack_damage, player_two_health = display_player_one_control_screen(player_one_name, player_one_pokemon_name, player_two_health)
        player_two_action, player_two_attack, player_two_attack_damage, player_one_health = display_player_two_control_screen(player_two_name, player_two_pokemon_name, player_one_health)

    print("Would you like to play again?")
    play_again = input().lower()

