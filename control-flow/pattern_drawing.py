# size = int(input("Enter the size of the pattern: "))

# for i in range(size):
#     for j in range(size):
#       print("*", end="")
#     print()

size = int(input("Enter the size of the pattern: "))

i = 0
while i < size:
    j = 0
    while j < size:
        print("*", end="")
        j += 1
    print()
    i += 1