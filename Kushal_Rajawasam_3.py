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


#Problem 2 - Sales Target

#Ask user for sales target.
target = float(input("Enter Target Sales Amount: "))

#Initializing total sales
total_sales = 0

#Adding for loop for 5 days.
for day in range (1,6):
#Ask for  daily sales
    daily_sales = float(input(f"Enter Daily Sales Amount For Day {day}: "))

#Add daily sales to total sales.
    total_sales += daily_sales

#Calculating achieved percentage of target sales.
    percentage = (total_sales / target) * 100

#Display final result.
    print(f"Cumulative sales are: {total_sales} ({percentage:.1f}%)")