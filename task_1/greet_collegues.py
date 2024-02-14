from collections import defaultdict
from datetime import date, datetime
from utils import create_random_users


def get_birthdays_per_week(collegues: list[dict], relative_date: date = datetime.today().date()):
    """
    Determine which colleagues have birthdays in the upcoming week.

    Args:
        collegues (list[dict]): A list of dictionaries where each dictionary represents a user and
            contains "name" and "birthday" keys.

        relative_date (date, optional): The date from which to calculate one week forward. Default is today's date.

        weekdays (list[str], optional): List of weekday names. Defaults to predefined WEEKDAYS list.

    Returns:
        str: A formatted string containing the names of colleagues that have birthdays
            in the upcoming week, sorted by the day of the week.
    """

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    next_week_birthday_colleagues = defaultdict(list)

    for colleague in collegues:
        # prepare colleague birthday information
        name = colleague["name"]
        birthday = colleague["birthday"]
        birthday_this_year = birthday.replace(year=relative_date.year)

        if birthday_this_year < relative_date:
            birthday_this_year = birthday_this_year.replace(year=relative_date.year + 1)

        # get the colleagues with birthdays in the next 7 days, including relative_date
        delta_days = (birthday_this_year - relative_date).days
        # TODO: handle next monday situation
        if delta_days >= 0 and delta_days < 7:
            # if BD's on a weekend and relative_date is Monday, so greeting goes to next Monday
            if (birthday_this_year.weekday() >= 5) & (relative_date.weekday() == 0):
                weekday = "Next Monday"
            # if BD's on a weekend and goes to Monday
            elif birthday_this_year.weekday() >= 5:
                weekday = 'Monday'
            else:
                weekday = weekdays[birthday_this_year.weekday()]
            next_week_birthday_colleagues[weekday].append(f"{name} ({birthday_this_year.strftime('%Y-%m-%d')})")
    # print colleagues with birthdays in the next 7 days, including relative_date
    relative_date_str = f"{relative_date.strftime('%Y-%m-%d')}, {weekdays[relative_date.weekday()]}"
    print(
        f"---\nColleagues to greet for the next week, as of {relative_date_str}:\n---"
    )
    for day, names in next_week_birthday_colleagues.items():
        print(f'{day}: {", ".join(names)}')


if __name__ == "__main__":
    users = create_random_users()
    # example of checking birthdays from Monday
    monday = date(2024, 2, 12)
    get_birthdays_per_week(users, monday)
    # example of checking birthdays from today
    get_birthdays_per_week(users)
