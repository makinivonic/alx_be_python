from datetime import datetime, timedelta
from datetime import date


def display_current_datetime():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current date and time: {current_date}")
    return datetime.now()

def calculate_future_date():
    number_of_days = int(input ("Enter the number of days to add to the current date: "))
    future_date = display_current_datetime() + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

calculate_future_date()