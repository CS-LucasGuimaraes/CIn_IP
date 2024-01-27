def check_len(byte):
    """
    Ensures the binary string (byte) has a length of 8 characters by adding leading zeros if necessary.

    Args:
        byte (str): The binary string to check.

    Returns:
        str: The binary string with a length of 8, padded with leading zeros if needed.
    """

    if len(byte) == 8:  # Already the correct length, return it as is
        return byte

    # Calculate the number of leading zeros needed:
    leading_zeros = 8 - len(byte)

    # Create a new string with leading zeros and append the original binary string:
    new_byte = "0" * leading_zeros + byte

    return new_byte


def binary2decimal(binary):
    """
    Converts a binary string to its decimal equivalent.

    Args:
        binary (str): The binary string to convert.

    Returns:
        int: The decimal equivalent of the binary string.
    """

    decimal = 0

    binary = check_len(binary)  # Ensure binary string has a length of 8

    # Convert each binary digit to its decimal value and add them up:
    decimal += int(binary[0]) * 2**7
    decimal += int(binary[1]) * 2**6
    decimal += int(binary[2]) * 2**5
    decimal += int(binary[3]) * 2**4
    decimal += int(binary[4]) * 2**3
    decimal += int(binary[5]) * 2**2
    decimal += int(binary[6]) * 2**1
    decimal += int(binary[7]) * 2**0

    return decimal


def browse_list(list, cont):
    """
    Recursively prints the characters represented by the binary strings in the list.

    Args:
        list (list): A list of binary strings.
        cont (int): The current index within the list.
    """

    if cont < len(list):
        # Convert the binary string to decimal and print its corresponding character:
        print(chr(binary2decimal(list[cont])), end='')

        # Recursively call the function for the next binary string:
        browse_list(list, cont + 1)


def main():
    """
    Gets a space-separated string of binary values, converts them to characters,
    and prints a message with the decoded message.
    """

    binary_string = input().split(" ")  # Get a list of binary strings

    print("Os códigos da Matrix indicam que ", end='') 

    browse_list(binary_string, 0)  # Decode and print the characters

    print(" está perto.") 

    return 1


main()  # Start the program execution
