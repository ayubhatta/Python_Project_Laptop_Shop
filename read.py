def read_A_File():
    # Initialize an empty dictionary to store laptop information
    laptop_dict = {}
    # Open the file "Laptop.txt" in read mode
    with open("Laptop.txt", "r") as file:
        # Iterate over each line in the file
        for laptop_id, line in enumerate(file, start=1):
            # Remove leading/trailing whitespaces from the line
            line = line.strip()
            # Split the line using comma as the separator
            laptop_details = line.split(",")
            # Add laptop details to the dictionary using laptop_id as the key
            laptop_dict[laptop_id] = laptop_details
    # Return the dictionary containing laptop information
    return laptop_dict
