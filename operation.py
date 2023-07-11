''' Importing functions and classes from other modules'''
from read import read_A_File
from datetime import datetime

def purchase_laptop():
    '''A function for purchasing a laptop from the manufacturer.'''

    # Initialize an empty list to store purchased laptops' details
    laptops_purchased = []

    # Display a welcome message to the customer
    print("**********************************************************")
    print("***\t\tWelcome to Ayub's Laptop Shop!         ***")
    print("**********************************************************")
    print("Thank you for choosing us.")

    # Prompt the customer for their name and phone number
    print("\nPlease provide your name and phone number for the bill.")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    # Read laptop details from a file using the read_A_File() function
    laptop_dict = read_A_File()

    # Display the available laptops to the customer
    print("\n")
    print("**********************************")
    print("*Here are the available laptops: *")
    print("**********************************")
    print("\n")

    # Display a table with laptop details
    print("---------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("---------------------------------------------------------------------------------------------------------------")

    # Iterate through the laptop dictionary and print each laptop's details
    for laptop_id, laptop_details in laptop_dict.items():
        laptop_name, brand, price, quantity, processor, graphic_card = laptop_details
        print(f"{laptop_id}\t{laptop_name}\t{brand}\t{price}\t{quantity}\t{processor}\t{graphic_card}")
    
    # Initialize a variable to control the purchase loop
    ch = 'y'
    
    # Start a loop to allow the customer to purchase multiple laptops
    while ch.lower() == 'y':

        # Get a valid laptop ID from the customer
        valid_id = get_valid_id(laptop_dict)

        # Get a valid quantity for the selected laptop
        quantity = get_valid_quantity(laptop_dict, valid_id)

        # Update the laptop's quantity in the dictionary and write it back to the file
        update_laptop_quantity(laptop_dict, valid_id, quantity, 1)

        # Retrieve the laptop's details
        laptop = laptop_dict[valid_id]
        laptop_name, brand, price, _, processor, graphic_card = laptop

        # Create a tuple with purchased laptop details and add it to the list
        laptops_chosen = (laptop_name, quantity, price, int(price.strip().replace('$', '')) * quantity)
        laptops_purchased.append(laptops_chosen)

        # Get the current date and time
        date_time = datetime.now()
        
        # Calculate the total price and final total
        total_price = sum(item[3] for item in laptops_purchased)
        vat_amount = calculate_vat(total_price)
        final_total = total_price + vat_amount

        # Ask the customer if they want to order another laptop
        while True:
            try:
                ch = input("Would you like to order another laptop? (Y/N): ")
                if ch.lower() not in ['y', 'n']:
                    raise ValueError("---Invalid input. Please enter 'Y' or 'N'.---")
                print("\n")
                break  # break out of the loop if input is valid
            except ValueError as e:
                print(e)
                print("\n")
    
    # Display the shop's details and the purchase summary to the customer
    print("\n")
    print("*************************************************************")
    print("******\t\t\tAyub's Laptop Shop             ******")
    print("*************************************************************")
    print("******\t\t  Address: Dillibazar, Kathmandu       ******")
    print("******\t\t      Contact: 9863589173              ******")
    print("*************************************************************")
    print("\n")
    print("Laptop Details:")
    print("---------------------")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Date and Time: {date_time}")
    print("----------------------------------------------")

    print("\nPurchase Details:")
    print("---------------------------------------------------------------------------")
    print("Product Name\tTotal Quantity\t\tUnit Price\t\tTotal")
    print("---------------------------------------------------------------------------")
    for laptop in laptops_purchased:
        laptop_name, quantity, unit_price, total = laptop
        print(f"{laptop_name}\t\t{quantity}\t\t{unit_price}\t\t{total}")
    print("---------------------------------------------------------------------------")

    print(f"VAT Amount: {vat_amount}")
    print(f"Grand Total: {final_total}")
    print("Note: VAT Amount added to the grand total")

    # Return the purchase details
    return name, phone, date_time, laptops_purchased, vat_amount, final_total

def get_valid_id(laptop_dict):
    while True:
        try:
            valid_id = int(input('''\nPlease provide the ID of the laptop you want to purchase: '''))
            if valid_id <= 0 or valid_id > len(laptop_dict):
                raise ValueError('''Invalid laptop ID. Please try again.''')
            return valid_id
        except ValueError as e:
            print(e)


def get_valid_quantity(laptop_dict, valid_id):
    while True:
        try:
            quantity = int(input('''Please provide the quantity of the laptop you want to purchase: '''))
            if quantity <= 0:
                raise ValueError('''Invalid quantity. Please enter a positive integer.''')
            available_quantity = int(laptop_dict[valid_id][3])
            if quantity > available_quantity:
                raise ValueError('''Insufficient quantity. Please enter a valid quantity.''')
            return quantity
        except ValueError as e:
            print(e)

def update_laptop_quantity(laptop_dict, valid_id, quantity, operation):
    if operation == 1:
        laptop_dict[valid_id][3] = str(int(laptop_dict[valid_id][3]) + quantity)
    elif operation == 2:
        laptop_dict[valid_id][3] = str(int(laptop_dict[valid_id][3]) - quantity)

    with open("Laptop.txt", "w") as file:
        for laptop_id, laptop_details in laptop_dict.items():
            line = ",".join(laptop_details)
            file.write(f"{line}\n")
     
def calculate_vat(total_price):
    vat_rate = 0.13
    vat_amount = vat_rate * total_price
    return vat_amount



def sell_laptop():
    '''A function for selling a laptop to a customer.'''

    # Initialize an empty list to store sold laptops' details
    laptops_purchased = []

    # Display a message to the customer
    print('''Thank you for selling!''')
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("We will need your name and phone number to print the bill.")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    # Prompt the customer for their name and phone number
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t      Brand \t   Price \t Quantity \t Processor \t Graphic Card")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    # Read laptop details from a file using the read_A_File() function
    a = 1
    laptop_dict = read_A_File()
    for laptop_id, laptop_details in laptop_dict.items():
        laptop_name, brand, price, quantity, processor, graphic_card = laptop_details
        print(f"{a}\t{laptop_name}\t{brand}\t{price}\t{quantity}\t{processor}\t{graphic_card}")
        a += 1
    
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    # Initialize a variable to control the sale loop
    ch = 'y'
    
    # Start a loop to allow the customer to sell multiple laptops
    while ch.lower() == 'y':
    
        # Get a valid laptop ID from the customer
        valid_id = get_valid_id(laptop_dict)

        # Get a valid quantity for the selected laptop
        quantity = get_valid_quantity(laptop_dict, valid_id)

        # Update the laptop's quantity in the dictionary and write it back to the file
        update_laptop_quantity(laptop_dict, valid_id, quantity, 2)

        # Retrieve the laptop's details
        laptop = laptop_dict[valid_id]
        laptop_name, brand, price, _, processor, graphic_card = laptop

        # Create a tuple with sold laptop details and add it to the list
        laptops_chosen = (laptop_name, quantity, price, int(price.strip().replace('$', '')) * quantity)
        laptops_purchased.append(laptops_chosen)

        # Get the current date and time
        date_time = datetime.now()

        # Calculate the total price of purchased laptops
        total_price = sum(item[3] for item in laptops_purchased)
        
        # Set the final total equal to the total price
        f_total = total_price + 0
        
        while True:
            try:
                # Prompt the user if they want to order another laptop
                ch = input("Would you like to order another laptop ? (Y/N) : ")
                if ch.lower() not in ['y', 'n']:
                    # Raise an error for invalid input
                    raise ValueError("---Invalid input. Please enter 'Y' or 'N'.---")
                print("\n")
                # Break out of the loop if input is valid
                break  
            except ValueError as e:
                print(e)
                print("\n")

    # Get the cost of shipping
    cost_of_shipping = get_shipping_cost()
    
    # Calculate the final total by adding the total price and shipping cost
    final_total = f_total + cost_of_shipping

    print("\n")
    print("*************************************************************")
    print("******\t\t\tAyub's Laptop Shop            ******")
    print("*************************************************************")
    print("******\t\t  Address: Dillibazar, Kathmandu       ******")
    print("******\t\t      Contact: 9863589173             ******")
    print("*************************************************************")
    
    print("--------------------")
    print("--Laptop Details: --")
    print("--------------------")
    
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Date and Time: {date_time}")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Sales Details are:")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    for laptop in laptops_purchased:
        laptop_name, quantity, unit_price, total = laptop
        # Print the details of the purchased laptops
        print(f"{laptop_name}\t\t\t{quantity}\t\t\t{unit_price}\t\t\t{total}")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")

    if cost_of_shipping == 500:
        # Print the shipping cost
        print("Shipping Cost:", cost_of_shipping)
        # Print the final total including shipping cost
        print("Grand Total:", final_total)
        #Print the note
        print("Note: Shipping Cost is added to the total amount.")
    else:
        # Print the final total
        print("Grand Total:", final_total)
        print("\n")

    return name, phone, date_time, laptops_purchased, cost_of_shipping, final_total

def get_shipping_cost():
    while True:
        try:
            shipping_choice = input("Dear Customer, do you want your product to be shipped? (Y/N): ")
            if shipping_choice.upper() not in ["Y", "N"]:
                # Raise an error for invalid input
                raise ValueError("Invalid input. Please enter Y or N.")
            # Return 500 if shipping_choice is 'Y', otherwise return 0
            return 500 if shipping_choice.upper() == "Y" else 0
        except ValueError as e:
            # Print the error message for invalid input
            print(e)
            
