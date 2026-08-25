l = []

while True:

    c = int(input('''
1. Enqueue element
2. Dequeue element
3. Front element
4. Last element
5. Display Queue
6. Exit

Enter your choice: '''))

    if c == 1:
        n = input("Enter the value: ")
        l.append(n)
        print("Queue:", l)

    elif c == 2:
        if len(l) == 0:
            print("Empty Queue")
        else:
            p = l.pop(0)
            print("Dequeued element:", p)
            print("Queue:", l)

    elif c == 3:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Front element:", l[0])

    elif c == 4:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Last element:", l[-1])

    elif c == 5:
        print("Display Queue:", l)

    elif c == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")