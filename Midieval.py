from sys import exit
from random import shuffle
import time
import os
class inventory:
    sword = False
    ring =False
    pokeball = False
    grass = False
    mahogany = False
    form= False
    rapidash= False

class event:
    mission = False
    savedprincess= False
    hors=False
    foodshopfavor = False
    blacksmithfavor1=False
    blacksmithfavor2=False
    blacksmithfavor3=False
    armour1= False
    rule=False

def ellip():
    from time import sleep
    for i in range (1, 4):
        print('.', end="")
        sleep(1)


def grassyplain():
    print('You appear in a grassy plain. You are surrounded by "grass". There is a lot of "grass". Your time machine is here also and a river to the "S"')
    print('There are plains to the "W", "E", and "N"'+ '\n')
    while True:
        badaboom = input(">>").strip().lower()
        if badaboom == 'n':
            grassyplains2()
        elif badaboom == 'e':
            grassyplains4()
        elif badaboom == 'w':
            grassyplains5()
        elif badaboom == 'look grass':
            print('Oh look, a bug scuttered away to the east'+ '\n')
        elif badaboom== 'take grass':
            print('It seems to have no practical use'+ '\n')
        elif badaboom == 'exit':
            print('goodbye!')
            exit()
        else:
            print('Print Something real'+ '\n')

def grassyplains2():
    print('You are surrounded by "grass" to the "S" and "W". There is a river to the "E" and "N" that you cannot pass.')
    print('You can enter more grass to the "S" and "W"'+ '\n')
    while True:
        badaboom= input(">>").strip().lower()
        if badaboom == 's':
            grassyplain()
        elif badaboom == 'w':
            grassyplains3()
        elif badaboom == 'n':
            print('The water is moving too quickly to enter'+ '\n')
        elif badaboom== 'e':
            print('The water is moving too quickly to enter'+ '\n')
        elif badaboom == 'look grass':
            print('Oh look, a bug scuttered away to the east'+ '\n')
        elif badaboom == 'take grass':
            print('It seems to have no practical use'+ '\n')
        elif badaboom == 'exit':
            print('goodbye!'+ '\n')
            exit()
        else:
            print('Print Something real'+ '\n')

def grassyplains3():
    print('You are surrounded by "grass" to the "N", "S", and "E". There is a river to the "W" that you cannot pass.')
    while True:
        badaboom = input(">>").strip().lower()
        if badaboom == 's':
            grassyplains5()
        elif badaboom == 'e':
            grassyplains2()
        elif badaboom == 'n':
            grassyplains6()
        elif badaboom == 'w':
            print('The river is moving to fast to pass'+ '\n')
        elif badaboom == 'look grass':
            print('Oh look, a bug scuttered away to the north'+ '\n')
        elif badaboom == 'take grass':
            print('It seems to have no practical use'+ '\n')
        elif badaboom == 'exit':
            print('goodbye!'+ '\n')
            exit()
        else:
            print('Print Something real'+ '\n')

def grassyplains4():
    print('You are surrounded by "grass" to the "W". There is a river to the "E", "S", and "N" that you cannot pass.')
    while True:
        badaboom = input(">>").strip().lower()
        if badaboom== 'w':
            grassyplain()
        elif badaboom== 'take grass':
            print('You have some "peculiar" grass'+ '\n')
            inventory.grass= True
        elif badaboom== 'n':
            print('The water is moving too quickly to enter'+ '\n')
        elif badaboom== 'e':
            print('The water is moving too quickly to enter'+ '\n')
        elif badaboom== 's':
            print('The water is moving too quickly to enter'+ '\n')
        elif badaboom== 'look grass':
            print('Oh look, a bug scuttered away to the east'+ '\n')
        elif badaboom == 'exit':
            print('goodbye!'+ '\n')
            exit()
        else:
            print('Print Something real'+ '\n')

def grassyplains5():
    print('You are surrounded by "grass" to the "E" and "S". There are mountains to the "S" and "W" that you cannot pass.')
    while True:
        badaboom= input(">>").strip().lower()
        if badaboom== 'e':
            grassyplain()
        elif badaboom== 'n':
            grassyplains3()
        elif badaboom== 's':
            print("The mountain is too high to pass"+ '\n')
        elif badaboom=='w':
            print('The mountain is too high to pass'+ '\n')
        elif badaboom== 'look grass':
            print('Oh look, a bug scuttered away to the north'+ '\n')
        elif badaboom== 'take grass':
            print('It seems to have no practical use'+ '\n')
        elif badaboom == 'exit':
            print('goodbye!'+ '\n')
            exit()
        else:
            print('Print Something real'+ '\n')

def grassyplains6():
    print('You have passed the "grass" and it lies to the "S". There is a bridge crossing a mote to the "N" and to the "E" is a river that you cannot pass. To the "W" is a tall mountain.')
    while True:
        badaboom= input(">>").strip().lower()
        if badaboom== 's':
            grassyplain()
        elif badaboom== 'n':
            bridge()
        elif badaboom== 'e':
            print('The river is moving too quickly.'+ '\n')
        elif badaboom== 'w':
            print('The mountain is too high to pass')
        elif badaboom== 'look grass':
            print('Oh look, a bug scuttered away to the north'+ '\n')
        elif badaboom== 'take grass':
            print('It seems to have no practical use'+ '\n')
        elif badaboom == 'exit':
            print('goodbye!'+ '\n')
            exit()
        else:
            print('Print Something real'+ '\n')

def bridge():
    print('You have reached a bridge and see a castle ahead. To your "E" is a mote and to your "W" is a mote.')
    print('You can either go "N" across the bridge or go "S" to the grassy plains.'+ '\n')
    while True:
          badaboom=input(">>").strip().lower()
          if badaboom == 'n':
              print("You're crossing the bridge"+ '\n')
              gate()
          elif badaboom == 's':
              grassyplains6()
          elif badaboom== 'e':
              print("You can't do that silly goose. There's a mote"+ '\n')
          elif badaboom == 'w':
              print("You can't do that silly goose. There's a mote"+ '\n')
          elif badaboom == 'exit':
              print('goodbye!'+ '\n')
              exit()
          else:
              print('Print Something real'+ '\n')
def gate():
    print("You approach guards. What do you want to do?")
    print('["sneak past", "talk", "look", "take"]'+ '\n')
    while True:
        badaboom= input(">>").strip().lower()
        if badaboom== 'sneak past':
            print("The guards spotted you and stopped you. They order you to explain what you are doing")
            print('What do you say?'+ '\n')
            input(">>").strip().lower()
            print("A funny tongue you speak. You must be the frenchman we ordered to help save the princess. Our apologies for our rude behaviour, sire. Please forgive us."+ '\n'+ '\n')
            cityentrance()
        elif badaboom == 'talk':
            print("A funny tongue you speak. You must be the frenchman we ordered to help save the princess. Our apologies for our rude behaviour, sire. Please forgive us."+ '\n'+ '\n')
            cityentrance()
        elif badaboom== 'talk guard':
            print("A funny tongue you speak. You must be the frenchman we ordered to help save the princess. Our apologies for our rude behaviour, sire. Please forgive us."+ '\n'+ '\n')
            cityentrance()
        elif badaboom == 'look':
            print("You'll lose an eye if you get much closer to my sword"+ '\n')
            print("What would you like to do?")
            print('["sneak past", "talk", "look", "take"]'+ '\n')
        elif badaboom== 'take':
            print("'EY! You dare attempt to steal from a guard? You'll be trialed for this!"+ '\n')
            kingsthrone()
        elif badaboom == 'exit':
              print('goodbye!'+ '\n')
              exit()
        else:
              print('Print Something real'+ '\n')

def cityentrance():
    print('\n'+ "You're in the city")
    print('Here there is an "armoury", the "Kingsroom", and a "bazaar". You can also "leave" the city')
    print('Where would you like to go?'+ '\n')
    while True:
        phone= input(">>").strip().lower()
        if phone == "armoury":
            armoury()
        elif phone == "kingsroom":
            kingsthrone()
        elif phone == "bazaar":
            bazaar()
        elif phone== 'leave':
            bridge()
        elif phone == 'exit':
            print('goodbye!')
            exit()
        else:
            print('That is not a command')

def kingsthrone():
    if event.mission== False:
        print('You have entered the throneroom. There is a "guard". You may approach the king and "talk" with him.')# TALK THAT TALK
        while True:
            phone= input(">>").strip().lower()
            if phone == "talk":
                print("Welcome to my throne room. My apologies for the uncivilized commoners. My daughter is missing and I command you to go and find her from the mighty Charizard, a ferocious beast.")
                print("Do you accept?  y/n?"+ '\n')
                truth= input(">>").strip().lower()
                if truth == "y":
                    print('Godspeed to you. You can go pick up a suit of armour and sword in the armoury')
                    print('I bequeath you with this mission. You Have this "form" you can take it to the armoury and suit up. This should act as money.' + '\n')
                    event.mission = True
                    inventory.form = True
                    cityentrance()
                elif truth== "n":
                    print('Get out of my face! I only need people who will save my daughter')
                    cityentrance()
                else:
                    print("What? Speak English! That's not a real command"+ '\n'+ '\n')
            if phone== 'talk king':
                print("Welcome to my throne room. My apologies for the uncivilized commoners. My daughter is missing and I command you to go and find her from the mighty Charizard, a ferocious beast.")
                print("Do you accept?  y/n?"+ '\n')
                truth= input(">>").strip().lower()
                if truth == "y":
                    print('Godspeed to you. You can go pick up a suit of armour and sword in the armoury')
                    print('I bequeath you with this mission. You Have this "form" you can take it to the armoury and suit up. This should act as money.' + '\n')
                    event.mission = True
                    inventory.form = True
                    cityentrance()
                elif truth== "n":
                    print('Get out of my face! I only need people who will save my daughter')
                    cityentrance()
                else:
                    print("What? Speak English! That's not a real command"+ '\n'+ '\n')
            if phone == "talk guard":
                print("The king has been depressed ever since his daughter was taken." + "Somebody should rescue her.\n")
                print('You have entered the throneroom. There is a "guard". You may approach the king and "talk" with him.')
            elif phone == 'exit':
                print('goodbye!'+ '\n')
                exit()
            else:
                print('That is not a command'+ '\n')
    elif event.mission== True:
        if event.savedprincess==False:
            print("Go and save my daughter!"+ '\n')
            cityentrance()
        elif event.savedprincess== True:
            print("Thank you for saving my daughter. Now we can be happy"+ '\n')
            cityentrance()

bob=[]
for i in range (10, 100):
    bob.append(i)
shuffle(bob)

def armoury():
    while True:
        if event.mission== False:
            if event.armour1== False:
                print("Do you have money? y/n"+ '\n')
                phone= input(">>").strip().lower()
                if phone== "y":
                    print("Let me show you what we have here.")
                    print("We have suits of armour, swords, crossbows, maces, and axes.")
                    print("What would you like?"+ '\n')
                    input(">>").strip().lower()
                    print("Ah! Perfect choice! That will cost "+ str(bob[0])+ " pieces of gold"+ '\n')
                    print("Wait", end="")
                    ellip()
                    print("You don't have money?!?! Get out of here!"+ '\n'+ '\n')
                    cityentrance()
                elif phone== "n":
                    print("What are you doing here?!? You lazy wench! Get out!"+ '\n'+ '\n')
                    cityentrance()
                else:
                    print("That's not a real command\n")
        elif event.mission== True:
            if event.armour1==False:
                print("Do you have money? y/n?"+ '\n')
                lenovo= input(">>").strip().lower()
                if lenovo== "y":
                    print("Let me show you what we have here.")
                    print("We have suits of armour, swords, crossbows, maces, and axes.")
                    print("What would you like?"+ '\n')
                    input(">>").strip().lower()
                    print("Ah! Perfect choice! That will cost "+ str(bob[0])+ " pieces of gold. How will you be paying?"+ '\n')
                    chelsea= input(">>").strip().lower()
                    if chelsea== "use form":
                        if inventory.form==True:
                            inventory.pokeball=True
                            print("Oh, this is straight from the king himself. Sorry I didn't know earlier. I'll give you this magic 'pokeball'"+ '\n')
                            cityentrance()
                            event.armour1= True
                    else:
                        print("Wait", end="")
                        ellip()
                        print(" You don't have money?!? What are you doing here?!? You lazy wench! Get out!"+ '\n')
                        cityentrance()
                elif lenovo== "n":
                    print("What are you doing here?!? You lazy wench! Get out!"+ '\n')
                    cityentrance()
                elif lenovo== "use form":
                    if inventory.form==True:
                        print("The King sent you! I have something better! Here's a 'pokeball'! You can 'use' it on the beast. Godspeed."+ '\n')
                        cityentrance()
                        event.armour1= True
                    elif inventory.form== False:
                        print("You don't have a form")
                        bazaar()
                elif lenovo == 'exit':
                    print('goodbye!'+ '\n')
                    exit()
                else:
                    print('Print Something real'+ '\n')
            elif event.armour1== True:
                print("I won't give you anything else for that form. The pokeball is my best invention \n")
                cityentrance()

def bazaar():
    print("Here in the bazaar there are a plethora of shops including a 'food stop', a 'shoe maker', a 'horse stable', 'blacksmith', or you can 'leave' to the city entrance "+ '\n')
    while True:
        pleth= input(">>").strip().lower()
        if pleth== 'food stop':
            foodsto()
        elif pleth== "shoe maker":
            shoemake()
        elif pleth== 'blacksmith':
            blacksmit()
        elif pleth == 'horse stable':
            horsie()
        elif pleth== "leave":
            cityentrance()
        elif pleth== 'exit':
            exit()
        else:
            print('Type something real'+ '\n')

def foodsto():
    while True:
        if event.foodshopfavor== False:
            print("Feeling a bit hungry? We have food here that you can pay with coins or do us a favor")
            print('Would you like to do us a "favor" or "pay"?'+ '\n')
            miggs= input(">>").strip().lower()
            if miggs== 'favor':
                print("We need you to go and fetch some special grass from a field far from here"+ '\n')
                event.foodshopfavor=True
                bazaar()
            elif miggs== 'pay':
                print('Our policy is that you must pay before due to recent robberies')
                print("You don't have money? You can always do us a favor. Would you like to do us a 'favor'? y'n"+ '\n')
                rob= input(">>").strip().lower()
                if rob== 'y':
                  event.foodshopfavor=True
                  bazaar()
                  print("We need you to go and fetch some special grass from a field far from here"+ '\n')
                elif rob== 'favor':
                  event.foodshopfavor=True
                  print("We need you to go and fetch some special grass from a field far from here"+ '\n')
                  bazaar()
                else:
                    print("Sorry, you don't have money.I'll have to ask you to leave"+ '\n')
                    bazaar()
        elif event.foodshopfavor== True:
            if inventory.grass== False:
                print("Come back once you have collected the grass"+ '\n')
                bazaar()
            elif inventory.grass== True:
                if inventory.ring==  False:
                    print("Oh, you have a lot of grass for us. Come by anytime.")
                    print("Also let us give you this 'ONE RING' The poem on it says:\n\n")
                    print("One Ring to rule them all, One Ring to find them,\nOne Ring to bring them all and in the darkness bind them.\n\n")
                    event.rule=True
                    inventory.ring= True
                    bazaar()
                elif inventory.ring== True:
                    print("Hey! Thanks for all the grass! It's coming in handy!"+ '\n')
                    bazaar()
            inventory.sword=True

def horsie():
    if inventory.mahogany==False:
        print('You walk into the stable and stumble over a "beam" on the way in. But alas, you are safe')
    elif inventory.mahogany== True:
        print("You walk into a stable where there is a man who talks with you.\n")
    while True:
        if inventory.rapidash==False:
            if event.hors==False:
                print("Would you like a horse? y/n? You can always 'leave' if you don't"+ '\n')
                horses= input(">>").strip().lower()
                if horses== 'y':
                    print("It'll cost you a lot. I don't think you can afford it. Only the king's men can."+ '\n')
                    print("How will you be paying?")
                    bana= input(">>").strip().lower()
                    if inventory.form==True:
                        if bana== 'use form':
                            print("Oh! You are with the king. I have a mission for you too")
                            print("Then I'll give you a mighty steed")
                            print("I need you to give me a sword"+ '\n')
                            event.hors=True
                            bazaar()
                        elif bana== "form":
                            print("Oh! You are with the king. I have a mission for you too")
                            print("Then I'll give you a mighty steed")
                            print("I need you to give me a sword"+ '\n')
                            event.hors=True
                            bazaar()
                    elif inventory.form==False:
                        if bana== 'form':
                            print("You don't seem to have one of those")
                        elif bana== 'gold':
                            print("Oh, you don't seem to have enough gold.")
                            print("I'm going to have to ask you to leave without a 'form' from the king")
                        else:
                            print("I'm sorry, we don't accept that type of currency. Only a 'form' from the king or gold\n")
                            bazaar()
                elif horses== 'n':
                    print("alright. That's cool."+ '\n')
                    bazaar()
                elif horses== 'leave':
                    bazaar()
                elif horses== 'use form':
                    if inventory.form==True:
                        print("Oh! You are with the king. I have a mission for you too")
                        print("Then I'll give you a mighty steed")
                        print("I need you to give me a sword"+ '\n')
                        event.hors=True
                        bazaar()
                elif horses== 'take beam':
                    inventory.mahogany=True
                    print("You've taken some fine wood. It's made of mahagony"+ '\n')
            elif event.hors==True:
                print("Do you have the sword yet? y/n? If you don't. You can 'leave' and come back when you do")
                horses= input(">>").strip().lower()
                if horses== 'y':
                    if inventory.sword==True:
                        print("Oh. Here's my 'Rapidash' I'll miss her. But she's yours to use. Defeat the Beast"+ '\n')
                        inventory.rapidash=True
                        bazaar()
                    elif inventory.sword==False:
                        print("LIES! BRING ME A SWORD! I need a sword"+ '\n')
                        bazaar()
                elif horses== 'n':
                    print("Awh. Please bring me a sword"+ '\n')
                elif horses== 'take beam':
                    inventory.mahogany=True
                    print("You've taken some fine 'wood'. It's made of mahagony"+ '\n')
                elif horses== 'leave':
                    bazaar()
                elif horses == 'exit':
                    print('goodbye!'+ '\n')
                    exit()
                else:
                    print('Print Something real'+ '\n')
        elif inventory.rapidash==True:
            print("Deep appreciation for the sword. Have fun Rapidash. Defeat the beast.\n")
            bazaar()

def shoemake():
    print("Need a  pair of 'shoes'?")
    print("Or a 'secret tunnel'?")
    while True:
        secret= input(">>").strip().lower()
        if secret== 'shoes':
            print("You don't want to save the princess? Fine. I don't want to help you"+ '\n')
            bazaar()
        elif secret== "secret tunnel":
            if inventory.rapidash==True:
                if inventory.pokeball==True:
                    print("I'll let you into this secret tunnel in the back. From there, you are on your own"+ '\n')
                    tunnel()
                elif inventory.pokeball== False:
                    print("I don't think you'll make it from here without something else. I don't want you to die. Go forth and something to catch the beast"+ '\n')
                    bazaar()
            elif inventory.rapidash== False:
                print("I don't think you'll make it from here without something else. I don't want you to die. Go forth and get something to catch the beast"+ '\n')
                bazaar()
        elif secret=='exit':
            print('goodbye!'+ '\n')
            exit()
        else:
            print('Either choose between the "shoes" and "secret tunnel"'+ '\n')

def blacksmit():
    while True:
        if event.blacksmithfavor1==False:
            if inventory.sword== False:
                print("Need to buy a sword? y/n?"+ '\n')
                swordie= input(">>").strip().lower()
                if swordie== 'y':
                    print("It'll cost you " + str(bob[2]) +" pieces of gold.")
                    print("If you don't have money, you can always do me a favor")
                    print("Would you like to do me a 'favor' or 'pay'?"+ '\n')
                    shamon= input(">>").strip().lower()
                    if shamon== 'favor':
                        print("I need you to get me a fine piece of wood. It needs to be very fine indeed"+ '\n')
                        event.blacksmithfavor1=True
                        bazaar()
                    elif shamon== 'pay':
                        print("You'll need to pay up front. We've been having difficulties lately")
                        print("Oh, you don't have any money? You should get some or do us a favor"+ '\n')
                        bazaar()
                    elif shamon == 'exit':
                        print('goodbye!'+ '\n')
                        exit
                    else:
                        print('Print Something real'+ '\n')
                elif swordie== 'n':
                    print("I'll have to ask you to leave then")
                    bazaar()
                elif swordie == 'exit':
                      print('goodbye!'+ '\n')
                      exit()
                else:
                      print('Print Something real'+ '\n')
        elif event.blacksmithfavor1== True:
            if inventory.sword==False:
                if inventory.mahogany== True:
                    print("Thanks for the wood. Here's a sword"+ '\n')
                    inventory.sword=True
                    bazaar()
                elif inventory.mahogany==False:
                    print("Please bring me back some wood and you'll get a sword"+ '\n')
                    bazaar()

            elif inventory.sword== True:
                print("Thanks for everything you've done for me")
                print("I have a lot of work to do though. I'm going to ask you to go"+ '\n')
                bazaar()


def tunnel():
    print("You're deep in the tunnel ")
    print("You hear a noise at the end", end="")
    ellip()
    print("You see a light at the end and approach the end", end="")
    ellip()
    print('\n')
    battletalk()

def battletalk():
    print("You see a lady sitting by herself in the middle.")
    print("Suddently! She pops up and screams:")
    print("I CHALLENGE YOU TO A MATCH!")
    while True:
        print("Do you accept? y/n")
        match= input(">>").strip().lower()
        if match== 'y':
            battlefield()
        elif match== 'n':
            print("Too bad! I'm not letting you leave until you face me and Charizard")
            battlefield()
        elif match == 'exit':
            print('You scaredy cat')
            exit()
        else:
            print("type something real")

attack= ["inferno", "fury attack", "stomp", "Flair blitz"]
def battlefield():
    print("\n\nA wild charizard appears controlled by the princess")
    print("What do you like to do?")
    print(["fight", "item", "switch", "run"])
    while True:
        eel=input(">>").strip().lower()
        if eel== "fight":
            print("What attack would you like to use?")
            print(["inferno", "fury attack", "stomp", "Flair blitz"])
            attacks= input(">>").strip().lower()
            if attacks== "inferno":
                print("Rapidash used inferno on Charizard!\n")
                print("What do you like to do?")
                print(["fight", "item", "switch", "run"])
            elif attacks== "fury attack":
                print("Rapidash used fury attack on Charizard! \n")
                print("What do you like to do?")
                print(["fight", "item", "switch", "run"])
            elif attacks== "stomp":
                print("Rapidash used stomp on Charizard!\n")
                print("What do you like to do?")
                print(["fight", "item", "switch", "run"])
            elif attacks== "flair blitz":
                print("Rapidash used flair blitz on Charizard!\n")
                print("What do you like to do?")
                print(["fight", "item", "switch", "run"])
            else:
                print("You don't have that move\n")
                print("what would you like to do?")
                print(["fight", "item", "switch", "run"])
        elif eel== "item":
            print("What item would you like to use?")
            if inventory.ring==True:
                print("'pokeball', 'One Ring'")
            else:
                print("'pokeball'")
            pokes= input(">>").strip().lower()
            if pokes== "pokeball":
                print("You threw a pokeball")
                ellip(), ellip()
                print("It worked!")
                battleover()
            elif pokes== 'use pokeball':
                print("You threw a pokeball")
                ellip(), ellip()
                print("It worked!\n")
                battleover()
            elif pokes== 'use ring':
                print("You put on the 'One Ring' and become invisible to the other trainer")
            else:
                print("That's not a possible command.")
        elif eel== "switch":
            print("You don't seem to have any other pokemon to swtich with")
            print("\nWhat do you like to do?")
            print(["fight", "item", "switch", "run"])
        elif eel== "run":
            print("The princess screams at you that you can't leave this battle as Charizard guards the exit")
            print("\nWhat do you like to do?")
            print(["fight", "item", "switch", "run"])
        else:
            print("That's not a possible command.")

def battleover():
    while True:
        print("You've powered up the time machince with Charizard's mighty fire power")
        print("You may now enter the next time period")
        print("would you like to 'leave' to the next time period or go back into the 'city'?")
        event.savedprincess=True
        final= input(">>").strip().lower()
        if final== 'leave':
            print("That was fun. Now let's travel to the second millenium!")
            os.system('modernday.py 1')
            exit()
        elif final== 'city':
            cityentrance()
        else:
            print("Please type a real command")

grassyplain()
