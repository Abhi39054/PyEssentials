"""
    Name: pyessentials.generators
    Description: A module providing utility functions for generating random data.
    Author: Abhishek Kumar
"""

import secrets

def generate_random_int(min_value=0, max_value=100):
    """Generate a random integer within a specified range.

    Args:
        min_value (int): The minimum value of the range. Default is 0.
        max_value (int): The maximum value of the range. Default is 100.

    Returns:
        int: A randomly generated integer within the specified range.
    """
    return secrets.randbelow(max_value - min_value + 1) + min_value

