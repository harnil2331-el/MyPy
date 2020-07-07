a = int(input("enter no of row"))

b = int(input("enter 0 or 1"))
c = bool(b)
if c == True:

    for i in range(a):
        for j in range(i):
            print("* ", end=" ")
        print()

elif c == False:

    for i in range(a):
        for j in range(a - i):
            print("* ", end="")
        print()
