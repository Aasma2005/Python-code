l = []

while True:

    c = int(input('''
1. Push element
2. Pop element
3. Peek element
4. Display stack
5. Exit

Enter your choice: '''))

    if c == 1:
        n = input("Enter the value: ")
        l.append(n)
        print("Stack:", l)

    elif c == 2:
        if len(l) == 0:
            print("Empty stack")
        else:
            p = l.pop()
            print("Popped element:", p)
            print("Stack:", l)

    elif c == 3:
        if len(l) == 0:
            print("Empty stack")
        else:
            print("Last stack value:", l[-1])

    elif c == 4:
        print("Display stack:", l)

    elif c == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")