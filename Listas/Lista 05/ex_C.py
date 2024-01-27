def check_len(firewall):
    """
    Ensures the firewall string has a length of 32 characters by adding leading zeros if necessary.

    Args:
        firewall (str): The firewall string to check.

    Returns:
        str: The firewall string with a length of 32, padded with leading zeros if needed.
    """

    if len(firewall) == 32:  # Already the correct length, return it as it is.
        return firewall

    # Calculate the number of leading zeros needed:
    leading_zeros = 32 - len(firewall)

    # Create a new string with leading zeros and append the original firewall string:
    new_firewall = "0" * leading_zeros + firewall

    return new_firewall


def check_byte(firewall, tries):
    """
    Iteratively prompts for bytes and checks if they are present within the firewall string.

    Args:
        firewall (str): The firewall string.
        tries (int): The remaining number of attempts.

    Returns:
        bool: True if the correct byte is found, False otherwise.
    """

    if tries == 0:  # No more attempts left.
        print("Corre Keanu! Eles nos descobriram!!")
        return False

    # Ask for a byte:
    byte = input()

    if byte in firewall:  # Check if the byte is present in the firewall
        print("Muito bem! Estamos dentro! Vamos queimar essa cidade!!")
        return True
    else:
        print("Não é essa a senha, estamos ficando sem tempo.")

    # Recursively call the function with one less try:
    return check_byte(firewall, tries - 1)


def main():
    """
    Gets the firewall string, calls the check_len function to ensure its length,
    gets the number of tries, and starts the byte-checking process.
    """

    firewall = input()
    firewall = check_len(firewall)  # Ensure firewall string has a length of 32

    tries = int(input())

    check_byte(firewall, tries)  # Start the byte-checking process

    return 1


main()  # Start the program execution
