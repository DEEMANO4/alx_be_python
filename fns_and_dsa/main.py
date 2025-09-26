from datetime import datetime
def get_current_datetime():
    current_dt = datetime.now()
    return current_dt

current_timestamp = get_current_datetime()
print(f"The current date and time is: {current_timestamp}")

formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted current date and time: {formatted_timestamp}")