"""Second task"""


import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """Calculates the number of days between the given date and the current date.

    Args:
        param1 (int): the minimum possible number in the set (at least 1);
        param2 (int): the maximum possible number in the set (no more than 1000);
        param3 (int): quantity of numbers to choose (value between min and max).

    Returns:
        list: The list of randomly selected, sorted unique numbers. 
              If the parameters do not meet the specified limits, 
              the function returns an empty list.

    Raises:
        ValueError: If param1 > param2 or param3 > (param2 - param1 + 1).
        TypeError: If parameters are not int.
    """

    try:
        if min_num < 1 or max_num > 1000:
            return []
        numbers = list(range(min_num, max_num + 1))
        random_numbers = random.sample(numbers, quantity)
        random_numbers.sort()
        return random_numbers

    except ValueError as e:
        return e

    except TypeError:
        return "argument must be int"
