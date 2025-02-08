# Quantity Discount Calculator
# Date: January 20, 2025
# CSC121 m1Lab1 – Review
# Michael Odoom

# Pseudocode:
# 1. Start the program.
# 2. Define the cost per item based on the quantity:
#   - 1–19 items: $4.75 per item
#   - 20–49 items: $4.50 per item
#   - 50–99 items: $4.25 per item
#   - 100 or more items: $4.00 per item
# 3. Prompt the user to enter the number of items they wish to purchase.
# 4. Validate the input to ensure it is a positive number.
# 5. Determine the cost per item based on the quantity.
# 6. Calculate the total cost by multiplying the quantity by the cost per item.
# 7. Display the cost per item and the total cost to the user.
# 8. Ask the user if they want to run the program again.
# 9. If the user enters 'No', terminate the program.
# 10. If the user enters anything other than 'No', repeat the process.

def main():
    # Loop to allow the user to run the program multiple times
    run_again = 'Yes'
    while run_again.lower() != 'no':
        # Prompt the user for the number of items
        quantity = int(input("Enter the number of items: "))

        # Validate the input
        if quantity < 0:
            print("Please enter a positive number.")
            continue  # Skip the rest of the loop and prompt again

        # Determine the cost per item based on the quantity
        if 1 <= quantity <= 19:
            cost_per_item = 4.75
        elif 20 <= quantity <= 49:
            cost_per_item = 4.50
        elif 50 <= quantity <= 99:
            cost_per_item = 4.25
        elif quantity >= 100:
            cost_per_item = 4.00
        else:
            print("Invalid input. Please enter a positive number.")
            continue  # Skip the rest of the loop and prompt again

        # Calculate the total cost
        total_cost = quantity * cost_per_item

        # Display the results
        print(f"Cost per item: ${cost_per_item:.2f}")
        print(f"Total cost: ${total_cost:.2f}")

        # Ask the user if they want to run the program again
        run_again = input("Do you want to run the program again? (Yes/No): ")

    print("Thank you for using the Quantity Discount Calculator!")

# Call the main function to run the program
if __name__ == "__main__":
    main()