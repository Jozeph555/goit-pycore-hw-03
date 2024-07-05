"""First task"""


from datetime import datetime


def get_days_from_today(date: str) -> int:
    """Calculates the number of days between the given date and the current date.

    Args:
        param1 (str): Date in format 'YYYY-MM-DD'.

    Returns:
        int: The number of days between the given date and the current date.
             If the given date is later than the current one, the result must be negative.
    
    Raises:
        ValueError: If param1 doesn't match the defined format.
        TypeError: If param1 is not a string.
    
    """

    try:
        current_date = datetime.today()
        date_given = datetime.strptime(date, "%Y-%m-%d")
        return (current_date - date_given).days
    except ValueError as e:
        return e
    except TypeError:
        return "argument must be string"
