import random
import time

rock_paper_scissor_list = [
            "Rock",
            "Paper",
            "Scissor",
        ]

def computer_turn() -> None:
        piece = random.choice(rock_paper_scissor_list)
        print(f"(Champion)- ROCK PAPER SCISSOR SHOOT !")
        return piece

def player_turn() -> None:
            turn = input()
            return turn

def display_intro() -> None:
        print(" Welcome ! Before i introduce the game , just wait for the game to load first.")
        time.sleep(0)
        print(
            """
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠰⡁⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠙⠻⣿⣿⣿⡆⠠⠁⢠⣿⣿⣿⠟⠋⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠙⠿⣦⡄⠙⣿⣷⣶⣶⣾⣿⠋⢀⠤⠒⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⣠⣿⣿⣿⣿⣿⣿⣄⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢁⣠⡄⠈⣿⣿⣿⣿⣿⣿⠁⠠⣀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠺⠛⢉⣠⣴⣿⡟⠉⠉⢻⣿⣦⣄⡀⠉⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
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
            ⣷⣤⣈⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⣉⠉⡉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⡉⢉⣉⣁⣤⣾

            """)

        time.sleep(0)

        print(""" 
            Oh hi there! Sorry for the time stamp , the game is just loading! Welcome to the beatiful / really annoying and bad game of Rock Paper Scissors!!
            You will be playing against my Champion in a game of Rock Paper Scissors . The first to win the most games in 9 games wins! The only rules is that you can only play Rock , Paper and Scissor.  You .. WON'T .. win. Cya! And good luck :D
            BUT ... Just remember .. the house always wins.
            Now lets play shall we.. ( ≖‿  ≖ )    

               

                          ⢀⣀⣀⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ⢀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢠⣶⠟⠉⠁⠀⣠⠉⠉⠛⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠀⠈⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⢰⡿⠁⠀⣀⣠⠞⠁⠀⠀⠀⠀⠀⠉⠻⣶⡶⠶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣠⡶⠟⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠈⢿⡄⠀⢠⣴⠶⠶⠶⣦⣄⠀⠀⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⣀⣀⣀⡀⠀⠀⠀
                ⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣶⠈⣿⡀⠘⣷⠀⢸⡇⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⢀⣼⠏⢀⣠⡶⠟⠋⠉⠉⠛⢷⣄⠀
                ⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢀⣀⡀⠹⣧⠀⢻⡄⠸⣧⠀⠀⠀⠀⠀⢻⡇⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⢠⣾⣧⠾⠛⠉⠀⠀⠀⠀⠀⠀⢈⣿⠀
                ⠀⣼⡿⠶⠦⠤⠤⠤⠀⠀⠀⠀⠀⠀⢠⣤⡶⠶⠞⠛⢋⡁⠀⣿⠀⢸⡧⠀⢻⣇⠀⠀⠀⠀⠘⣇⣴⡾⠋⠀⠀⠀⠀⠀⠀⣰⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀
                ⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠃⢀⣿⢀⣾⠁⠀⠀⣿⡇⠀⠀⠀⠀⠟⠁⠀⠀⠀⠀⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⣀⣴⠿⠋⠁⠀⠀⠀
                ⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢀⣿⡛⠛⠁⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⢀⣤⠾⠋⣀⣠⣤⣤⣤⣄⡀
                ⠈⠻⣶⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀⠀⠂⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠛⠛⠛⠉⠉⠁⠀⠀⠙⣿
                ⠀⠀⠀⢹⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⠀⠀⢀⣴⡄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠏
                ⠀⠀⠀⠀⠙⠿⣶⣤⣤⣀⣀⣠⣤⣴⡶⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠉⣷⠀⢀⣴⡿⠋⠀⢀⣴⠿⠁⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠁⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣀⣀⣀⡀⠀⠀⠀⠀⠀⠁⣷⠀⢻⣧⠈⠁⢀⣤⡾⠋⠁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⢀⣤⠶⠿⣶⣤⡶⠟⠛⠉⠉⠉⢉⡉⠙⠛⢷⣦⡀⠀⠀⠀⠹⣇⠀⠹⣷⡀⠉⠁⣤⣴⠶⠛⠋⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⣰⡟⠁⢠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠙⢿⡄⠀⠀⠀⠹⣧⡀⠈⢿⣦⡀⠁⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣰⡏⠀⣰⡟⠀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄⣸⣇⠀⠀⠀⠀⠈⠻⣦⣄⣈⣻⡷⠶⣶⣶⡶⠶⠾⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⢠⡟⠀⣰⡟⠀⣄⠈⠉⠛⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠳⠶⠶⠶⠶⣤⣭⣭⣋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⢸⡇⢀⣿⠁⢠⠛⠿⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠘⣷⣼⣇⠀⠘⢷⣄⡀⠈⠙⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠈⠉⢿⡆⠀⠀⠙⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠒⠶⢶⣶⣶⣤⣤⣤⣤⣤⣀⣀⣀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠘⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠉⠛⠲⢶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠶⣦⣤⣄⣠⣤⣤⠶⠟⠋⠉⠛⠳⢶⣤⣀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣦⣄⡀⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

def get_player_turn() -> None:
            print("Choose , either Rock - Paper - Scissor")
            turn = input()
            if turn == "Rock":
                print("ROCK PAPER SCISSOR SHOOT ")
            elif turn == "Paper":
                print("ROCK PAPER SCISSOR SHOOT ")
            else:
                turn == "Scissor"
                print("ROCK PAPER SCISSOR SHOOT ")
            return turn

def get_the_winner_of_current_round(player_turn, computer_turn) -> str:
            print("Player chose")
            print(player_turn)
            print("Champion chose")
            print(computer_turn)
            if player_turn == "Rock" and computer_turn == "Paper":
                print("HAHAHHAHAHAHAHAHAAHAAHA LOOOOOOOOOOOOOOOOOOOOSER I WON YOU DUM DUM DUM BAD SKILL ISSUE")
            if player_turn == "Paper" and computer_turn == "Rock":
                print("ooooooooooohhhhhh ... you won ... for now 𓁹‿𓁹")
            if player_turn == "Rock" and computer_turn == "Scissor":
                print("ooooooooooohhhhhh ... you won ... for now 𓁹‿𓁹")
            if player_turn == "Scissor" and computer_turn == "Rock":
                print("HAHAHHAHAHAHAHAHAAHAAHA LOOOOOOOOOOOOOOOOOOOOSER I WON YOU DUM DUM DUM BAD SKILL ISSUE")
            if player_turn == "Paper" and computer_turn == "Scissor":
                print("HAHAHHAHAHAHAHAHAAHAAHA LOOOOOOOOOOOOOOOOOOOOSER I WON YOU DUM DUM DUM BAD SKILL ISSUE")
            if player_turn == "Scissor" and computer_turn == "Paper":
                print("ooooooooooohhhhhh ... you won ... for now 𓁹‿𓁹")
            if player_turn == "Rock" and computer_turn == "Rock":
                print("oooooooooooooooo we tied up! You won't win next round. (•̀ ᴖ •́ ｡) ")
            if player_turn == "Paper" and computer_turn == "Paper":
                print("oooooooooooooooo we tied up! You won't win next round. (•̀ ᴖ •́ ｡) ")
            if player_turn == "Scissor" and computer_turn == "Scissor":
                print("oooooooooooooooo we tied up! You won't win next round. (•̀ ᴖ •́ ｡) ")

def get_amount_of_games_played() -> None:
    if games_played == 1:
        print("Game 1. onto game 2")
    if games_played == 2:
        print("Game 2. onto game 3")
    if games_played == 3:
        print("Game 3. onto game 4")
    if games_played == 4:
        print("Game 4. onto game 5")
    if games_played == 5:
        print("Game 5. onto game 6")
    if games_played == 6:
        print("Game 6. onto game 7")
    if games_played == 7:
        print("Game 7. onto game 8")
    if games_played == 8:
        print("Game 8. onto game 9")
    if games_played == 9:
        print("WOW YOU FINALLY REACHED GAME 9!! yay ;D")

needed_games_to_end_session = 9
games_played = 1
coins = 0
turn = player_turn()
piece = computer_turn()
play_again = "y"

while play_again.startswith("y"):
        
    while games_played in range (1, 10):
        # win
        if turn == "Paper" and piece == "Rock":
            player_win = True
            coins += 100
        if turn == "Rock" and piece == "Scissor":
            player_win = True
            coins += 100
        if turn == "Scissor" and piece == "Paper":
            player_win = True
            coins += 100
        # lose
        if turn == "Rock" and piece == "Paper":
            player_win = True
            coins -= 50
        if turn == "Scissor" and piece == "Rock":
            player_win = True
            coins -= 50
        if turn == "Paper" and piece == "Scissor":
            player_win = True
            coins -= 50

        print(coins)
        


        if games_played < 2:
            display_intro()
            print("Im just gonna give you some time to read the intro and the rules.")
            time.sleep(0)
            print("Oh wait a second! whats your name??")
            player_name = input()
            print(f"Okay! now lets play, {player_name}!")

        if games_played > 1:
            print(" well .. welcome to another game of rock paper scissors i guess. welp lets just get straight to it.")
            print(f"oh just so you know , you got {coins} coins.")
            time.sleep(0)
            print("lets start now")

        if games_played > 1: 
            print(f"welp onto game {games_played}.")
        

        if games_played == 9:
            print(f"wowwwww you reached the end. again and in total you have gotten {coins} coins!")

        if games_played == 9:
             print("Play again? Yes or No")
             if play_again.startswith("y"):
                  play_again
             if play_again.startswith("n"):
                  print("wow. your mean")

                
        turn = get_player_turn()

        piece = computer_turn()

        winner = get_the_winner_of_current_round(turn, piece)

        get_amount_of_games_played()

        print("wow. the game is over .")

        games_played += 1

