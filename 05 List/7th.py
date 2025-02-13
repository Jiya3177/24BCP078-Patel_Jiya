# Write a menu-driven program to implement the stack data structure

stack = []

def main():
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. trewerse")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            push()
        elif choice == "2":
            pop()
        elif choice == "3":
            display()
        elif choice == "4":
            traverse()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def is_empty():
    return len(stack) == 0

def push():
    item = int(input("Enter the item to push: "))
    stack.append(item)
    print("Item pushed successfully.")

def pop():
    if is_empty ():
        print("Stack is empty.")
    else:
        item = stack.pop()
        print(f"Item popped: {item}")

def display():
    print("Stack elements: ", stack)

def traverse():
    if is_empty():
        print("Stack is empty.")
    else:
        c = len(stack) -1
        while c >= 0:
            print(stack[c])
            c -= 1


main()

