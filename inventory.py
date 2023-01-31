from tabulate import tabulate
#========The beginning of the class==========
#define the shoe object which all shoes will be stored as
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost, and
        ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return int(self.cost)



    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return int(self.quantity)


    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r") as f:
            content =f.readlines()
            for i in range(len(content)):
                line_cont = content[i].split(",")
                line_cont[4] = line_cont[4].rstrip("\n")
                #Code to skip first row
                if line_cont == ["Country", "Code", "Product", "Cost", "Quantity"]:
                    continue
                #append as a class to shoelist
                shoe_list.append(Shoe(line_cont[0], line_cont[1], line_cont[2],
                 line_cont[3], line_cont[4]))
        return shoe_list
    #error except incase file is not present
    except FileNotFoundError:
        print("inventory.txt File not found")
            

# captures shoe data from user and appends to shoelist
def capture_shoes(shoe_list):
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("Enter Country: ")
    code = input("Enter Code: ")
    product = input("Enter Product: ")
    cost = num_input_validation("cost")
    quantity = num_input_validation("quantity")
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    return shoe_list
    

# prints the shoe_list list using tabulate
def view_all(shoe_list):
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    table = []
    for obj in shoe_list:
        table.append([obj.country, obj.code, obj.product,
         obj.cost, obj.quantity])
    print(tabulate(table, headers=["Country", "Code", "Product",
     "Cost", "Quantity"]))
    print("--------------------------------------")


#using alamba key to only compare the quantity value for min
def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    try:
        lowest_qty = min(shoe_list,key=lambda x:x.quantity)
    except ValueError:
        print("error, please read shoe data or capture data and try again")
        return   
    while True:       
        try:
            print(f"lowest quantity item in stock is:")
            class_obj_2_table(lowest_qty)
            print("--------------------------------------")
            choice = input("would your like to add to stock? y/n  ").strip()\
            .lower()
            if choice == "y" or choice == "yes":
                print("--------------------------------------")
                print(f"how much would your like to add to stock?")
                qty_add = int(input(f"{lowest_qty.get_quantity()} units + "))
                update_qty = lowest_qty
                update_qty.quantity = update_qty.get_quantity() + qty_add
                # itteraate over the shoe_list to find original quantity
                # update shoelist
                for i in range(len(shoe_list)):
                    if shoe_list[i] == lowest_qty:
                        shoe_list[i] = update_qty
                        print("--------------------------------------")
                        print( f"item qty updated too: ")
                        class_obj_2_table(update_qty)
                        print("--------------------------------------")
                        #open and write updated shoe list
                        with open("inventory.txt", "w") as f:
                            f.write("Country,Code,Product,Cost,Quantity\n")
                            # use enumerate to count lines
                            for k,j in enumerate(shoe_list):
                                f.write(f"{j.country},{j.code},{j.product}"\
                                    f",{j.cost},{j.quantity}")
                                # make a newline on all but the last line
                                if k < len(shoe_list) - 1:
                                    f.write("\n")
                        print("inventory.txt updated")                        
                        print("--------------------------------------")    
                        break
                    elif choice == "n" or choice == "no":
                        print("returning to menu")
                        print("--------------------------------------")
                        break
        except ValueError:
            print("error, please try again ")            
        except FileNotFoundError:
            print("error, inventory.txt not found")
        # required to get out of while loop
        finally:
            break


# searches for sku in list and returns the shoe object
def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    sku = input("Enter SKU for the shoe you want to view: ")
    try:
        for i in range(len(shoe_list)):
            if shoe_list[i].code.lower().strip() == sku.lower().strip():
                return shoe_list[i]
    except AttributeError:
        if shoe_list == []:
            print("error, shoe data not found")
            print("--------------------------------------")
            return shoe_list
        else:
            print("ERROR, sku not found, try again")
            print("--------------------------------------")       



# creates a table calulating the cost of goods for eeach item
# and the total of all goods
def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # if statement will print error statement informing user to load data
    if shoe_list == []:
        print("ERROR, no inventory data loaded, please load data")

        print("--------------------------------------") 
        return
    # create a empty list to build table in, and hheader list for tablate
    table = []
    total_cost_all = 0
    headers=["Country", "Code", "Product", "Cost (§)", "Qty","Total cost(§)"]
    for i in range(len(shoe_list)):
        # calc total value of item
        total_cost = shoe_list[i].get_cost()*shoe_list[i].get_quantity()
        # calc total of all items
        total_cost_all += total_cost
        # add item to table
        table.append([shoe_list[i].country, shoe_list[i].code,
         shoe_list[i].product, shoe_list[i].cost,
          shoe_list[i].quantity, total_cost])
    # print out table using tablate function, and total of all
    print("TOTAL COST OF INVENTORY ON HAND")
    print(tabulate(table, headers))
    print(f"total value of all goods on hand: §{total_cost_all}")
    print("--------------------------------------")
    

# finds the highest quantity item in the list, prints ir out and
# that it is on sale
def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    try:
        highest_qty = max(shoe_list,key=lambda x:x.quantity)
        class_obj_2_table(highest_qty)
        print("IS ON SALE!")
        print("--------------------------------------")
    except ValueError:
        print("ERROR, please read shoe data or capture data and try again")
        print("--------------------------------------")
        

# funciton which converts single objects into tables and prints 
# for better presentation
def class_obj_2_table(obj):
    table=[]
    try:
        table.append([obj.country, obj.code,
            obj.product, obj.cost,
            obj.quantity])
        headers=["Country", "Code", "Product", "Cost (§)", "Qty",
        "Total cost(§)"]
        print(tabulate(table, headers))
    except AttributeError:
        print("error, shoe data not found, read "\
             "shoe data with 'r' & try again")

# makes sure entries are intergers and keeps asking until interger is provided
def num_input_validation(variable_name):
    while True:
        try:
            num = int(input(f"Enter the {variable_name}: "))
            return num
        except ValueError:
         print(f"{variable_name} must be an integer.")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    print("What would you like to do?\n\
            r - Read shoes data\n\
            c - Capture shoes\n\
            v - View all shoes\n\
            re - Re-stock lowest Qty item\n\
            s - Search a shoe\n\
            i - See inventory value\n\
            h - See the highest Qty item\n\
            e - Exit")
    print("--------------------------------------")
    selection = input("Make a selection: ").lower().strip()
    print("--------------------------------------")
    # read shoes data
    if selection == "r":
        shoe_list = read_shoes_data()
        print("shoe_list created")

    # capture shoes
    elif selection == "c":
        shoe_list = capture_shoes(shoe_list)
    
    # view all shoes
    elif selection == "v":
        view_all(shoe_list)
    
    # re-stock lowest Qty item
    elif selection == "re":
        re_stock()
    
    # search a shoe
    elif selection == "s":
        obj = search_shoe()
        class_obj_2_table(obj)
        print("--------------------------------------")
    # see inventory value
    elif selection == "i":
        value_per_item()
    
    # see the highest Qty item
    elif selection == "h":
        highest_qty()
    
    #exit program
    elif selection == "e" or selection == "exit":
        exit()
    else:
        print("invalid selection, please try again\n\
            type only the letters 'r', 'c', 'v', 're', 's', 'i', 'h' or 'e'")