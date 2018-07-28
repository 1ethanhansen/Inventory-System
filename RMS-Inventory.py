import pickle
from difflib import get_close_matches
import os

#load the saved inventory from the file to a dictionary
inventory = pickle.load(open('DO_NOT_TOUCH_INVENTORY.txt', 'rb'))

def itemSearch(item) :
    if item in inventory:
        #if the name was exact, just print the thing and location
        print("The location of " + item + " is " + inventory[item])
        
    else :
        #create a list of keys
        keys = list(inventory.keys())
        #this finds up the three best matches for the search item in keys
        bestMatches = get_close_matches(item, keys, 3, 0.5)
        
        if len(bestMatches) > 0:
            #print out locations of best matches if there were any
            for guess in bestMatches:
                itemSearch(guess)
                
        else :
            #say we couldn't find anything
            print("Couldn't find anything matching the name '" + item + "'. Try another name or add that item")

def fixtures(entered):
    try :
        #open the info file with the default system program, if it exists
        os.startfile("W:\\WDS\\Inventory\\fixture-docs\\" + entered + ".docx")
        
    except FileNotFoundError:
        #create a new document
        print("That fixture number doesn't exist, either add it or try again")

def items(entered) :
    #while the user hasn't entered "exit", keep the program running
    while (entered != "exit" and entered != "e") :
        #if the user entered "add"
        if (entered == "add" or entered == "a") :
            #get more responses to add to the dictionary
            name = str(input("Enter the name of the item to add ")).lower()
            location = str(input("Enter the location of the item (room.storage.row.description): ")).lower()
            #add the new item
            inventory[name] = location
            
        elif (entered == "print" or entered == "p") :
            #this just displays everything in the inventory
            print(inventory)
            
        elif (entered == "delete" or entered == "d") :
            #get the name of the item and make it lowercase
            name = str(input("Enter the name of the item to delete ")).lower()
            if name in inventory:
                #delete from the dictionary inventory the item with that name
                del(inventory[name])
            else:
                print("Hey you can't delete something that doesn't exist! That's like dividing 0 by 0!")
            
        elif (entered == "change" or entered == "c") :
            name = str(input("Enter the name of the item to change ")).lower()
            if name in inventory:
                location = str(input("Enter the new location of " + name + ": ")).lower()
                inventory[name] = location
            else:
                #create a list of keys
                keys = list(inventory.keys())
                #this finds up the three best matches for the search item in keys
                bestMatches = get_close_matches(name, keys)
                if (len(bestMatches) > 0) :
                    print("Couldn't find that, add an item, or try one of these: ")
                    print(bestMatches)
                else:
                    print("Couldn't find that, add an item, or try again")
                
        elif (entered == "open the pod bay doors, hal") :
            #just having some fun
            print("I'm sorry Dave, I'm afraid I can't do that")

        elif (entered == "is this loss?") :
            #more fun
            print("|\t||\n||\t|_")

        elif (entered == "people sometimes make mistakes.") :
            #Okay okay, last one I promise
            entered = str(input("\nYES THEY DO. SHALL WE PLAY A GAME?\n\n"))
            if (entered == "Love to. How about Global Thermonuclear War?") :
                print("\nWOULDN'T YOU PREFER A GOOD GAME OF CHESS?")
            
        else:
            #in this case, we are searching for an item, look it up in function
            itemSearch(entered)
            
        #runs every loop
        pickle.dump(inventory, open("DO_NOT_TOUCH_INVENTORY.txt", "wb"))
        entered = str(input("\nOptions:  add, change, delete, print, exit ")).lower()

def halp() :
    #named this way because help() is already a python thing
    topic = str(input("\nWhat topic do you want help with? (add, change, delete, print, search, fixtures) or exit ")).lower()

    while (topic != "exit") :
        if (topic == "add" or topic == "a") :
            print("To add a new item, enter 'add' or 'a'. You will then be prompted for the name of the item and then the location")
            print("Here are the rooms for locations: shop, wash, CMM, closet, office, MRB")
            
        elif (topic == "change" or topic == "c") :
            print("To change an existing item, enter 'change' or 'c'. You will then be prompted for the name of the item then the new location")
            
        elif (topic == "delete" or topic == "d") :
            print("To delete an existing item, enter 'delete' or 'd'. You will then be prompted for the name of the item. WARNING: this is irreversable, there is no undo")

        elif (topic == "print" or topic == "p") :
            print("This displays the entirety of the inventory on the screen.")
            
        elif (topic == "search" or topic == "s") :
            print("To search for an item, just enter its name. If that exact name doesn't exist, the system will show the 3 best matches and their locations")

        elif (topic == "fixtures" or topic == "f") :
            print("To do stuff with fixtures, enter the fixture number with an exclamation mark in front (ex. !9999)\nIt will automatically search for the file and display it if it exists")

        else:
            print("I-I-I-I-I'll do almost anything. That you want me toooo. But I can't go for that, no can do")
            
        topic = str(input("\nWhat topic do you want help with? (add, change, delete, print, search, fixtures) or exit ")).lower()

def main() :
    #initial input
    entered = str(input("Options: \nhelp\tadd\tchange\ndelete\tprint\texit\nOr just enter the name of the item to find (for fixtures enter ! then the number ex. !9999) ")).lower()

    while (entered != "exit") :
        if (entered == "help"):
            halp()

        elif (entered[:1] == "!") :
            #call the fixtures program with everthing but the !
            fixtures(entered[1:])
            
        else :
            #call the items function with the input
            items(entered)
            
        entered = str(input("\nOptions: help, add, change, delete, print, exit, or just enter the name of the item to find (for fixtures enter ! then the number ex. !9999) ")).lower()

main()
