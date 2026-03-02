def fact_rec(num): # define function to calculate factorial
    """
    calculate the factorial of positive integer using recursive function
    The factorial of a number n (n!) is the product of all numbers less than or equal to n.
    n! = n * (n-1) * (n-2).....2 * 1
    0! = 1
    1! = 1
    n! = n * (n -1)! if n >1
    :param num: int
    :return: int
    """

    if num == 0 or num == 1: # check whether the number is 0 or 1 and return 1.
        return 1
    else:
        factorial = num * fact_rec(num -1) # recursive function to calculate factorial.
        return factorial

while True: #infinte loop to keep asking user for a valid input.
    try:
        number = int(input("Enter a positive integer to calculate factorial: ")) # prompt the user to enter a positive integer.
        if number < 0: # check if the number is negative
            print("Please enter a positive integer") #inform the user about invalid input.
            continue # restart the loop and ask again.
        print(f"The factorial of {number} is {fact_rec(number)}") # if the input is valid, calculate factorial by calling fact_rec()
        break # exit from the loop after successful calculation.
    except ValueError: # Handle cases with value error.
        print("Please enter a positive integer")




