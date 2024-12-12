import random
import time

sugar_bags = 3
milk_bottles = 4
wheat_bags = 3
fishes_fishes = 2

list_of_items = [

    sugar_bags, 
    milk_bottles, 
    wheat_bags, 
    fishes_fishes,

    ]

# make a list of items that contains all of the above
# pass the list into each function and return the updated list from each function

def intro_dialogue() -> list:

    print("Welcome to...")
    print("        ")
    time.sleep(2)
    print("𝔒 𝔯𝔢𝔤 𝔬 𝔫  ✯  𝔗 𝔯𝔞 𝔦 𝔩")
    time.sleep(2)

    print("What is your name young traveler?")
    user_name = input()

    time.sleep(3)

    print("        ")
    print(f"Well, {user_name}, nice to meet you.")

    time.sleep(2)

    print("        ")
    print("So I heard you're from Missouri, and headed to Oregon City! This trip will take you 6 months. You will go through 5-7 states.")
        
    time.sleep(4)

    print("        ")
    print("So you will start with 3 sugar bags, 4 milk bottles, 3 wheat bags, and 2 fishes. Please keep in mind that throughout this journey you may loose and gain materials. ")

    time.sleep(6)

    print("        ")
    print("You will come across some challenges, which include illnesses and wagon/trail issues, and weather problems.")

    time.sleep(4)

    print("        ")
    print("Your partner couldn't make it due to work issues, but they will meet you later at Oregon City when traveling with others, so it's just you, your child and your grandmother.")

    time.sleep(4)

    print("        ")
    print("good luck comrade.")

    time.sleep (3)

    print("        ")
    print("oh and try not to die or kill your family :>")

    return list

def challenge_one_dialogue(list_of_items: list) -> list:
    sugar_bags, milk_bottles, wheat_bags, fishes_fishes = list_of_items

    time.sleep (1)

    print("        ")
    print("𝔠 𝔥 𝔞 𝔭 𝔱𝔢 𝔯 1 (𝔐  𝔬 𝔫 𝔱 𝔥 1-2)")
    time.sleep(3)

    print("        ")
    print(f"You have {sugar_bags} sugar bags, {milk_bottles} milk bottles, {wheat_bags} wheat bags, and {fishes_fishes} fishes.")
    time.sleep (3)


    print("        ")
    print("It's the 1st month, and everything is going smoothly. Your currently hanging out in the wagon playing with your child.")

    time.sleep (5)

    print("        ")
    print("Grandmother is taking over the horses, and you feel the burning sun on your skin through the white cloth covering the wagon.")

    time.sleep (5)

    print("""                           ======
                        _}|_+__+_|
        𓃔 𓃔 𓃔 𓃔 ---- -^    𖥞  𖥞   𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """)

    time.sleep (3)

    print("But wait. Is that your grandmother calling you? hmm, she seems to be talking about some river ahead.")

    time.sleep(5)

    print("        ")
    print("The wagon slowly comes to a stop. You exit the wagon with your child, and find grandmother staring into the distance.")

    time.sleep(3)

    print("        ")
    print("You look upon a river right in front of you, rushing with fast, clear water.")

    time.sleep(3)

    print("        ")
    print("                      oh no! ")
    print("﹏﹏﹏﹏﹏﹏﹏﹏﹏________𖨆 𖨆𐀪 𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣𖥧")
    
    list_of_items = [

    sugar_bags, 
    milk_bottles, 
    wheat_bags, 
    fishes_fishes,

    ]
    return list_of_items
    
def challenge_one(list_of_items: list) -> list:
    sugar_bags, milk_bottles, wheat_bags, fishes_fishes = list_of_items

    print("""Do you: (Please type 1, 2, or 3)
    1.) Guide your wagon through the old bridge on the other side 
    2.) Drive your wagon towards the shallow end of the river
    3.) Guiding your wagon to the "beach area" that connects both islands, however there might be a territory of alligators there
    
    """)

    chapter_one_choice = input

    if chapter_one_choice == "1":
        print("You hop back in your wagon, and explain the plan to Grandmother. She hesitates, but trusts you.")

        time.sleep(3)

        print("        ")
        print("Grandmother hops in the back with your child, and you take on the cattle.")

        time.sleep(3)

        print("        ")
        print("You slowly guide the wagon over the bumpy surface and over to the bridge.The wagon climbs over the bridge and you're right about to make it!")

        time.sleep(3)

        print("        ")
        print("＊ＣＲＡＣＫ＊")

        time.sleep(3)

        print("        ")
        print("WHAT WAS THAT??? oh no! it seems the wheel been snapped on a piece of wood! Good thing you made it across. With a bit of time and skill, you and grandmother managed to repair it.")

        time.sleep(3)

        print("""                           ======
                        _}|_+__+_|
        𓃔 𓃔 𓃔 𓃔 ---- -^    𖥞 𖨆/𖥞 𖨆+ """)

        time.sleep(3)

        fishes_fishes = fishes_fishes + 5
        print("        ")
        print(f"fortunately, you decided to stop by and fish, and luck was on your side today! You now have {fishes_fishes} fishes! Congrats. You made the right choice!")



        print("𝕮𝖍𝖆𝖑𝖑𝖊𝖓𝖌𝖊 1 ~ 𝕻𝖆𝖘𝖘𝖊𝖉")

        return list_of_items

    if chapter_one_choice == "2" :

        print("So you chose to guide your wagon through the shallow end, eh? Well, lets get on to it.")

        time.sleep(3)

        print("        ")
        print("Grandmother heartfully agrees, approving of your decision.")

        time.sleep(3)

        print("        ")
        print("She climbs in with your child, and you take the lead of the cattle.")

        time.sleep(3)

        print("        ")
        print("One whip, and they're off. You guide them towards the shallow end, and its smooth sailing from there on.")

        time.sleep(3)

        print("        ")
        print("You make it across, and everyone celebrates! You sit down with Grandmother and your child, and fall asleep under the stars. ")

        time.sleep(4)

        print("✧･ﾟ: *✧･ﾟ:*~*:･ﾟ✧*:･ﾟ✧")

        time.sleep(3)

        print("        ")
        print("uh oh. you woke up to find only scraps of wood where your carriage used to be. turns out that termites ate it all! uh oh...")

        time.sleep(3)

        print("       ")
        print("they ate all your food too! you and your grandmother and child slowly die of hunger and lack of shelter.")

        time.sleep(3)

        print("𓆨𓆨𓆨𓆨𓆨𓆨𓆨𓆨")
        print(" *termites* ")

        print("       ")
        print("𝔱𝔥𝔢 𝔢𝔫𝔡")

        time.sleep(3)

        print(f"You died due to hunger, because wagon and food was eaten by termites.")

        return list

    if chapter_one_choice == "3" : 

        print("Ah. So you chose to be a bit more adventurous. ")

        time.sleep(3)

        print("        ")
        print("Grandmother is extremely unsure, but she trusts that you know the right decision.")

        time.sleep(3)

        print("        ")
        print("She and your child enter the wagon, and you take the lead. With one whip at the cattles, you're off. You guide them towards the desert area, and you think twice if this was the right decision.")

        time.sleep(3)

        print("        ")
        print("Uh oh. The roars of alligators are heard and from then everything is cHAOS!")

        print("SWING TO THE RIGHT!")
        time.sleep(1.6789)
        print("ALLIGATOR!!! ALLIGATOR!!!")
        time.sleep(1.6789)
        print("I SAID TO THE LEFT!!!")
        time.sleep(1.6789)
        print("QUICK!!! WHAT ARE YOU DOING?!?!?!?!")
        time.sleep(1.6789)
        print("ALLIGATOR!!! ALLIGATOR!!!")
        time.sleep(1.6789)
        print("WHAT THE*#579q99w478980($*%($*%(*W^8$&W(^*(8")
        time.sleep(1.6789)
        print("ALLIGATOR!!! ALLIGATOR!!!")
        time.sleep(1.6789)
        print("I SAID GO TO THE $58&W(%*)  RIGHT!!! ARE YOU S*%&w8579w485?!?!?!?!")
        time.sleep(1.6789)
        print("ALLIGATOR!!! ALLIGATOR!!!")
        time.sleep(1.6789)
        print("WATCH OUT!!!!!")


        time.sleep(3)
        print("        ")
        print("phew. that was quite the chaos!")

        print("        ")
        print("good to see you're still in one piece... this wasn't that good of a decision i see...")

        time.sleep(3)
        print("        ")
        print("best to check up on grandmother and your child now... make sure everythings still there.")

        time.sleep (3)
        print("        ")
        print(" It seems there is some damage to your wagon. Grandmother and your child are a bit shaken up, but thankfully still with you. You have lost some items.")
        #HERE
        sugar_bags = sugar_bags - 1
        milk_bottles = milk_bottles - 2
        wheat_bags = wheat_bags - 1
        fishes_fishes = fishes_fishes - 1

        print(f"You now have {sugar_bags} sugar bags, {milk_bottles} milk bottles, {wheat_bags} wheat bags, and {fishes_fishes} fishes.")

        return list
    list_of_items = [

    sugar_bags, 
    milk_bottles, 
    wheat_bags, 
    fishes_fishes,

    ]
    return list_of_items
    
def challenge_two_dialogue(list_of_items: list) -> list:
    sugar_bags, milk_bottles, wheat_bags, fishes_fishes = list_of_items

    sugar_bags = sugar_bags - 1
    milk_bottles = milk_bottles - 2
    wheat_bags = wheat_bags - 1
    fishes_fishes = fishes_fishes - 1

    print("        ")
    print("𝔠 𝔥 𝔞 𝔭 𝔱𝔢 𝔯 2 (𝔐  𝔬 𝔫 𝔱 𝔥 3-4)")
    time.sleep(3)

    print("        ")
    print(f"You have {sugar_bags} sugar bags, {milk_bottles} milk bottles, {wheat_bags} wheat bags, and {fishes_fishes} fishes.")
    time.sleep (5)

    print("        ")
    print("Your child has been feeling sick lately, you suspect it must be fever, so you decided to stop and rest. But this morning when you woke up you found your child throwing up everywhere.")

    print("...")

    print("your child, you suspect, has cholera. cholera has a mortality rate as high as 50 - 70 percent if left untreated. it is also contagious, so if not isolated, you could catch it aswell. ")

    time.sleep(5)

    print("        ")
    print("You're in luck, because not far from here is a clinic. Please rush!")

    time.sleep(4)

    print("        ")

    print("""                       ======
                    _}|_+__+_|
    𓃔 𓃔 𓃔 𓃔 ---- -^    𖥞  𖥞   𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣𖥧𖡼.𖤣
    ______________________________________________ """)

    print("                ")
    print("loading ↻")

    time.sleep(5)

    print(" you have arrived ~ ")

    print("""               ✙    
    ° ˛ ° ˚ * _Π_____*☽*˚ ˛
    ✩ ˚˛˚*/______/__＼。✩˚  ˚˛    ♡ 
    ˚ ˛˚˛˚｜ 田田｜門｜ ˚ ˚
                            """)
    
    time.sleep(3)

    print("A doctor awaits you. Grandmother carries your child inside, and you nervously follow.")
    print("    ")
    time.sleep(4)
    print("doctor:")
    print("✙ 𝖄𝖔𝖚𝖗 𝖈𝖍𝖎𝖑𝖉 𝖍𝖆𝖘 𝖇𝖊𝖊𝖓 𝖉𝖎𝖆𝖌𝖓𝖔𝖘𝖊𝖉 𝖜𝖎𝖙𝖍 𝖈𝖍𝖔𝖑𝖊𝖗𝖆. ✙")

    time.sleep(4)

    print("   ")
    print("𝕱𝖔𝖗𝖙𝖚𝖓𝖆𝖙𝖊𝖑𝖞, 𝖜𝖊 𝖍𝖆𝖛𝖊 𝖔𝖓𝖊 𝖙𝖗𝖊𝖆𝖙𝖒𝖊𝖓𝖙 𝖑𝖊𝖋𝖙. 𝕴𝖙 𝖜𝖎𝖑𝖑 𝖈𝖔𝖘𝖙 𝖞𝖔𝖚 𝖙𝖍𝖔𝖚𝖌𝖍.")

    list_of_items = [

    sugar_bags, 
    milk_bottles, 
    wheat_bags, 
    fishes_fishes,

    ]
    return list_of_items
    
def challenge_two(list_of_items: list) -> list:
    sugar_bags, milk_bottles, wheat_bags, fishes_fishes = list_of_items
    time.sleep(3)
    print("     ")
    print("Well? This doctor is offering you a treatment for your sick child. You do however require to pay 4 sugar bags.")
    time.sleep(4)
    print("     ")
    ("So what will it be? wait, one sec, the doctor is saying something...")
    time.sleep(5)
    print("     ")
    print("Ah ok. So the doctor suggested a game of luck, with a reduced price of 1 sugar bag per guess. I'd say you have a better chance here!")

    time.sleep(3)
    print("    ")

    print("""~✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙~

            Do you: (Please type 1 or 2)
            1) Take the lucky opportunity!
            2) Disappointly decline because you're a selfish brat (sorry but its true-)""")
    chapter_two_choice = input()

    if chapter_two_choice == "1":
        print("Glad to know that you care about your child! Previous travelers said no because they cared more about themselves... crazy folk")
        print("    ")
        time.sleep(3)
        print("You walk back to the office, hesistant of your decision, but willing to risk anything to save your child.")
        time.sleep(3)
        print("    ")
        print("Doctor:")
        time.sleep(2)
        print("    ")
        print("ℑ'𝔪 𝔤𝔩𝔞𝔡 𝔶𝔬𝔲 𝔴𝔢𝔫𝔱 𝔱𝔥𝔯𝔬𝔲𝔤𝔥 𝔴𝔦𝔱𝔥 𝔪𝔶 𝔡𝔢𝔠𝔦𝔰𝔦𝔬𝔫! 𝔜𝔬𝔲 𝔴𝔬𝔫𝔱 𝔯𝔢𝔤𝔯𝔢𝔱 𝔦𝔱.")
        time.sleep(3)
        print("          ")
        print("𝔖𝔬, ℑ 𝔡𝔢𝔠𝔦𝔡𝔢𝔡 𝔱𝔬 𝔩𝔢𝔱 𝔶𝔬𝔲 𝔭𝔩𝔞𝔶 𝔞 𝔤𝔞𝔪𝔢 𝔴𝔦𝔱𝔥 𝔞 𝔯𝔢𝔡𝔲𝔠𝔢𝔡 𝔭𝔯𝔦𝔠𝔢 𝔬𝔣 1 𝔰𝔲𝔤𝔞𝔯 𝔟𝔞𝔤 𝔭𝔢𝔯 𝔤𝔲𝔢𝔰𝔰!")
        time.sleep(3)
        print("    ")
        print("""𝔗𝔥𝔢 𝔤𝔞𝔪𝔢 𝔴𝔬𝔯𝔨𝔰 𝔩𝔦𝔨𝔢 𝔱𝔥𝔦𝔰;
         𝔶𝔬𝔲 𝔪𝔲𝔰𝔱 𝔠𝔥𝔬𝔬𝔰𝔢 𝔬𝔫𝔢 𝔬𝔣 3 𝔠𝔲𝔭𝔰, 𝔞𝔫𝔡 𝔬𝔫𝔢 𝔠𝔬𝔫𝔱𝔞𝔦𝔫𝔰 𝔞 𝔠𝔬𝔦𝔫. 
         𝔈𝔳𝔢𝔯𝔶 𝔤𝔲𝔢𝔰𝔰 𝔠𝔬𝔰𝔱𝔰 1 𝔰𝔲𝔤𝔞𝔯 𝔟𝔞𝔤. ℑ𝔣 𝔶𝔬𝔲 𝔴𝔦𝔫 𝔟𝔢𝔣𝔬𝔯𝔢 𝔶𝔬𝔲 𝔯𝔲𝔫 𝔬𝔲𝔱 𝔬𝔣 𝔰𝔲𝔤𝔞𝔯 𝔟𝔞𝔤𝔰, 𝔶𝔬𝔲 𝔤𝔢𝔱 𝔱𝔥𝔢 𝔪𝔢𝔡𝔦𝔠𝔦𝔫𝔢.
          ℑ𝔣 𝔶𝔬𝔲 𝔯𝔲𝔫 𝔬𝔲𝔱 𝔬𝔣 𝔰𝔲𝔤𝔞𝔯 𝔟𝔞𝔤𝔰 𝔟𝔢𝔣𝔬𝔯𝔢 𝔶𝔬𝔲 𝔪𝔞𝔫𝔞𝔤𝔢 𝔱𝔬 𝔤𝔲𝔢𝔰𝔰 𝔠𝔬𝔯𝔯𝔢𝔠𝔱𝔩𝔶, 𝔶𝔬𝔲 𝔩𝔬𝔰𝔢 𝔱𝔥𝔢 𝔪𝔢𝔡𝔦𝔠𝔦𝔫𝔢.
        """)
        time.sleep(5)
        print("   ")
        print("Lets begin!")
        time.sleep(3)
        print("       ")

        while sugar_bags > 0:
            print(f"You have {sugar_bags} sugar bags. Please guess 1, 2, or 3")
            time.sleep(3)
            choice_chapter_two = input()
            print(f"You chose cup #{choice_chapter_two}.")
            random.choice((1, 2))
            if random == 1 :
                print("Sorry, the coin is not under that cup.")
                sugar_bags = sugar_bags - 1
                
            if random == 2 :
                print("WOW! You got it! Congrats!")

        if sugar_bags == 0:
            print("You ran out of sugar bags.")


    if chapter_two_choice == "2":
        print("... alright then...")
        print("    ")
        print("well we better be on our way now.")

        time.sleep(5)
        print("    ")
        print("    ")
        print("On July 23rd 3:02 AM, your child passed away in their sleep from Cholera.")
        print("    ")
        print("    ")
        time.sleep(3)
        print(" ﮩ٨ـﮩﮩ٨ـﮩ٨ـ____________")
        
        time.sleep(3)

    list_of_items = [

    sugar_bags, 
    milk_bottles, 
    wheat_bags, 
    fishes_fishes,

    ]
    return list_of_items






intro_dialogue()
list = challenge_one_dialogue(list_of_items)
list = challenge_one(list_of_items)
list = challenge_two_dialogue(list_of_items)
list = challenge_two(list_of_items)