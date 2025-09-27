from datetime import datetime, date, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    return current_datetime
datetime = display_current_datetime()
formatted_datetime = datetime.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current date and time: {formatted_datetime}")

number_of_days = int(input("Enter the number of days to add to the current date:"))




def calculate_future_date():
    current_date = date.today()
    return current_date

    
date = calculate_future_date()

future_date = date + timedelta(days=number_of_days)
formatted_date = future_date.strftime("%Y-%m-%d")
print(f"Future date: {formatted_date}")