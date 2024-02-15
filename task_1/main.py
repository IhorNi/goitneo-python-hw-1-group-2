from collections import defaultdict
from datetime import date, datetime

from utils import create_random_users

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Next Monday"]
MONDAY_INDEX = 0
NEXT_MONDAY_INDEX = -1


def get_birthday_this_year(birthday: date, relative_date: date) -> date:
    """
    Returns this year's birthday based on a given reference date.

    Args:
        birthday (date): The birthday date.
        relative_date (date): The reference date.

    Returns:
        date: This year's birthday based on the reference date.
    """

    birthday_this_year = birthday.replace(year=relative_date.year)
    if birthday_this_year < relative_date:
        birthday_this_year = birthday_this_year.replace(year=relative_date.year + 1)

    return birthday_this_year


def get_greeting_day(birthday_this_year: date, relative_date: date) -> str:
    """
    Returns the weekday to greet the colleague.

    Args:
        birthday_this_year (date): The colleague's birthday this year.
        relative_date (date): The reference date.

    Returns:
        str: The weekday to greet the colleague.
    """

    # if birthday is a weekend and relative_date is Monday, so greeting goes to next Monday
    if (birthday_this_year.weekday() >= 5) & (relative_date.weekday() == 0):
        return WEEKDAYS[NEXT_MONDAY_INDEX]
    elif birthday_this_year.weekday() >= 5:
        return WEEKDAYS[MONDAY_INDEX]
    else:
        return WEEKDAYS[birthday_this_year.weekday()]


def get_birthdays_per_week(collegues: list[dict], relative_date: date = datetime.today().date()) -> str:
    """
    Determine which colleagues have birthdays in the upcoming week.

    Args:
        collegues (list[dict]): A list of dictionaries where each dictionary represents a user and
            contains "name" and "birthday" keys.

        relative_date (date, optional): The date from which to calculate one week forward. Default is today's date.

    Returns:
        str: A formatted string containing the names of colleagues that have birthdays
            in the upcoming week, sorted by the day of the week.
    """
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    next_week_birthday_colleagues = defaultdict(list)

    for colleague in collegues:
        name = colleague["name"]
        birthday = colleague["birthday"]
        birthday_this_year = get_birthday_this_year(birthday, relative_date)

        delta_days = (birthday_this_year - relative_date).days
        if delta_days < 7:
            weekday_to_greet = get_greeting_day(birthday_this_year, relative_date)
            next_week_birthday_colleagues[weekday_to_greet].append(
                f"{name} ({birthday_this_year.strftime('%Y-%m-%d')})"
            )

    relative_date_str = f"{relative_date.strftime('%Y-%m-%d')}, {weekdays[relative_date.weekday()]}"

    greeting_string = f"---\nColleagues to greet for the next week, as of {relative_date_str}:\n---"
    if next_week_birthday_colleagues:
        for day, names in next_week_birthday_colleagues.items():
            greeting_string += f"\n{day}: {', '.join(names)}"
    else:
        greeting_string += "\nNo birthdays this week :("

    return greeting_string


if __name__ == "__main__":
    users = create_random_users()
    # example of checking birthdays from Monday
    monday = date(2024, 2, 12)
    print(get_birthdays_per_week(users, monday))
    # example of checking birthdays from today
    print(get_birthdays_per_week(users))
