#Problem 1 - Calculator

#Getting inputs from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+ , - , * , /: ")
num2 = float(input("Enter second number: "))

#Perform operations bases on the input
#Checks each input so the second number is not 0
if operator == "+" :
    if num2 != 0:
        print(f"Result is : {num1 + num2}")
    else:
        print("Second number cannot be 0")

elif operator == "-" :
    if num2 != 0:
        print(f"Result is : {num1 - num2}")
    else:
        print("Second number cannot be 0")

elif operator == "*" :
    if num2 != 0:
        print(f"Result is : {num1 * num2}")
    else:
        print("Second number cannot be 0")

elif operator == "/" :
    if num2 != 0:
        print(f"Result is : {num1 / num2}")
    else:
        print("Second number cannot be 0")

else:
    print("Error: Invalid operator")