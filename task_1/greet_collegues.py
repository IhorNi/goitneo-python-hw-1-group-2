from datetime import datetime, timedelta, date
from collections import defaultdict


def create_users() -> list[dict]:
    """
    Create users all-over the year
    """
    users = []
    for day_of_year in range(1, 360):
        date_of_year = datetime(datetime.today().year, 1, 1) + timedelta(day_of_year - 1)
        users.append({"name": f"User{2*day_of_year-1}", "birthday": date_of_year})
        users.append({"name": f"User{2*day_of_year}", "birthday": date_of_year})

    return users


def get_birthdays_per_week(users: list[dict], refference_date: date = datetime.today().date()):
    """
    Function to get the list of user names who have birthdays in the upcoming week.
    The function prints the names of the users sorted by the day of the next week on which their birthday falls.
    If a user's birthday falls on a weekend, it is considered as falling on the next Monday.
    """

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    next_week_birthday_users = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=refference_date.year)

        if birthday_this_year < refference_date:
            birthday_this_year = birthday_this_year.replace(year=refference_date.year+1)

        delta_days = (birthday_this_year - refference_date).days

        if delta_days >= 0 and delta_days < 7:
            if birthday_this_year.weekday() >= 5:  # if it's a weekend
                weekday = 'Monday'
            else:
                weekday = weekdays[birthday_this_year.weekday()]
            next_week_birthday_users[weekday].append(name)

    for day, names in next_week_birthday_users.items():
        print(f'{day}: {", ".join(names)}')


if __name__ == '__main__':
    users = create_users()
    print(f"Total number of users: {len(users)}")
    print(f"Each user follows next structure {users[0]}")
    get_birthdays_per_week(users)
