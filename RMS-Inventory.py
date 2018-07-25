import pickle

inventory = pickle.load(open('DO_NOT_TOUCH_INVENTORY.txt', 'rb'))

def fixtures(entered):
    entered = str(input("Options: add, find")).lower()

def items(entered) :
    #while the user hasn't entered "exit", keep the program running
    while (entered != "exit" and entered != "e") :
        
        #if the user entered "add"
        if (entered == "add" or entered == "a") :
            #get more responses to add to the dictionary
            name = str(input("Enter the name of the item to add ")).lower()
            location = str(input("Enter the location of the item (room.zone.row.description): ")).lower()
            #add the new item
            inventory[name] = location
            
        elif (entered == "print" or entered == "p") :
            #this just displays everything in the inventory
            print(inventory)
            
        elif (entered == "delete" or entered == "d") :
            #get the name of the item and make it lowercase
            name = str(input("Enter the name of the item to delete ")).lower()
            #delete from the dictionary inventory the item with that name
            del(inventory[name])
            
        elif (entered == "change" or entered == "c") :
            name = str(input("Enter the name of the item to change ")).lower()
            if name in inventory:
                location = str(input("Enter the new location of " + name + ": ")).lower()
                inventory[name] = location
            else:
                print("Couldn't find that, try something else, or add an item")
                
        elif (entered == "open the pod bay doors, hal") :
            #just having some fun
            print("I'm sorry Dave, I'm afraid I can't do that")
            
        else:
            #in this case, we are searching for an item
            name = entered
            if name in inventory:
                print("The location of " + name + " is " + inventory[name])
            else :
                print("That doesn't exist, try another name for the item or add an item")

        #runs every loop
        pickle.dump(inventory, open("DO_NOT_TOUCH_INVENTORY.txt", "wb"))
        entered = str(input("Options:  add, change, delete, print, exit ")).lower()

#initial input
entered = str(input("Options: add, change, delete, print, exit, or just enter the name of the item to find (for fixtures enter ! then the number ex. !9999) ")).lower()
if (entered[:1] == "!") :
    #call the fixtures program with everthing but the !
    fixtures(entered[1:])
else :
    #call the items function with the input
    items(entered)
