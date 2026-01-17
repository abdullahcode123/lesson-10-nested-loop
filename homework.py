
num = int(input("Enter a decimal number: "))
binary = ""

while num > 0:           
    remainder = num % 2
    num = num // 2

    for i in range(1):   
        binary = str(remainder) + binary

print("Binary number is:", binary)