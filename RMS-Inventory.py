#load text document with inventory into the program
file = open('DO_NOT_TOUCH_INVENTORY.txt', 'r')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#put code for reading text document into dictionary here

#take in input and make it a lower case string
entered = str(input("Options: find, add, change, delete, print ")).lower()
#while the user hasn't entered "exit", keep the program running
while (entered != "exit") :
    #if the user entered "add"
    if (entered == "add") :
        #get more responses to add to the dictionary
        name = str(input("Enter the name of the item ")).lower()
        location = str(input("Enter the location of the item (room.shelf.row.column): ")).lower()
        
    entered = str(input("Options: add, change, delete ")).lower()

#just testing github
