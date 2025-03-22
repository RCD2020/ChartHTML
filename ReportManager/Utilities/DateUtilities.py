from datetime import datetime


def read_date(date_str):
    return datetime.strptime(date_str, '%d %B %Y %I:%M %p')


if __name__ == '__main__':
    print(read_date('22 March 2025 9:29 AM'))
