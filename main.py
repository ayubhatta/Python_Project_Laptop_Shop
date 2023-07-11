''' Importing functions and classes from other modules'''
from operation import purchase_laptop, sell_laptop
from write import write_purchase_details, write_sold_details

def print_menu():
    # Displays the shop's name, address, and contact details
    print("\n")
    print("*************************************************************")
    print("******\t\t\tAyub's Laptop Shop💻           ******")
    print("*************************************************************")
    print("******\t\t  Address: Dillibazar, Kathmandu       ******")
    print("******\t\t      Contact: 9863589173📞            ******")
    print("*************************************************************")
    print("\n")
    
    # Displays the menu options asking the user what they want to do
    print("********************************")
    print("** What would you like to do? **")
    print("********************************")
    print("1. Purchase a laptop from the manufacturer.")
    print("2. Sell a laptop to the customer.")
    print("3. Exit the shop!")
    print("\n")

def get_menu_choice():
    while True:
        try:
            # Prompts the user to enter their choice
            choice = int(input("\nPlease enter your choice (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                # Returns the choice if it is valid (1, 2, or 3)
                return choice
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def perform_purchase():
     # Calls the purchase_laptop function to perform the purchase
    name, phone, date_time, laptops_purchased, vat_amount, final_total = purchase_laptop()
    
     # Calls the write_purchase_details function to record the purchase details
    write_purchase_details(name, phone, date_time, laptops_purchased, vat_amount, final_total)
    
     # Prints a success message
    print("Purchase from the manufacturer completed successfully!")


def perform_sale():
    # Calls the sell_laptop function to perform the sale
    name, phone, date_time, laptops_purchased, cost_of_shipping, final_total = sell_laptop()
    
    # Calls the write_sold_details function to record the sale details    
    write_sold_details(name, phone, date_time, laptops_purchased, cost_of_shipping, final_total)
    
    # Prints a success message
    print("Sale to the customer completed successfully!")

print_menu()

while True:
    choice = get_menu_choice()

    if choice == 1:
        perform_purchase()
    elif choice == 2:
        perform_sale()
    elif choice == 3:
        print("Thank you for visiting Ayub's Laptop Shop! Have a great day!")
        break
