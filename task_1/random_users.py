import random
from datetime import datetime, timedelta

from faker import Faker


def create_random_users() -> list[dict]:
    """
    Generate random users with birthdays evenly distributed throughout the year.

    Returns:
        list[dict]: A list of dictionaries where each dictionary represents a user and contains
        "name" and "birthday" keys.
    """
    fake = Faker()
    random_users = []
    for day_of_year in range(1, 360):
        # get the next date
        date_of_year = (datetime(datetime.today().year, 1, 1) + timedelta(day_of_year - 1)).date()

        # decide randomly how many birthdays will be in a day from 0 to 2
        num_birthdays = random.randint(0, 2)

        # generate users with random names per day, if any
        for _ in range(num_birthdays):
            chosen_name = fake.name()
            random_users.append({"name": chosen_name, "birthday": date_of_year})

    return random_users
