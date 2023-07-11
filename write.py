def write_sold_details(name, phone, date_time, laptops_purchased, cost_of_shipping, final_total):
    # Generate the file name based on customer's name and phone number
    file_name = f"{name}_{phone}_sold.txt"

    # Open the file in write mode
    with open(file_name, "w") as file:
        # Write shop details and header
        file.write("*************************************************************\n")
        file.write("******\t\t\tAyub's Laptop Shop                     ******\n")
        file.write("*************************************************************\n")
        file.write("******\t\t  Address: Dillibazar, Kathmandu           ******\n")
        file.write("******\t\t      Contact: 9863589173                  ******\n")
        file.write("*************************************************************\n")

        # Write customer information section
        file.write("-------------------------\n")
        file.write("--Customer Information:--\n")
        file.write("-------------------------------------------------------------\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone Number: {phone}\n")
        file.write(f"Date and Time: {date_time}\n")
        file.write("-------------------------------------------------------------\n\n")

        # Write purchased laptops section
        file.write("----------------------\n")
        file.write("--Purchased Laptops:--\n")
        file.write("--------------------------------------------------\n")
        file.write("Product Name\tTotal Quantity\tUnit Price\tTotal\n")
        file.write("--------------------------------------------------\n")

        # Iterate over each purchased laptop and write its details
        for i, laptop in enumerate(laptops_purchased):
            file.write(f"\n{i+1}\t{laptop[0]},\t\t{laptop[1]},\t\t{laptop[2]},\t{laptop[3]}")
            file.write("\n")

        file.write("--------------------------------------------------\n\n")

        # Write shipping details or total amount section based on cost_of_shipping value
        if cost_of_shipping == 500:
            file.write("---------------------\n")
            file.write("--Shipping Details:--\n")
            file.write("-------------------------------------------------------\n")
            file.write(f"Shipping Cost: {cost_of_shipping}\n")
            file.write(f"Grand Total: ${final_total}\n")
            file.write("-------------------------------------------------------\n")
            file.write("Note: Shipping Cost is added to the total amount\n")
            file.write("-------------------------------------------------\n")
        else:
            file.write("----------\n")
            file.write("--Total:--\n")
            file.write("---------------------------\n")
            file.write(f"Total: ${final_total}\n")
            file.write("---------------------------\n")


def write_purchase_details(name, phone, date_time, laptops_purchased, vat_amount, final_total):
    # Generate the file name based on customer's name and phone number
    file_name = f"{name}_{phone}_purchase.txt"

    # Open the file in write mode
    with open(file_name, "w") as file:
        # Write shop details and header
        file.write("*************************************************************\n")
        file.write("******\t\t\tAyub's Laptop Shop                     ******\n")
        file.write("*************************************************************\n")
        file.write("******\t\t  Address: Dillibazar, Kathmandu           ******\n")
        file.write("******\t\t      Contact: 9863589173                  ******\n")
        file.write("*************************************************************\n")

        # Write customer information section
        file.write("-------------------------\n")
        file.write("--Customer Information:--\n")
        file.write("-------------------------------------------------------------\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone Number: {phone}\n")
        file.write(f"Date and Time: {date_time}\n")
        file.write("-----------------------------------------------------------\n\n")

        # Write purchased laptops section
        file.write("----------------------\n")
        file.write("--Purchased Laptops:--\n")
        file.write("--------------------------------------------------\n")
        file.write("Product Name\tTotal Quantity\tUnit Price\tTotal\n")
        file.write("--------------------------------------------------\n")

        # Iterate over each purchased laptop and write its details
        for i, laptop in enumerate(laptops_purchased):
            file.write(f"\n{i+1}\t{laptop[0]},\t\t{laptop[1]},\t\t{laptop[2]},\t{laptop[3]}")
            file.write("\n")

        file.write("--------------------------------------------------\n\n")

        # Write VAT details or total amount section based on vat_amount value
        if vat_amount:
            file.write("----------------\n")
            file.write("--VAT Details:--\n")
            file.write("--------------------------------\n")
            file.write(f"VAT Amount: ${vat_amount}\n")
            file.write(f"Total (including VAT): ${final_total}\n")
            file.write("--------------------------------\n")
            file.write("Note: VAT Amount added to the grand total\n")
            file.write("------------------------------------------\n")
        else:
            file.write("Total:\n")
            file.write("---------------------------\n")
            file.write(f"Total: ${final_total}\n")
            file.write("---------------------------\n")
