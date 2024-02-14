import random
from collections import defaultdict
from datetime import date, datetime, timedelta


def create_random_users() -> list[dict]:
    """
    Generate random users with birthdays evenly distributed throughout the year.

    Returns:
        list[dict]: A list of dictionaries where each dictionary represents a user and contains
        "name" and "birthday" keys.
    """
    first_names = [
        "John",
        "Sarah",
        "Robert",
        "Emma",
        "Michael",
        "Sophia",
        "James",
        "Emily",
        "David",
        "Olivia",
        "Richard",
        "Isabella",
        "Charles",
        "Ava",
        "Joseph",
        "Mia",
        "Thomas",
        "Charlotte",
    ]
    surnames = [
        "Smith",
        "Johnson",
        "Brown",
        "Taylor",
        "Miller",
        "Davis",
        "Clark",
        "Rodriguez",
        "Lewis",
        "Lee",
        "Walker",
        "White",
        "Jackson",
        "Harris",
        "Martin",
        "Thompson",
        "Garcia",
        "Martinez",
    ]
    random_users = []
    for day_of_year in range(1, 360):
        # get the next date
        date_of_year = datetime(datetime.today().year, 1, 1) + timedelta(day_of_year - 1)

        # decide randomly how many birthdays will be in a day from 0 to 2
        num_birthdays = random.randint(0, 2)

        # generate users with random names per day, if any
        for _ in range(num_birthdays):
            chosen_name = f"{random.choice(first_names)} {random.choice(surnames)}"
            random_users.append({"name": chosen_name, "birthday": date_of_year})

    return random_users


def get_birthdays_per_week(collegues: list[dict], refference_date: date = datetime.today().date()):
    """
    Determine which colleagues have birthdays in the upcoming week.

    Args:
        collegues (list[dict]): A list of dictionaries where each dictionary represents a user and
            contains "name" and "birthday" keys.

        refference_date (date, optional): The date from which to calculate one week forward. Default is today's date.

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
        birthday = colleague["birthday"].date()
        birthday_this_year = birthday.replace(year=refference_date.year)

        if birthday_this_year < refference_date:
            birthday_this_year = birthday_this_year.replace(year=refference_date.year + 1)

        # get the colleagues with birthdays in the next 7 days from refference_date
        delta_days = (birthday_this_year - refference_date).days
        # TODO: handle next monday situation
        if delta_days >= 0 and delta_days < 7:
            if birthday_this_year.weekday() >= 5:  # if it's a weekend
                weekday = "Monday"
            else:
                weekday = weekdays[birthday_this_year.weekday()]
            next_week_birthday_colleagues[weekday].append(f"{name} ({birthday_this_year.strftime('%Y-%m-%d')})")

    print(
        f"List of colleagues to greet for the next week, as of {refference_date.strftime('%Y-%m-%d')}, {weekdays[refference_date.weekday()]}:"
    )
    print("---")
    for day, names in next_week_birthday_colleagues.items():
        print(f'{day}: {", ".join(names)}')


if __name__ == "__main__":
    users = create_random_users()
    get_birthdays_per_week(users)
