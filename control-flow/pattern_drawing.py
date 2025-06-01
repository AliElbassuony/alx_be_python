number = int(input("Enter the size of the pattern:"))
count = number
while count > 0:
    for i in range(0,number):
        print("*", end="")
    print()
    count -= 1

