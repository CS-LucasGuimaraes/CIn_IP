def binary2decimal(binary, i=0, decimal=0):
    """
    Converts a binary string to its decimal equivalent.

    Args:
        binary (str): The binary string to convert.
        i (int): The current index.
        decimal (int): The current converted binary.

    Returns:
        int: The decimal equivalent of the binary string.
    """
    if i < len(binary):
        decimal += int(binary[-i-1]) *2**i
        return binary2decimal(binary, i+1, decimal)
    
    return decimal


def browse_list(list, cont=0, answ=''):
    """
    Recursively gets the characters represented by the binary strings in the list.

    Args:
        list (list): A list of binary strings.
        cont (int): The current index within the list.
        answ (string): The current answer string.
    Return:
        string: The string decoded from the binaries.
    """

    if cont < len(list):
        # Convert the binary string to decimal and print its corresponding character:
        answ += chr(binary2decimal(list[cont]))

        # Recursively call the function for the next binary string:
        return browse_list(list, cont + 1, answ)

    return answ


def main():
    """
    Gets a space-separated string of binary values, converts them to characters,
    and prints a message with the decoded message.
    """

    binary_string = input().split(" ")  # Get a list of binary strings

    print(f"Os códigos da Matrix indicam que {browse_list(binary_string)} está perto.") 

    return 1


main()  # Start the program execution
