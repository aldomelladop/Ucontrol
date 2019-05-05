

import pickle  # pickle makes it SO easy to load/save data from/to disk.
from collections import OrderedDict


class Item:
    '''
        This class models an Item in a a collection.
        An item has a category, description, value and quantity.
        For example: Antique, Desk, 250.00, 1
    '''

    def __init__(self, category, desc, value, quant):
        '''
           This is the constructor for the Item class. It creates an Item object
           from the parameters passed in by the user.
           Note that self must be used in order to refer to the object's properties

           This constructor should NOT need any modifications
        '''
        self.category = category
        self.desc = desc
        self.value = value
        self.quant = quant

    def __str__(self):
        return self.category + " " + self.desc + " " + str(self.value) + " " + str(self.quant) + " "

    def display(self):
        '''
            This method simply displays the item properties in a nicely formatted manner.

            This method should NOT need any modifications.
        '''
        print("{:<30}{:<18}{:8.2f}{:7d}".format(self.desc, self.category, self.value, self.quant))


class Collection:
    '''
        The Collection class models a collection of Item objects.
        It also provides the methods necessary to display information related to this collection.
    '''

    def __init__(self):
        '''
            This is the constructor for the Collection class. Note that it initializes
            a list. This list will contain Item objects.

            This constructor should NOT need any modifications.
        '''
        self.items = []

    def addItem(self, category, desc, value, quant):
        '''
        This method accepts information about the Item object to create in the parameter list.
        An Item object is created and then added to the list.

        YOU MUST IMPLEMENT THIS METHOD

        item = Item(category, desc, value, quant)
        self.items.append(item)

        '''
        item = Item(category, desc, value, quant)
        self.items.append(item)
        # nodupes = {}
        # while True: 
        #   if item in self.items:
        #   item = nodupes[item]
        # else: 
        #   self.items.append(item)


    def displayAllItems(self):
        '''
        This method displays all the Item objects in a nicely formatted table.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        print("\n{:<30}{:<18}{:<10}{:7}".format('Description', 'Category', 'Value', 'Quantity'))
        print("_" * 65 + "\n")

        for s in self.items:
            s.display()

    def displayAllCategories(self):
        '''
        This method displays all the categories in the collection in a nicely
        formatted table. Note that each category is displayed exactly once.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        print("\n{:<30}".format('Category'))
        print("_" * 40 + "\n")
        for cat_items in self.items:
            print(cat_items.category)
        



    def displayAllItemsForCategory(self, category):
        '''
        This method displays all the item objects that are in the category specified in
        the parameter list. This should be displayed in a nicely formatted table.

        If no items exist for the given category then a message should be displayed to
        the user stating so.

        YOU MUST IMPLEMENT THIS METHOD 
        '''

        
        # for values in self.items:
        #     if category in values.category:
        #         values.display()
        print("\n{:<30}{:<18}".format('Description', 'Category'))
        print("_" * 45 + "\n")
        while True: 
          for _cats in self.items:
            if _cats.category in category: #Needed Values.
              # print("\n{:<30}{:<18}".format('Description', 'Category'))
              # print("_" * 45 + "\n")
              print("{:<30}{:<18}".format(_cats.desc, _cats.category))
              # print(values.desc,('\t\t\t\t\t\t\t') , values.category) 
              # You were printing out the wrong attributes 
            # if _cats.category not in category:
            else:
              print('\nCategory does not exist; please try again\n')
          break
          #forgot to break out of the loop when there were no more values
        # print('Please enter a valid category')

    def displayItemsOverValue(self, value):
        '''
        This method displays all item objects whose value is greater than or equal to the
        value specified in the parameter list.

        These items should be displayed in a nicely formatted table.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        print("\n{:<30}{:<18}{:<10}{:7}".format('Description', 'Category', 'Value', 'Quantity'))
        print("_" * 65 + "\n")

        while True: 
          for _value in self.items:
            if _value.value >= value:
              # print("\n{:<30}{:<18}{:<10}{:7}".format('Description', 'Category', 'Value', 'Quantity'))
              # print("_" * 65 + "\n")
                _value.display()
              # print("{:<30}{:<18}{:<10}{:7}\n".format(_value.desc, _value.category, _value.value, _value.quant))

            else:
                print('\nNo items within that value range.  Please try again\n')
          break



    def displayItemFromDescription(self, desc):
        '''
        This method displays the first occurence of any item object whose description is
        the same as the description specified in the parameter list.

        This item should be displayed in a nicely formatted manner.

        If no item exists with the given description, then an message should be displayed
        stating so.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        
        while True: 
          print("\n{:<30}{:<18}{:<10}{:7}".format('Description', 'Category', 'Value', 'Quantity'))
          print("_" * 65 + "\n")
          for _desc in self.items:
            if _desc.desc == desc:
                # _desc.display()
              print("{:<30}{:<18}{:<10}{:7}\n".format(_desc.desc, _desc.category, _desc.value, _desc.quant))
              break
              
            else: 
              print('\nNo items match that description.  Please try again\n')
          break

    def displayCollectionValue(self):
        '''
        This method should display the total value of the collection.
        The total value of each item is the item's value * the item's quantity.

        YOU MUST IMPLEMENT THIS METHOD 
        '''
        colvalue = 0
        for itemz in self.items: 
          colvalue = colvalue + itemz.value
        print("\nTotal Collection Value")
        print("_"*25 + "\n")
        print("$", colvalue)

# This simple print menu function displays the menu.
# You should NOT need to modify this function.

def printMenu():
    print("")
    print("1. Display all items in my collection")
    print("2. Display all categories of my items")
    print("3. Display all items in a given category")
    print("4. Search for an item by description")
    print("5. Add an new item to my collection")
    print("6. Display all items above a given value")
    print("7. Calculate the total value of my collection")
    print("S. Save to disk")
    print("L. Load data from disk")
    print("Q. Quit")
    print()


# This is the main function that drives the program
# This function will be called when you run the program
# You should NOT need to modify this main function.
#
# This function is already implemented to display the menu,
# get input from the user and call the appropriate Collection class methods

def main():
    stuff = Collection()
    print()
    print('Welcome to my Collection Manager')
    while True:
        printMenu()
        selection = input("Please enter a selection: ").strip().upper()
        if selection not in ['1', '2', '3', '4', '5', '6', '7', 'S', 'L', 'Q']:
            print("Please enter a valid choice...")
            continue
        if selection == '1':
            stuff.displayAllItems()
        elif selection == '2':
            stuff.displayAllCategories()
        elif selection == '3':
            category = input("Enter category: ").strip()
            stuff.displayAllItemsForCategory(category)
        elif selection == '4':
            itemToFind = input("Enter item's description: ").strip()
            stuff.displayItemFromDescription(itemToFind)
        elif selection == '5':
            cat = input("Enter the item's category: ").strip()
            desc = input("Enter the item's description: ").strip()
            value = eval(input("Enter the item's value: "))
            quant = eval(input("Enter the item's quantity: "))
            stuff.addItem(cat, desc, value, quant)
            print("Item added")
        elif selection == '6':
            value = eval(input("Enter the value: "))
            stuff.displayItemsOverValue(value)
        elif selection == '7':
            stuff.displayCollectionValue()
        elif selection == 'S':
            pickle.dump(stuff, open("stuff.p", "wb"))
            print("Data saved...")
        elif selection == 'L':
            stuff = pickle.load(open("stuff.p", "rb"))
            print("Data loaded...")
        else:
            print("Thanks for using my Collection Manager")
            break


# This line of code runs the main function above automatically when you run the program.

if __name__ == "__main__":
    main()
