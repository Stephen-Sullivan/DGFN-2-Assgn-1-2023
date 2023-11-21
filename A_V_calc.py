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

# This section uses the round function
# I found this on the python website
# https://docs.python.org/2/library/functions.html#round

# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if length <= 0 or width <= 0:
        return "Invalid Input", ""
    # Calculate the area and round the result to 2 decimal places
    area = round(length * width, 2)
    return area, "m²"  # returns the value along with the unit

# Function to calculate the volume of a cylinder
def volume_of_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        return "Invalid Input", ""
    # Calculate the volume and round the result to 2 decimal places
    volume = round(pi * (radius ** 2) * height, 2)
    return volume, "m³"

# Function to calculate the area of a triangle
def area_of_triangle(base, height):
    if base <= 0 or height <= 0:
        return "Invalid Input", ""
    # Calculate the area and round the result to 2 decimal places
    area = round(0.5 * base * height, 2)
    return area, "m²"

# Function to calculate the volume of a sphere
def volume_of_sphere(radius):
    if radius <= 0:
        return "Invalid Input", ""
    # Calculate the volume and round the result to 2 decimal places
    volume = round((4/3) * pi * (radius ** 3), 2)
    return volume, "m³"

# Function to calculate the volume of a cone
def volume_of_cone(radius, height):
    if radius <= 0 or height <= 0:
        return "Invalid Input", ""
    # Calculate the volume and round the result to 2 decimal places
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/volume-of-a-cone
    volume = round((1/3) * pi * (radius ** 2) * height, 2)
    return volume, "m³"

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
                print("2. Volume of Cylinder (pi x radius^2 x height)")
                print("3. Area of Triangle (0.5 x base x height)")
                print("4. Volume of Sphere (4/3 x pi x radius^3)")
                print("5. Volume of Cone (1/3 x pi x radius^2 x height)")
                print("Enter Q/q to return to Level 0.")
            else:
                # Display without formulas
                print("\nA/V Calculator Menu (Level 1)")
                print("1. Area of Rectangle")
                print("2. Volume of Cylinder")
                print("3. Area of Triangle")
                print("4. Volume of Sphere")
                print("5. Volume of Cone")
                print("Enter Q/q to return to Level 0.")

            choice = input("> ").strip().lower()

# F-strings are used in the following section
# https://docs.python.org/3/tutorial/inputoutput.html

            if choice == 'q':
                break
            elif choice == '1':
                length = float(input("\nEnter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                result = area_of_rectangle(length, width)
                print(f"\nArea of Rectangle: {result[0]} {result[1]}\n")
            elif choice == '2':
                radius = float(input("\nEnter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                result = volume_of_cylinder(radius, height)
                print(f"\nVolume of Cylinder: {result[0]} {result[1]}\n")
            elif choice == '3':
                base = float(input("\nEnter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                result = area_of_triangle(base, height)
                print(f"\nArea of Triangle: {result[0]} {result[1]}\n")
            elif choice == '4':
                radius = float(input("\nEnter the radius of the sphere: "))
                result = volume_of_sphere(radius)
                print(f"\nVolume of Sphere: {result[0]} {result[1]}\n")
            elif choice == '5':
                radius = float(input("\nEnter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                result = volume_of_cone(radius, height)
                print(f"\nVolume of Cone: {result[0]} {result[1]}\n")
            else:
                print("\nInvalid choice! Please choose again.")

# Ensure the main program is run when the script is executed directly
if __name__ == "__main__":
    main()
# testing
