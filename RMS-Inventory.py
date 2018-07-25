#load text document with inventory into the program
file = open('DO_NOT_TOUCH_INVENTORY.txt', 'r')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#put code for reading text document into dictionary here
inventory = {
}

def fixtures(entered):
    entered = str(input("Options: find, add")).lower()

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
        if (entered == "print" or entered == "p") :
            print(inventory)
        if (entered == "delete" or entered == "d") :
            #get the name of the item and make it lowercase
            name = str(input("Enter the name of the item to delete ")).lower()
            #delete from the dictionary inventory the item with that name
            del(inventory[name])
        if (entered == "change" or entered == "c") :
            name = str(input("Enter the name of the item to change ")).lower()
            if name in inventory:
                location = str(input("Enter the new location of " + name + ": ")).lower()
                inventory[name] = location
            else:
                print("Couldn't find that, try something else, or add an item")
        if (entered == "open the pod bay doors, hal") :
            print("I'm sorry Dave, I'm afraid I can't do that")
        else:
            name = entered
            if name in inventory:
                print("The location of " + name + " is " + inventory[name])
            else :
                print("That doesn't exist, try another name for the item or add an item")
        entered = str(input("Options: find, add, change, delete, print, exit ")).lower()

entered = str(input("Options: add, change, delete, print, exit ")).lower()
if (entered[:1] == "!") :
    fixtures(entered[1:])
else :
    items(entered)
