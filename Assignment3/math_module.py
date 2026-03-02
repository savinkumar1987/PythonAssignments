import math  # importing math function.
def calc(num): #define calc() to calculate square root, log and sine value
    """
    calculate square root, Natural log, and sine of a number using math function
    :param num: float
    :return: tuple
    """
    sqrt_val = math.sqrt(num) #square root
    log_val =math.log(num) #log
    sine_val =math.sin(num) #sine
    return sqrt_val, log_val, sine_val # returning value as tuple.

while True:
    try:
        number = int(input("Enter a positive number: "))
        if number <= 0:
            print("Number must be greater than 0 ")
            continue
        sqrt_result, log_result, sine_result = calc(number)
        print(f"Square root: {sqrt_result}")
        print(f"Logarithm: {log_result}")
        print(f"Sine: {sine_result}")
        break
    except ValueError:
        print("Enter a valid number")