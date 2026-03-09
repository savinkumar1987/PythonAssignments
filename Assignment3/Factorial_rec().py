def fact_rec(num): # define function to calculate factorial
    """
    calculate the factorial of positive integer using recursive function
    The factorial of a number n (n!) is the product of all numbers less than or equal to n.
    :param num: int
    :return: int
    """

    if num == 0 or num == 1:
        return 1
    else:
        factorial = num * fact_rec(num -1) # calling fact_rec() function inside it to calculate factorial
        return factorial


number = int(input("Enter a positive integer to calculate factorial: "))
print(f"Factorial of {number} is: {fact_rec(number)}")





