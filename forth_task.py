"""Forth task"""


from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Returns a list of users whose birthday is 7 days ahead including the current day.

    Args:
        param1 (list[dict]): the list of dictionary. Eech dictionary contains user's name 
                             and birthday in format "%Y.%m.%d".

    Returns:
        list[dict]: returns list of dictionary where each dictionary contains user's name
                    and congratulation date in format "%Y.%m.%d".

    Raises:
        TypeError: If param1 is not a list of dictionaries.
        ValueError: If date has wrong format.
    """

    try:
        # creates an empty list to store dictionaries with user's name and congratulation date
        greeting_list = []

        # determines current date
        current_date = datetime.today().date()

        for user in users:
            # creates an empty dictionary to store user's name and congratulation date
            greeting_dict = {}

            # converts user's birthday to datetime object
            user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

            # determines the birthday in current year
            birthday_this_year = datetime(year=current_date.year,
                                          month=user["birthday"].month,
                                          day=user["birthday"].day).date()

            # calculates the difference between a birthday and the current day
            diff_days = (birthday_this_year - current_date).days

            # checks if user's birthday falls on the next week
            if diff_days >= 0 and diff_days <=7:
                # checks if user's birthday falls on a Saturday
                if birthday_this_year.weekday() == 5:
                    # moves the congatulation date to next Monday
                    congratulation_date = birthday_this_year + timedelta(days=2)
                # checks if user's birthday falls on a Sunday
                elif birthday_this_year.weekday() == 6:
                    # moves the congatulation date to next Monday
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year

                # writes user's name to greenting dictionary
                greeting_dict["name"] = user["name"]
                # writes user's congratulation date to greeting dictionary
                greeting_dict["congratulation_date"] = congratulation_date.strftime("%Y.%m.%d")

                # adds greeting dictionary to greeting list
                greeting_list.append(greeting_dict)

        return greeting_list

    except ValueError as e:
        return e

    except TypeError:
        return "argument must be list of dictionaries"
