def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the start number: "))
b = int(input("Enter the end number: "))

for square in squares(a, b):
    print(square)