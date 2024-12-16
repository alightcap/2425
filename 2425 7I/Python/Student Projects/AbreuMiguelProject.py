import random
import time
play_again = True
dumbness = 0
player_hp = 100
lumerian_health = 65
lumerian = True
turn = True
status = "None"
player = True
play_again_input = ""

def crit() -> bool:
    crit_active = False
    crit_chance = random.randint(1,3)
    return crit_active, crit_chance

def fire_blast_roll() -> int:
    fire_damage = random.randint(6, 10)
    fire_effect = random.randint(1,3)
    fire_chip_damage = random.randint(1, 2)
    return fire_chip_damage, fire_damage, fire_effect

def elec_roll() -> int:
    elec_damage = random.randint(7, 9)
    elec_effect = random.randint(1,2)
    elec_stun = random.randint(1, 2)
    return elec_stun, elec_damage, elec_effect

def heal_roll() -> int:
    heal_amount = random.randint(25, 30)
    return heal_amount

def swipe_roll() -> int:
    swipe_damage = random.randint(15, 20)
    return swipe_damage

def bite_roll() -> int:
    bite_damage = random.randint(19, 23)
    return bite_damage

def battle_data(lumerian_health, status, name, player_hp) -> None:
    print(f"""
Lumerian Health {lumerian_health}/65
        Status:{status}
""")
    print(f"{name} Health {player_hp}/100 ")

def get_player_skill() -> str:
    skill = ""
    while skill != "a" and skill != "s" and skill != "d":    
        print("""
        a Fire Blast
        s Heal Self
        d Shock Hands""")
        skill = input()
    return skill

def get_enemy_skill() -> str:
    enemy_skill = ""
    enemy_skill = random.randint(1,4)
    return enemy_skill

def display_instruct() -> None:
    print("You will fight creatures")
    print("""You will fight these said creatures by
          a fire blast
          s heal
          d shock hands 

Enter the letter coressponding to the skill
________________________________""")
    
def display_intro() -> str:
    print("Welcome Survivor")
    print("What is your name")
    name = input()
    print(f""" Welcome {name} 
          
          
          
    go to the planet""")
    return name



name = display_intro()
display_instruct()
# get the player input
while play_again == True:
    while lumerian == True and player == True:
        if turn == True:
            battle_data(lumerian_health, status, name, player_hp)
            skill = get_player_skill()
            if skill == "a":
                fire_chip_damage, fire_damage, fire_effect = fire_blast_roll()
                crit_active, crit_chance = crit()
                if crit_chance == 1:
                    fire_damage = (fire_damage) * 3
                    print("You got a crit!")
                lumerian_health -= fire_damage
                print(f"You have done {fire_damage} damage")
                if fire_effect == 1:
                    status = "Burned"
                    print("""Target has been burned""")
                    lumerian_health -= fire_chip_damage
                    print(f"Target has taken {fire_chip_damage} burn damage")
            if skill == "s":
                if player_hp != 100:
                    heal_amount = heal_roll()
                    print(f"""You healed {heal_amount}""")
                    player_hp += heal_amount
                if player_hp >= 130:
                    print("Hey Stinky don't do that")
                    player_hp = 1
            if skill == "d":
                elec_stun, elec_damage, elec_effect = elec_roll()
                crit_active, crit_chance = crit()
                if crit_chance == 1:
                    elec_damage = (elec_damage) * 3
                    print("You got a crit!")
                lumerian_health -= elec_damage
                print(f"""You have done {elec_damage} damage""")
                if elec_effect == 1:
                    status = "Stunned"
                    print("""Target has been stunned
                        """)
        if lumerian_health <= 0:
            lumerian = False
        if player_hp <= 0:
            print("DEAD: Killed by lumerian")
            print("Play Again?????!?!?!?!?!?!?!?!?!?!?!?!?!?!?!")
            input()
        turn = False
        if turn == False:
            print("""Enemy turn
                """)
            enemy_skill = get_enemy_skill()
            if enemy_skill == 1:
                if status == "Stunned":
                    print("""Lumerian is to stunned to move!
                        """)
                    status = "None"
                    turn = True
                else:
                    swipe_damage = swipe_roll()
                    print(f"""Lumerian swiped dealing {swipe_damage} damage
                    """)
                    player_hp -= swipe_damage
            if enemy_skill == 2:
                if status == "Stunned":
                    print("""Lumerian is to stunned to move!
                        """)
                    status = "None"
                    turn = True
                else:
                    bite_damage = bite_roll()
                    print(f"""Lumerian swiped dealing {bite_damage} damage
                    """)
                    player_hp -= bite_damage
            turn = True
            if player_hp <= 0:
                print("DEAD: Killed by lumerian")
                print("Play Again?????!?!?!?!?!?!?!?!?!?!?!?!?!?!?!")
                play_again = input()
                if play_again == "yes":
                    player_hp = 100

    if lumerian == False:
        print("You Win")
        # play_again = False
    if player == False:
        print("Lol you lol lol you died.")
        # play_again = False

    print("Play again")
    play_again_input = input()
    while play_again_input != "yes" and play_again_input != "no":
        print("write yes or no")
        play_again_input = input()
    if play_again_input == "yes":
        lumerian = True
        player_hp = 100
        lumerian_health = 65
        status = "None"
        play_again == True
    if play_again_input == "no":
        play_again = False
play_again = ""










































































































































































































































































































































































































































































































