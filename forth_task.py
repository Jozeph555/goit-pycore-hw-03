"""Forth task"""


from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Returns a list of users whose birthday is 7 days ahead including the current day.

    Args:
        param1 (list[dict]): the list of dictionary. Eech dictionary contains user's name
                             as a key and user's birthday in format "%Y.%m.%d" as a value.

    Returns:
        list[dict]: returns list of dictionary where each dictionary contains user's name
                    as a key and congratulation date in format "%Y.%m.%d" as a value

    Raises:
        TypeError: If param1 is not a list of dictionaries.
    """

    try:
        greeting_list = []
        current_date = datetime.today().date()
        for user in users:
            greeting_dict = {}
            user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = datetime(year=current_date.year,
                                          month=user["birthday"].month,
                                          day=user["birthday"].day).date()
            diff_days = (birthday_this_year - current_date).days
            if diff_days >= 0 and diff_days <=7:
                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year
                greeting_dict["name"] = user["name"]
                greeting_dict["congratulation_date"] = congratulation_date.strftime("%Y.%m.%d")
                greeting_list.append(greeting_dict)
        return greeting_list

    except:
        return "argument must be list of dictionaries"
