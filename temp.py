i = 0

while i < 3:
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")

    try:
        num1 = float(number1)
        num2 = float(number2)
    except:
        print("invalid character entered")
        i = i + 1
    else:
        sum = num1 + num2
        print(sum)
        break
        