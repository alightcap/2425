import random
import math
import time

#CATEGORIZE LATERRRRR

possum_sibling_moralties_and_drive_list = [

"Violence", #DOEST CARE ABOUT YOU BECASU EIS CSCARE DYOULL SNITHC HIM OUT TO OTHER POSSUM GANGS AND HE BABANDONS YOU YOU ARE VERY LIKELY TO GO DOWN MENACE TO SOCIETY PATH BUT HAVE POSSSIBLITY O FREEDEEMDE SOUL WHER EYOU  HELP EVEYRONE GAIN AN APOLOGIZE OT EVERYOEN BECUAS EYOU KIND NA DGENTEL AND NICE :) FLOWER ESUNSHIEN SMILES HEARTS AND LAUGHTER
"Wealth", # DOENST CARE JUST LIVEES OFF OF YOU S
"Food", # DOESNT CARE ABPUT YPUR JUST LIVES OFF OF YOU AND ACTAULLY MAKE YOU WEAKER

]

DEATH = False
player_first_choice_input = ""
possum_sibling_moralties_and_drive = possum_sibling_moralties_and_drive_list
choice = ""
cause_of_death = " "
eat_all = "eat all almonds"            #BELONGS WITH OPSTION OF FIRST CHOICE OF CHOICES OF FIREST LIFE OF POSSUM UNREINCARNETED.... IS A REPEATED VARIBALE  
eat_poison = eat_all
poison = eat_poison
first_choice___newbron_joey_born_in_den_chosen_choice_of_first_run_one_point_one = input() #BELONGS WITH FIRST CHOICE OF CHOICES OF FIREST LIFE OF POSSUM UNREINCARNETED 
mingle_with_sibs = "mingle with siblings"  #BELONGS WITH OPTION OF FIRST CHOICE OF CHOICES OF FIREST LIFE OF POSSUM UNREINCARNETED.... IS A REPEATED VARIBALE  
look_for_food = "look for food"            #BELONGS WITH OPTION OF FIRST CHOICE OF CHOICES OF FIREST LIFE OF POSSUM UNREINCARNETED.... IS A REPEATED VARIBALE  
play_again = True


sibling_list = [

"Offilia",
"Pita",
"Othelie",
"Stelli",
"Stevis" ,
"Usyrupla",
"Macienrie",

]

def noob_begginer_introductionary_visuals_and_wordsstuff() -> str:  # FIZ XBUG WHERE IN TERMINAL PRINTS UR_A_BOOMER_CONGRATS WITH "CONRGATS BOOMER" BEFORE ANY INTRODUCTORY TEXT Even.!!!! unimportnat n but notable 
    print("""✩♬ ₊˚.🎧⋆☾⋆⁺₊✧ """)
    time.sleep(0)
    print(""" 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠰⡁⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠙⠻⣿⣿⣿⡆⠠⠁⢠⣿⣿⣿⠟⠋⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠙⠿⣦⡄⠙⣿⣷⣶⣶⣾⣿⠋⢀⠤⠒⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⣠⣿⣿⣿⣿⣿⣿⣄⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢁⣠⡄⠈⣿⣿⣿⣿⣿⣿⠁⠠⣀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠺⠛⢉⣠⣴⣿⡟⠉⠉⢻⣿⣦⣄⡀⠉⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿1
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⡃⠠⠃⢈⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠐⠃⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⡛⠛⠛⢿⣿⣿
⣿⡟⠀⣴⣞⡷⣛⢾⢳⣛⢾⢳⡞⢷⣳⢻⢶⣛⠾⣞⡳⣞⠷⣛⢾⢳⡻⢶⣛⠾⣞⡳⢷⠾⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿
⣿⡇⠀⣷⡫⠴⣉⢦⢓⡬⣒⢣⡜⢣⢆⠳⣒⠬⡓⢦⡱⢎⠼⡑⡎⡖⣡⠳⣌⢓⠦⣙⠦⣙⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⢸⣿
⣿⣇⠀⢷⡏⡱⡍⢦⢋⡴⢃⠧⡜⢣⢎⠳⣡⠏⡼⢡⠞⣌⠧⡹⠴⡙⡴⢓⡬⢍⡺⢔⡙⢦⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢸⣿
⣿⣿⣤⣈⠁⠁⠈⠁⠉⠀⠉⠈⠈⠁⠈⠁⠁⠈⠁⠉⠈⠀⠉⠀⠉⠁⠈⠁⠈⠈⠁⠈⠉⠀⡀⠈⠉⠉⠉⠉⡋⢉⠉⢉⣁⣤⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠛⢉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⡉⠛⠻⣿
⠃⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠘
⠀⢸⣿⣿⠉⣿⣿⣿⣿⠟⠉⣉⠉⠻⣿⣿⡟⠉⠙⣿⣿⣿⠉⢉⡉⠙⢿⣿⠉⢻⡏⠙⢿⣿⣿⠉⢹⣿⠟⠋⢉⠉⠙⢿⣿⣿⣿⠀
⠀⢸⣿⣿⠀⣿⣿⣿⡏⠀⣿⣿⣿⡀⢹⣿⠀⣸⡀⢸⣿⣿⠀⣿⣿⣇⠈⣿⠀⢸⡇⢀⡈⠻⣿⠀⢸⡏⢀⣾⣿⣿⣷⣿⣿⣿⣿⠀
⠀⢸⣿⣿⠀⣿⣿⣿⡇⠐⣿⣿⣿⠀⢸⡇⠀⠛⠓⠀⢿⣿⠀⣿⣿⡇⠀⣿⠀⢸⡇⠸⣷⣄⠙⠀⢸⡇⠈⣿⣧⣤⡄⠀⣽⣿⣿⠀
⠀⢸⣿⣿⠀⠉⠉⠉⣻⣄⣈⠉⢁⣠⣿⢀⣶⣾⣶⣆⢘⣯⠀⠉⠉⣀⣼⣿⡀⣸⡇⢈⣿⣿⣦⡀⣸⣿⣦⣈⠉⢉⣀⣼⣿⣿⣿⠀
⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀
⣷⣤⣈⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⡉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⣉⣁⣤⣾""")
    time.sleep(0)
    print(""" 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠰⡁⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠙⠻⣿⣿⣿⡆⠠⠁⢠⣿⣿⣿⠟⠋⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠙⠿⣦⡄⠙⣿⣷⣶⣶⣾⣿⠋⢀⠤⠒⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⣠⣿⣿⣿⣿⣿⣿⣄⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢁⣠⡄⠈⣿⣿⣿⣿⣿⣿⠁⠠⣀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠺⠛⢉⣠⣴⣿⡟⠉⠉⢻⣿⣦⣄⡀⠉⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⡃⠠⠃⢈⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿1
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠐⠃⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⡛⠛⠛⢿⣿⣿
⣿⡟⠀⣴⣞⡷⣛⢾⢳⣛⢾⢳⡞⢷⣳⢻⢶⣛⠾⣞⡳⣞⠷⣛⢾⢳⠀⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿
⣿⡇⠀⣷⡫⠴⣉⢦⢓⡬⣒⢣⡜⢣⢆⠳⣒⠬⡓⢦⡱⢎⠼⡑⡎⡖⠀⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⢸⣿ ⢸⣿
⣿⣇⠀⢷⡏⡱⡍⢦⢋⡴⢃⠧⡜⢣⢎⠳⣡⠏⡼⢡⠞⣌⠧⡹⠴⡙⠀⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢸⣿
⣿⣿⣤⣈⠁⠁⠈⠁⠉⠀⠉⠈⠈⠁⠈⠁⠁⠈⠁⠉⠈⠀⠉⠀⠉⠁⠈⠁⠈⠈⠁⠈⠉⠀⡀⠈⠉⠉⠉⠉⡋⢉⠉⢉⣁⣤⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠛⢉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⡉⠛⠻⣿
⠃⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠘
⠀⢸⣿⣿⠉⣿⣿⣿⣿⠟⠉⣉⠉⠻⣿⣿⡟⠉⠙⣿⣿⣿⠉⢉⡉⠙⢿⣿⠉⢻⡏⠙⢿⣿⣿⠉⢹⣿⠟⠋⢉⠉⠙⢿⣿⣿⣿⠀
⠀⢸⣿⣿⠀⣿⣿⣿⡏⠀⣿⣿⣿⡀⢹⣿⠀⣸⡀⢸⣿⣿⠀⣿⣿⣇⠈⣿⠀⢸⡇⢀⡈⠻⣿⠀⢸⡏⢀⣾⣿⣿⣷⣿⣿⣿⣿⠀
⠀⢸⣿⣿⠀⣿⣿⣿⡇⠐⣿⣿⣿⠀⢸⡇⠀⠛⠓⠀⢿⣿⠀⣿⣿⡇⠀⣿⠀⢸⡇⠸⣷⣄⠙⠀⢸⡇⠈⣿⣧⣤⡄⠀⣽⣿⣿⠀
⠀⢸⣿⣿⠀⠉⠉⠉⣻⣄⣈⠉⢁⣠⣿⢀⣶⣾⣶⣆⢘⣯⠀⠉⠉⣀⣼⣿⡀⣸⡇⢈⣿⣿⣦⡀⣸⣿⣦⣈⠉⢉⣀⣼⣿⣿⣿⠀
⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀
⣷⣤⣈⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⡉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⣉⣁⣤⣾""")
    time.sleep(0)
    print(""" 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠰⡁⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠙⠻⣿⣿⣿⡆⠠⠁⢠⣿⣿⣿⠟⠋⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠙⠿⣦⡄⠙⣿⣷⣶⣶⣾⣿⠋⢀⠤⠒⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⣠⣿⣿⣿⣿⣿⣿⣄⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢁⣠⡄⠈⣿⣿⣿⣿⣿⣿⠁⠠⣀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠺⠛⢉⣠⣴⣿⡟⠉⠉⢻⣿⣦⣄⡀⠉⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⡃⠠⠃⢈⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿1
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠐⠃⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⡛⠛⠛⢿⣿⣿
⣿⡟⠀⣴⣞⡷⣛⢾⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿
⣿⡇⠀⣷⡫⠴⣉⢦⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⢸⣿ ⢸⣿
⣿⣇⠀⢷⡏⡱⡍⢦⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢸⣿
⣿⣿⣤⣈⠁⠁⠈⠁⠉⠀⠉⠈⠈⠁⠈⠁⠁⠈⠁⠉⠈⠀⠉⠀⠉⠁⠈⠁⠈⠈⠁⠈⠉⠀⡀⠈⠉⠉⠉⠉⡋⢉⠉⢉⣁⣤⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠛⢉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⡉⠛⠻⣿
⠃⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠘
⠀⢸⣿⣿⠉⣿⣿⣿⣿⠟⠉⣉⠉⠻⣿⣿⡟⠉⠙⣿⣿⣿⠉⢉⡉⠙⢿⣿⠉⢻⡏⠙⢿⣿⣿⠉⢹⣿⠟⠋⢉⠉⠙⢿⣿⣿⣿⠀
⠀⢸⣿⣿⠀⣿⣿⣿⡏⠀⣿⣿⣿⡀⢹⣿⠀⣸⡀⢸⣿⣿⠀⣿⣿⣇⠈⣿⠀⢸⡇⢀⡈⠻⣿⠀⢸⡏⢀⣾⣿⣿⣷⣿⣿⣿⣿⠀
⠀⢸⣿⣿⠀⣿⣿⣿⡇⠐⣿⣿⣿⠀⢸⡇⠀⠛⠓⠀⢿⣿⠀⣿⣿⡇⠀⣿⠀⢸⡇⠸⣷⣄⠙⠀⢸⡇⠈⣿⣧⣤⡄⠀⣽⣿⣿⠀
⠀⢸⣿⣿⠀⠉⠉⠉⣻⣄⣈⠉⢁⣠⣿⢀⣶⣾⣶⣆⢘⣯⠀⠉⠉⣀⣼⣿⡀⣸⡇⢈⣿⣿⣦⡀⣸⣿⣦⣈⠉⢉⣀⣼⣿⣿⣿⠀
⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀
⣷⣤⣈⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⡉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⣉⣁⣤⣾""")
    time.sleep(0)
    print("""
    
g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️g̷͒̈́l̷̿̔i̴̓̾t̴̓̒c̸͒̈́h̶̅̃⚠️

LOADING........FAILED...........¯\_(ツ)_/¯

     """)
    time.sleep(0)
    print(""" 
    
    ........DEINSTALLING GAME.......67 viruses have infected your device.......Malware detected.........Malware Protection Services Liscense plan expired........
    
     """)
    print(""" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        sike!

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣟⣹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣦⡾⠋⠛⠋⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣷⡟⠁⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣤⣄⣀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣆⡉⠙⢷⣦⡀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢷⣤⡀⠈⣻⣾⠏⠀⢠⣶⣦⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣾⣿⣤⣴⠶⠶⠿⠛⠛⠉⠉⠀⠀⠀⠙⠋⠀⠀⠀⢸⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠻⠿⣯⣥⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢡⣶⣶⣶⣶⣦⣄⠀⠀⢀⣠⡄⣀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠙⠛⠛⠻⠶⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡟⠀⢹⡗⠾⠻⠿⢛⣫⣥⡶⠶⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⠀⠀⢀⣠⣴⣦⡀⠀⠀⠀⠀⠙⢿⣿⠟⠀⠀⣼⠇⣠⣤⡶⠟⢉⡀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢋⠀⠀⢰⣿⣿⣿⣿⣿⣆⠀⠀⣶⡄⢀⣙⡻⠿⠟⠋⠈⠉⢥⡶⠾⠛⠃⡉⠉⠉⢛⠛⠻⠃⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣱⡟⢰⡄⣿⣿⠟⠛⠻⠿⣿⣆⠀⢸⣿⣄⠉⠛⠷⠦⡶⣶⠶⠾⠀⢀⣤⡾⠃⠀⠀⢹⡿⢾⣿⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠈⣿⠁⢻⡆⠀⠀⠀⠀⢸⡟⣠⡌⠿⠀⠻⢷⣄⠀⠀⠀⠀⠶⠟⣋⣭⣴⠇⠘⠛⠛⠃⠀⢉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⡾⢾⡟⡄⠈⠻⢶⣦⣴⣾⠛⠁⠘⣷⡄⠀⠀⠀⣹⣟⡀⠀⠀⠀⠘⠋⠁⠀⠀⠀⢠⣄⣦⣄⠘⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⢟⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠐⢻⡿⢡⡄⠀⣿⣦⠀⠀⠀⣄⣹⣧⢰⡄⠀⠀⠀⠀⠀⠈⠉⠛⠛⠀⣤⣀⡀⢴⣼⡻⠶⣦⠙⠗⠙⢻⣦⢈⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠠⡿⠁⣿⠃⢰⡟⡿⠗⠠⣦⣿⠀⠈⠈⢻⣆⡺⣦⠀⠀⡀⢠⣄⠀⠀⠈⠉⠋⠀⠈⠛⠷⠀⢴⡄⠀⢶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⢿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠰⣧⢀⣿⠀⠀⠹⣿⠀⠀⠀⠀⠉⠁⢹⣇⠈⠛⠷⢿⡆⠀⠀⠀⠻⣦⣄⣰⡄⠀⠈⠻⠖⢄⣙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣾⢿⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠀⣿⢸⡏⠀⠀⠀⣭⡀⠀⠀⠀⠀⠀⠈⠃⠀⠀⢷⣆⡘⢷⡶⡤⢀⠀⠉⠋⠻⣦⣄⢠⡀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣎⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡌⠁⠸⣧⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⢻⣆⠀⠙⠻⢶⣄⠀⠈⠀⣾⣷⣴⠿⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⢹⣧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⣦⣀⠻⠇⠀⠸⠇⠀⠀⣤⡀⠀⠀⠀⣄⠀⠀⠀⠀⢻⣷⣄⠀⠀⣿⠃⠀⣀⣿⣿⣿⣦⡀⢈⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⣤⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣶⣿⣾⣿⣏⠻⣦⣀⠀⣿⣷⣄⡀⢿⣄⠛⢻⢶⣄⣿⣴⣿⣿⣿⣿⣿⣿⣿⣟⠉⠈⠙⠷⣦⣄⡀⠀⠀⠀⢀⣴⠟⠋⢁⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠉⠀⠈⠀⠉⠉⠀⠻⠗⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠛⣷⣄⢰⡿⠁⠉⠻⣿⠷⠾⠻⢷⣤⣤⡾⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠙⠻⠶⣦⣤⣤⣽⣇⣤⣤⣶⠾⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛⢻⡿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣯⣿⠻⠿⠻⢿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣇⠀⣀⣸⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠛⠛⢹⡿⣿⣿⣠⣤⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠛⠛⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣶⣤⡿⠁⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣷⡄⣠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    time.sleep(0)
    print( 

            """     hi! and welcome to my inconsistent 'choose you path' opossum game.                                      
            In this game you will be playing as a baby opossum (NOT ACCURATE FIGHT ME IF YOUR MAD)              ᘛ⁐̤ᕐᐷ
            and you will be met with different choices through your life to progress through this game.         
            Your goal is to live the longest through is game and get the 'cOnGrAtS, b0oMeR<3' achivement        ⋆｡𖦹°⭒˚｡⋆
            to 'beat' the game.                                                                                 
                                                                                                                ᘛ⁐̤ᕐᐷ
            There are different achievements throughout the game you can aquire and                             
            these achievements will allow you to get more options and unlock more paths for your story.         ⋆｡𖦹°⭒˚｡⋆
            Your game and all achievements will be lost once you manually restart the game instead of           
            'retrying' it. <33.                                                                                 ᘛ⁐̤ᕐᐷ
                                                                                                                
            You can type in 'intro text run' to see this message again except for when entering                 ⋆｡𖦹°⭒˚｡⋆
            important input the game asks taht might/will affect your current game run.                         
                                                                                                                ᘛ⁐̤ᕐᐷ
            ________________________!---------DISCLAIMER---------!________________________                      
                                                                                                                ⋆｡𖦹°⭒˚｡⋆
            Not all of the content in this game will be scientificly accurate or true so                        
                     DO NOT use this as a source of basic or advenced knowledge                                 ᘛ⁐̤ᕐᐷ
                                                                                                                
            ________________________!-----------------------------!________________________                     ⋆｡𖦹°⭒˚｡⋆
            \n""")
        
    print("Oh and before you start, Can I have your name? It will help you recognise if you are still playing your current game run history becuase it will be shown in your screen <3.\n")
    user_name = input()
    print(f"Well its time to begin your game, {user_name}. Good luck ;)")

    for _ in range(3):
        time.sleep(0)
        print("...")

    return user_name

def hi ():
    print("🪼*ੈ｡𖦹°‧🫧⋅˚₊‧ 🐚 ily, carnation coral ~<3")

class Ur_A_Boomer_congrats: #longest life : winner of the game 

    print("'cOnGrAtS, b0oMeR<3'")

    #pass

class CURRENT_GAMERUN_STATISTICS: #GAUTHAM IMMA GET UUUUUUU SHUSHHSHSHHSHSHSHHHSHHSHHHHHSHSHSH BEFORE I SHOVE A PENCIL IN YOUR THROAT
    if DEATH == True:
        print(f"YOU DIED. YOUR CAUSE OF DEATH WAS {cause_of_death}")

    def __init__(self) -> None:
        self.current_hunger = [] #the moment your current hunger is less to minimum hunger, you health diminishes into less than the minimum health and you DIEE
        self.current_thirst = [] #the moment your current thirst is less to minimum thirst, you health diminishes into less than the minimum health and you DIEE
        self.current_health = [] #the moment your current hunger is less to minumum health, you immediately DIEE

        #self.opossum_joey_dies_prematurely_by_predator_in_forest_HAHA_LOL_LOSER = [] #FIX THIS AVRIABLE FUNCTION DO THAT IT HAS 15% CHANCE OF DIE BY PRED OR NOT

        self.cause_of_death = ()

        self.life_time_left = 500

        self.tempurrature_miniumum = 1

        self.tempurrature_maximum = 10

        self.died_when_trying_to_lay_dead_cuz_was_bad_at_pretedning = [] # BROS SKILL ISSUE TURNED INTO A LIFE ISSUE TURNED INTO DAHT FR FR. DAMN YOU SO BAD AT PRENTEIDN GTO BE DEAD YOU AACTUALLLY DIED LOL LOL "YOLO" NAHHHHHH MO LIKE YNLAA ahhahahahAHAHAAHAhAHbaHbBHABBAHa. 

        self.current_run_statistics = ()

        pass

        return poison

    
    def dying() -> None:
        print("YOU DIED. WAH WAH WAWAWAWAAAAAAAHH.")
        DEATH = True

#class Choices_Choices_Choices_im_whishy_washy:
def get_first_choice___newbron_joey_born_in_den(user_name: str, poison: int, cause_of_death: str, eat_all: str) -> None:  #REplace ___ with username metnioned above in def noob_begginer_introductionary_visuals_and_wordsstuffs
    print(f"""
           Welcome to life, {user_name}.You have already ended your 60 days attached to your  
        mother and have gained your vison after 2 motnhs of blindelessy followign on your mother's 
        back. You are currenly in your den in the woods and are currently at AGE ZERO . Your 
        mother and  is sleeping heavily and you are getting hungry. Your first objective is to get
        food before the third day ends or you starve. You will only have THREE chances to leave 
        the den each day you monon-scale and hot pink bishop couch potato named {user_name} DESAYUNO PETIT_DEJEUNER NRI ỰTỰTỰ
        
        (ALso your dad is naurt here he wendigo to get the berry juice :P)
        
        .\n""") 

    #if opossum_joey_dies_prematurely_by_predator_in_forest.random.randint(1, 100) < 16:
        #opossum_joey_dies_prematurely_by_predator_in_forest = "yes"s
        #print (opossum_joey_dies_prematurely_by_predator_in_forest)

    print("So, do you want to 'look for food' or 'mingle with siblings?. Remeber, yu must type in these EXACT responses to advance.")
    first_choice___newbron_joey_born_in_den_chosen_choice_of_first_run_one_point_one = input()   #ad 1 maybe to deviate and define it bwtrer idk lemem etest/
    if first_choice___newbron_joey_born_in_den_chosen_choice_of_first_run_one_point_one == mingle_with_sibs:
        print("You walk to your stinky little siblings and want to get to know them. You can only talk to 3 each day.") 
        print("You can now talk to 'Offilia' 'Pita' 'Othelie' 'Stelli' 'Stevis' 'Usyrupla' 'Macienrie' ?")
        choice = input()   
        if choice == sibling_list:
            print(f"You walk up to {choice}. They are talking about {possum_sibling_moralties_and_drive}")
    if first_choice___newbron_joey_born_in_den_chosen_choice_of_first_run_one_point_one == "look for food":
        print("""You temporarily leave your den in search of food and stumble upon sum ~suspicous~ almons 
              (CS minecraft 6th grade unit nostalgia hitting hard ngl) and you are wondering whether to eat

              them now or bring them back for your family. There would be enough for everyone to get one 
              almond each, or you can eat all 9 almonds. One almond will reward you +1 food but eating all 
              9 will lead to +9 food. 
              
                ~~~This choice might affect your future games~~~

              Remember: The less hunger, the better. The least amount  you can have in your
              food barbefore doryo-chaging the bucket is 1 so you need to eat food to keep 
              your food bar up ;P""")
        print("SO, 'eat all almonds' or 'share with family'. Remember to type these phrases out exactly.")
        first_choice___newbron_joey_born_in_den_chosen_choice_of_first_run_one_point_two = input()
        if first_choice___newbron_joey_born_in_den_chosen_choice_of_first_run_one_point_two == eat_all:
            print("You chose to eat ALL of the almonds by yourself, without sharing or checking with your family, but........")
            for _ in range(3):
                time.sleep(0)
                print("...")
            print("""OH NO. YOU ATE ALLL THE ALMONDS BUT YOU DIED CUZ ALMOND ARE TOXIC TO OPOSSUMS WAP WAP WAAAWAWAWWAAA. BUT MAYBE
                   IF YOU HAD NOT BEEN A SELFISH,  YOU WOULD HAVE SHARED WITH YOUR FAMILY AND ONE OF YOUR SIBLINGS WOULD HAVE 
                   DIED BEFORE YOU ATE THE ALMOND, >:T.  """)
            print("  ~~~~~~siggghhhh~~~~~~~~~")
            poison == cause_of_death
            DEATH
            
        
        
        #PATCH THE RANDOM CHANCE PROBABLITY OF DEATH BY PREADOT IN DEN IN FOREST BECAUSE THERE IS ERERRO AND IS A BUG AND ROADBLOCK RN 
        
    #else: print(f"....You have to do soemthing, {user_name}. You can either choose 'mingle with siblings' or 'look for food'")



    #def dying_unnaturally(self):
        #self.current_hunger = ... #the moment your current hunger is less to minimum hunger, you health diminishes into less than the minimum health and you DIEE
        #self.current_thirst = ... #the moment your current thirst is less to minimum thirst, you health diminishes into less than the minimum health and you DIEE
        #self.current_health = ... #the moment your current hunger is less to minumum health, you immediately DIEE

        #self.life_time_left = 500

        #if self.opossum_joey_dies_prematurely_by_predator_in_forest_HAHA_LOL_LOSER == "yes":
            #print(""" HAHA LOSER YOU DIED RIGHT AFTER YOU WERE BORN. BRO TRIED TO SKIP THE CUTSCENES AND GTO RESET. BRO DIED AFTER TWO SECONDS OF LIVING. BRO DDINT EVEN GET A LIVED FOR 10 SECONDS ACHIEVEMENT. 
                #BRO's DEAD AT 2 SEOCONDS . BROS DAD DIDNT EVEN HAVE ENOUGH TIME TO LEAVE HIM FOR TH EMILK. BRO PEAKED MORE IN THE WOMB THAN IN ACTUAL LIFE. BRO DDINT HAVE SKILL ISSUES HE HAS LIFE ISSUES. 
                #FR FR.. DMAN, THIS MSUT DISS_A POINTI_TINGn!!!!!. LOL LSOER LLLL. BRO DIED BEOFR OSOMEONE COULD SAY YOLO. BRO WOULDVAE TAKEN 'YOLO' TO HEART HE DIED BEFORE HE COULD LOL""")

user_name = noob_begginer_introductionary_visuals_and_wordsstuff()
while play_again:
    hi()
    #game = Choices_Choices_Choices_im_whishy_washy() *jeoprady theme song starts playing " NA NA NAAAAA NANA NA NA NAAAA NANA NA NA NA na NAHH^, NaNanAANaNA,,,,"
    get_first_choice___newbron_joey_born_in_den(user_name, poison, cause_of_death, eat_all)

print("\nDo you want to play again?")
play_again = input().lower().startswith("y")


