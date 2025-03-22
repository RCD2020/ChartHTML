from random import choice, randint


DAYS_IN_MONTH = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]
MONTH_NAME = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
NAMES = [
    'Cecil', 'Rudy', 'Paul', 'Mark', 'Debbie', 'Oliver', 'Nolan', 'Eve'
]


def get_num_days_in_month(num_month, year):
    days = DAYS_IN_MONTH[num_month-1]

    if (
        num_month == 2
        and year % 4 == 0
        and (
            year % 100 != 0
            or year % 400 == 0
        )
    ):
        days += 1

    return days


def generate_date_time():
    year = randint(2025, 2025)
    month = randint(1, 3)
    day = randint(1, get_num_days_in_month(month, year))
    hour = randint(1, 12)
    minute = randint(0, 59)
    mmmm = 'AM' if hour >= 6 and hour <= 11 else 'PM'

    return (
        f'{day:02d} {MONTH_NAME[month-1]} {year} '
        f'{hour}:{minute:02d} {mmmm}'
    )


def random_name():
    return choice(NAMES)


def random_csv(num_rows, path):
    text = 'Agent,Creation Date\n'

    for x in range(num_rows):
        text += f'{random_name()},{generate_date_time()}\n'

    text = text[:-1]

    with open(path, 'w') as f:
        f.write(text)


def random_rgb():
    return (randint(0, 255), randint(0, 255), randint(0,255))


if __name__ == '__main__':
    # print(generate_date_time())
    # print(random_name())
    random_csv(2000, 'out.csv')
