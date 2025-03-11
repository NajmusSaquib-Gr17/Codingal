number = float(input("Enter a Number Greater than 50: "))

if number <= 50:
    print("Please Enter A Number Greater than 50")
else:
    if number %2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")