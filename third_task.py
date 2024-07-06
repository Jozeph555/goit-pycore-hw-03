"""Third task"""


import re


def normalize_phone(phone_number: str) -> str:
    """Normalizes phone numbers to a standard format.

    Args:
        param1 (str): the string with a phone number in any format.

    Returns:
        str: returns a normalized phone number in the format "+380000000000"

    Raises:
        TypeError: If param1 is not a string.
    """

    try:
        numbers = re.findall(r"\d+", phone_number)
        phone_number_cleaned = "".join(numbers)
        if phone_number_cleaned.startswith("38"):
            return '+' + phone_number_cleaned
        return '+38' + phone_number_cleaned

    except TypeError:
        return "argument must be str"
