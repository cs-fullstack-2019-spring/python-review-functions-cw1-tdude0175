def main():
    # problem1()
    problem2()


# Create a function that has a loop
# Prompt for numbers until the user enters q to quit
# If the user doesn't enter q, ask them to input another number
# When the user enters q to quit, print the SUM of all numbers entered
# BONUS:
#
# Write your code so that it it doesn't matter if the User enters a lowercase or an uppercase q to quit
# Add extra validation to check that if the User doesn't enter q what they did enter is actually a number

def problem1():
    userInput = input("give me numbers!\n")
    numberGathering = []       #recording all necessary variable at the start
    start = 0
    while (userInput.lower() != "q"):
        if int(userInput) % 1 == 0:
            numberGathering.append(int(userInput))
            userInput = input("I am going to need more numbers\n")
    userInput = input("I am going to need more number \n")
    #if the user does NOT ENTER A NUMBER it won't be added to the list
    if userInput.lower() == "q":
        userInput = input("are you sure you want to quit? Y,n")
        if userInput.upper() == "Y":
                userInput == "q"
    for number in numberGathering:
        start += number
    print(start)
# Create a function problem2()
#
# In this function prompt the user for 2 numbers
#
# Create a second function called do_the_math that accepts 2 parameters (the 2 entered numbers)
#
# In the do_the_math calculate the SUM, DIFFERENCE, PRODUCT, and QUOTIENT (division result)
# and return them as a dictionary to the calling function
#
# Example: Dictionary result returned if the arguments 25 and 10 are passed to the function:
# {'diff': 15, 'prod': 250, 'quot': 2.5, 'sum': 35}
#
# In your problem2() function, print the dictionary result returned from your do_the_math function
# using string literal formatting
#
# Example: Execution and Output:
# Enter the First Number in the calculation:
# 25
# Enter the Second Number in the calculation:
# 10
# Here are your results for the numbers 25 and 10:
# The SUM result is 35
# The DIFFERENCE result is 15
# The PRODUCT result is 250
# The DIVISION result is 2.5

def problem2():
    num1 = int(input("i need your first number.\n"))
    num2 = int(input("I need a second number.\n"))          # userInput stored in num1 and num2 for easy to read
    numberCalculations = []
    numberCalculations.append(do_the_math(num1,num2))
    for element in numberCalculations:
        print(f"\n for index {numberCalculations.index(element)} ran\n")
        print(f"sum = {element['sum']}\ndifference = {element['difference']}")
        print(f"product = {element['product']}\nquotient = {element['quotient']}")
    # index mapped out to know which stored data is necessary
def do_the_math(number1,number2):
    sum = number1+number2
    difference = number1-number2        # stored all in short term variables for the function
    product = number1*number2
    quotient = number1/number2
    return{"sum": sum , "difference": difference , "product": product, "quotient": quotient}
    # Returning as a dictionary for easy to store and access in comparison


if __name__ == '__main__':
    main()
