#Example of Stack progran FILO
student = []#make an empty stack
#function to add element to the stack
def push():
    len(student)=n
    name=input("Enter name of student: ")
    student.append(name)
    print(student)
def pop():#function to eliminate the last element in the stack
    if not student:#if the element is not found in the stack
        print("Name is not found.")
    else:#if the element is in the stack
        e = student.pop()
        print("removed name:", e)
        print(student)
#The program will continue to run until the user select the operation 3.
n = int(input("Enter the limit of your stack: "))#the limit of elements you can put in your stack.
while True:
    print("Select operation 1. push, 2. pop, 3. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Please enter the correct operation!")

