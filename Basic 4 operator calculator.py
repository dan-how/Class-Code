
number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter another number: "))

print("Option\n","1 - Add\n", "2 - Subtract\n", "3 - Divide\n", "4 - Multiply\n")
4,
option = int(input("Enter options: "))

if option == 1:
    out = number1 + number2
    print(out)
elif option == 2:
    out = number1 - number2
    print(out)
elif option == 3:
    out = number1 / number2
    print(out)
elif option == 4:
     out = number1 * number2
     print(out)
else:
    print("Invalid option")