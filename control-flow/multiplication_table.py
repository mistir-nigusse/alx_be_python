X = input("Enter a number to see its multiplication table: ")
list = [1,2,3,4,5,6,7,8,9,10]

for Y in range(1,11):
    Z = int(X) * Y
    print(f"{X} * {Y} = {Z}")