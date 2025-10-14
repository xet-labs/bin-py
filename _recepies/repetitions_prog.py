def questions():
    user = input("What is your username?") #username
    race = input("What is your race? (orc, human, elf, goblin)") #race

#won't move on if the player fills an answer that is not an option
    if race == "orc" or race == "human" or race == "elf" or race == "goblin":
        pClass = input("What is your class? (archer, warrior, rogue or mage)")


    else:
        while race != "orc" and race != "human" and race != "goblin" and race != "elf":
            race = input("What is your race? (orc, human, elf, goblin------)")
            if race == "orc" or race == "human" or race == "elf" or race == "goblin":
                pClass = input("What is your class? (archer, warrior, rogue or mage)")

#won't move on if the player fills an answer that is not an option               
    if pClass == "archer" or pClass == "warrior" or pClass == "rogue" or pClass == "mage":
            correct = input("So you are " + user + ", the " + race + " " + pClass + "? (yes or no)")

    else:
        while pClass != "archer" and pClass != "warrior" and pClass != "rogue" and pClass != "mage":
            pClass = input("What is your class? (archer, warrior, rogue or mage)")
            if pClass == "archer" or pClass == "warrior" or pClass == "rogue" or pClass == "mage":
                correct = input("So you are " + user + ", the " + race + " " + pClass + "? (yes or no)")

    def correct_def():
        correct = input("So you are " + user + ", the " + race + " " + pClass + "? (yes or no)")
        if correct == "yes": #if player likes their choices the game will begin
            print("Enjoy the game " + user + "!")

        elif correct == "no": #if player doesn't like their choices all questions are asked again
            reAsk = input("What would you like to change?(username, race, class or all)")

        else:
            while correct != "yes" and correct != "no":
                correct = input("So you are " + user + ", the " + race + " " + pClass + "? (yes or no)")
            if correct == "yes":
                print("Enjoy the game " + user + "!")

            elif correct == "no":
                questions()

    if correct == "yes": #if player likes their choices the game will begin
        print("Enjoy the game " + user + "!")

    elif correct == "no": #if player doesn't like their choices all questions are asked again
        reAsk = input("What would you like to change?(username, race, class or all)")

        if reAsk == "username":
            user = input("What is your username?")
            correct_def()

        elif reAsk == "race":
            race = input("What is your race? (orc, human, elf, goblin)")
            while race != "orc" and race != "human" and race != "goblin" and race != "elf":
                race = input("What is your race? (orc, human, elf, goblin)")
            correct_def()

        elif reAsk == "class":
            pClass = input("What is your class? (archer, warrior, rogue or mage)")
            while pClass != "archer" and pClass != "warrior" and pClass != "rogue" and pClass != "mage":
                pClass = input("What is your class? (archer, warrior, rogue or mage)")
            correct_def()

        elif reAsk == "all":
            questions()

        else:
            while reAsk != "username" and reAsk != "race" and reAsk != "class" and reAsk != "all":
                reAsk = input("What would you like to change?(username, race, class or all)")
                if reAsk == "username":
                    user = input("What is your username?")
                    print("Enjoy the game " + user + "!")

                elif reAsk == "race":
                    race = input("What is your race? (orc, human, elf, goblin)")
                    while race != "orc" and race != "human" and race != "goblin" and race != "elf":
                        race = input("What is your race? (orc, human, elf, goblin)")
                    print("Enjoy the game " + user + "!")

                elif reAsk == "class":
                    pClass = input("What is your class? (archer, warrior, rogue or mage)")
                    while pClass != "archer" and pClass != "warrior" and pClass != "rogue" and pClass != "mage":
                        pClass = input("What is your class? (archer, warrior, rogue or mage)")
                    print("Enjoy the game " + user + "!")

                elif reAsk == "all":
                    questions()

#won't move on if the player fills an answer that is not an option 
    else:
        while correct != "yes" and correct != "no":
            correct = input("So you are " + user + ", the " + race + " " + pClass + "? (yes or no)")
        if correct == "yes":
            print("Enjoy the game " + user + "!")

        elif correct == "no":
            reAsk = input("What would you like to change?(username, race, class or all)")

        if reAsk == "username":
            user = input("What is your username?")
            correct_def()

        elif reAsk == "race":
            race = input("What is your race? (orc, human, elf, goblin)")
            while race != "orc" and race != "human" and race != "goblin" and race != "elf":
                race = input("What is your race? (orc, human, elf, goblin)")
            correct_def()

        elif reAsk == "class":
            pClass = input("What is your class? (archer, warrior, rogue or mage)")
            while pClass != "archer" and pClass != "warrior" and pClass != "rogue" and pClass != "mage":
                pClass = input("What is your class? (archer, warrior, rogue or mage)")
            correct_def()

        elif reAsk == "all":
            questions()

        else:
            while reAsk != "username" and reAsk != "race" and reAsk != "class" and reAsk != "all":
                reAsk = input("What would you like to change?(username, race, class or all)")
                if reAsk == "username":
                    user = input("What is your username?")
                    print("Enjoy the game " + user + "!")

                elif reAsk == "race":
                    race = input("What is your race? (orc, human, elf, goblin)")
                    while race != "orc" and race != "human" and race != "goblin" and race != "elf":
                        race = input("What is your race? (orc, human, elf, goblin)")
                    print("Enjoy the game " + user + "!")

                elif reAsk == "class":
                    pClass = input("What is your class? (archer, warrior, rogue or mage)")
                    while pClass != "archer" and pClass != "warrior" and pClass != "rogue" and pClass != "mage":
                        pClass = input("What is your class? (archer, warrior, rogue or mage)")
                    print("Enjoy the game " + user + "!")

                elif reAsk == "all":
                    questions()
#questions()
