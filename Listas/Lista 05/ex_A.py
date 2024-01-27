def oddFactorial(n, answ):
    """
    Recursively calculates the factorial of an odd number, multiplying only odd factors.

    Args:
        n (int): The odd number for which to calculate the factorial.
        answ (int): The current accumulated product (used for recursion).

    Returns:
        int: The factorial of the odd number.
    """

    if n <= 1:  # Base case: Factorial of 1 or less is 1
        return answ

    # Multiply the current odd number into the accumulated product:
    answ *= n

    # Recursively calculate the factorial of the next odd number:
    return oddFactorial(n - 2, answ)  # Note: Subtract 2 to directly reach the next odd number


def main():
    """
    Gets user input, handles even inputs, calls the oddFactorial function, and prints the result.
    """

    x = int(input())  # Get the input number

    if x % 2 == 0:  # If the input is even, adjust it to the previous odd number
        x -= 1

    answ = oddFactorial(x, 1)  # Start the factorial calculation with initial answer 1 (the multiplicative neutral value)

    print(answ)  # Print the final factorial

    return 1


main()  # Start the program execution
    