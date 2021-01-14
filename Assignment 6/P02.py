# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 8/2/20
# Description: Management System
# Assignment # - 6

##### Template for Assignment X, problems 1-X ######

def main():
    # product lists
    product_names = ["hamburger", "cheeseburger", "small fries"]
    product_costs = [0.99, 1.29, 1.49]

    # prompt user to either "search" or "quit"
    choice = input("(s)earch for product or (q)uit: ")

    # Management system continues while user doesn't "quit"
    while choice != "q":
        # if the user want to "search"
        if choice == "s":
            # Prompt user for the inquired food's name
            food = input("Enter a product name: ")

            # If the food was in the product list, display the price
            if food in product_names:
                # find index of the food in the "products list"
                product_index = product_names.index(food)

                # find the price of the product
                price = product_costs[product_index]

                # display the product's price
                print("We sell \"", food, "\" at", price, " per unit")

            # Otherwise, the requested food is not available
            else:
                print("Sorry, we don't sell", food)

        # Otherwise, the user is prompted for another option
        else:
            print("Invalid option, try again")

        # prompt user again to either "search" or "quit"
        choice = input("\n(s)earch for product or (q)uit: ")

    # Management System ends
    print("See you soon!")

# Run main program
main()
