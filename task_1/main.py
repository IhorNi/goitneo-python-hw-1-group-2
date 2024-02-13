from greeting_utils import create_users, get_birthdays_per_week


if __name__ == '__main__':
    users = create_users()
    print(f"Total number of users: {len(users)}")
    print(f"Each user follows next structure {users[0]}")
    get_birthdays_per_week(users)
