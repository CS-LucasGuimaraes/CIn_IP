def solve(initial, desired):
    """
    Recursively determines if it's possible to reach the desired value from the initial value
    by repeatedly dividing the current value into stacks of 2/3 and 1/3 of its size.

    Args:
        initial (int): The starting value.
        desired (int): The target value to reach.

    Returns:
        bool: True if the desired value can be reached, False otherwise.
    """

    if initial < desired:  # Base case: Not possible to reach a larger value
        return False

    if initial == desired:  # Base case: Desired value reached
        return True

    if initial % 3 != 0:  # Only valid if the initial value is divisible by 3
        return False

    max_stack = initial // 3 * 2  # Calculate the larger stack (2/3 of initial value)
    min_stack = initial // 3  # Calculate the smaller stack (1/3 of initial value)

    if max_stack == desired or min_stack == desired:  # Check for immediate solutions
        return True

    # Recursively explore possible paths from both stacks:
    return solve(max_stack, desired) or solve(min_stack, desired)


def main():
    """
    Handles input, calls the solve function, and prints results for multiple test cases.
    """

    tc = int(input())  # Get the number of test cases

    while tc:
        tc -= 1

        initial_desired = input().split(' ')  # Get the initial and desired values
        initial = int(initial_desired[0])     # Split the initial value to its own var
        desired = int(initial_desired[1])     # Split the desired value to its own var 

        answ = solve(initial, desired)  # Call the solve function

        print("SIM") if answ else print("NAO")  # Print the result (SIM for True, NAO for False)

    return 1


main()  # Start the program execution
