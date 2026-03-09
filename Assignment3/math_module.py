import math  # importing math function.
def calc(num): #define calc() to calculate square root, log and sine value
    """
    calculate square root, Natural log, and sine of a number using math function
    :param num: float
    :return: tuple
    """
    sqrt_val = math.sqrt(num)
    log_val =math.log(num)
    sine_val =math.sin(num)
    return sqrt_val, log_val, sine_val # returning value as tuple.

number = int(input("Enter a positive number: ")) # asking user to enter a positive number
sqrt_result, log_result, sine_result = calc(number) # calling calc() to calculate sqrt, log and sine operations.
print(f"Logarithm: {log_result}")
print(f"Sine: {sine_result}")
