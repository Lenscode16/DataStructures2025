# Example of Stack Program LIFO (Last In, First Out) - Plate Stack

plate_stack = []  # Create an empty stack for plates

# Function to add a plate to the stack (push operation)
def push_plate():
    plate = input("Enter the type of plate (e.g., Dinner Plate, Salad Plate): ")
    plate_stack.append(plate)
    print(f"Plates in stack: {plate_stack}")

# Function to remove the last plate from the stack (pop operation)
def pop_plate():
    if not plate_stack:  # Check if the stack is empty
        print("No plates left in the stack!")
    else:  # If there are plates in the stack
        removed_plate = plate_stack.pop()
        print(f"Removed plate: {removed_plate}")
        print(f"Plates in stack: {plate_stack}")

# The program will continue until the user selects operation 3 to quit
limit = int(input("Enter the limit of your plate stack: "))  # Limit on number of plates

while True:
    print("\nSelect operation 1. Add Plate (Push), 2. Remove Plate (Pop), 3. Quit")
    choice = int(input())

    if choice == 1:
        if len(plate_stack) < limit:
            push_plate()
        else:
            print("The stack is full! You cannot add more plates.")
    elif choice == 2:
        pop_plate()
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Please enter a valid operation (1, 2, or 3).")
