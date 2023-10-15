# Area Volume Calculator
# Stephen Sullivan (100526624)
# TPRG2131
# October 15th 2023 
# This program is strictly my own work. Any material 
# beyond course learning materials that is taken from 
# the Web or other sources is properly cited, giving 
# credit to the original author(s). 
# The program calculates area or volume of different
# shapes. the program has a two level menu


# Importing necessary libraries
from math import pi

# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if length <= 0 or width <= 0:
        return "Invalid Input", ""
    # Calculate the area and round the result to 2 decimal places
    area = round(length * width, 2)
    return area, "m²"  # returns the value along with the unit

# Main Program
def main():
    show_formula = False
    # Infinite loop for the Level 0 menu
    while True:
        print("\nA/V Calculator Menu \n\n(Level 0)")
        print("Enter Q/q to quit.")
        print("Enter V/v to change the calculated view or D/d for default view.")
        choice = input("Enter your choice: ").strip().lower()

        if choice in ['q']:
            print("Exiting...")
            break
        elif choice in ['v']:
            show_formula = True
        elif choice in ['d']:
            show_formula = False
        else:
            continue

        # Infinite loop for the Level 1 menu-driven program
        while True:
            if show_formula:
                # Display formulas
                print("\n(Level 1 with formulas)")
                print("1. Area of Rectangle (length x width)")
                print("Enter Q/q to return to Level 0.")
            else:
                # Display without formulas
                print("\nA/V Calculator Menu (Level 1)")
                print("1. Area of Rectangle")
                print("Enter Q/q to return to Level 0.")

            choice = input("> ").strip().lower()

            if choice == 'q':
                break
            elif choice == '1':
                length = float(input("\nEnter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                result = area_of_rectangle(length, width)
                print(f"\nArea of Rectangle: {result[0]} {result[1]}\n")
            else:
                print("\nInvalid choice! Please choose again.")

# Ensure the main program is run when the script is executed directly
if __name__ == "__main__":
    main()

                