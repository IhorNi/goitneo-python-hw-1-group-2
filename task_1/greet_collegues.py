import random
from datetime import datetime, timedelta, date
from collections import defaultdict


def create_random_users() -> list[dict]:
    """
    Create random users all-over the year
    """
    names = [
        'John', 'Sarah', 'Robert', 'Emma', 'Michael', 'Sophia', 
        'James', 'Emily', 'David', 'Olivia', 'Richard', 'Isabella', 
        'Charles', 'Ava', 'Joseph', 'Mia', 'Thomas', 'Charlotte'
    ]
    surnames = [
        'Smith', 'Johnson', 'Brown', 'Taylor', 'Miller', 'Davis', 
        'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'White', 
        'Jackson', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez'
    ]
    random_users = []
    for day_of_year in range(1, 360):
        # get the next date
        date_of_year = datetime(datetime.today().year, 1, 1) + timedelta(day_of_year - 1)
        
        # decide randomly how many birthdays will be in a day from 0 to 3
        num_birthdays = random.randint(0, 3)
        
        # generate users with random names per day, if any
        for _ in range(num_birthdays):
            chosen_name = f"{random.choice(names)} {random.choice(surnames)}"
            random_users.append({"name": chosen_name, "birthday": date_of_year})

    return random_users


def get_birthdays_per_week(collegues: list[dict], refference_date: date = datetime.today().date()):
    """
    Function to get the list of user names who have birthdays in the upcoming week.
    The function prints the names of the users sorted by the day of the next week on which their birthday falls.
    If a user's birthday falls on a weekend, it is considered as falling on the next Monday.
    """

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    next_week_birthday_users = defaultdict(list)

    for colleague in collegues:
        name = colleague["name"]
        birthday = colleague["birthday"].date()
        birthday_this_year = birthday.replace(year=refference_date.year)

        if birthday_this_year < refference_date:
            birthday_this_year = birthday_this_year.replace(year=refference_date.year + 1)

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
    users = create_random_users()
    print(f"Total number of users: {len(users)}")
    print(f"Each user follows next structure {users[0]}")
    get_birthdays_per_week(users)
