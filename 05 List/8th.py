# Write a menu-driven program to implement the Queue data structur

queue = []
def is_empty():
    return len(queue) == 0
def main():
    while True:
        print("\nQueue Operations:")
        print("1. Check if queue is empty")
        print("2. Add item to queue")
        print("3. Remove item from queue")
        print("4. Display queue")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            if is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == '2':
            enqueue()
        elif choice == '3':
            dequeue()
        elif choice == '4':
            display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
def enqueue():
    item = input("Enter the item to be added to the queue: ")
    queue.append(item)
    print("Item added to the queue.")

def dequeue():
    if not is_empty():
        item = queue.pop(0)
        print("Item removed from the queue: ", item)
    else:
        print("Queue is empty.")

def display():
    if not is_empty():
        print("Queue: ", queue)
    else:

        print("Queue is empty.")

main()