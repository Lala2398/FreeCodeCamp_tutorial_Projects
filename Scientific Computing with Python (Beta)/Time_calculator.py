def add_time(start, duration, day=None):
    # list of days to handle day tracking
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # start time - hours, minutes, and AM/PM
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # duration time : hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add hours and minutes for start time
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + total_minutes // 60
    result_minutes = total_minutes % 60
    result_hours = total_hours % 24
    days_later = total_hours // 24

    # Converting to 12-hour format
    if result_hours >= 12:
        period = 'PM'
    else:
        period = 'AM'

    display_hour = result_hours % 12
    if display_hour == 0:
        display_hour = 12

    # optional day of the week
    if day:
        day_index = days_of_week.index(day.capitalize())
        result_day = days_of_week[(day_index + days_later) % 7]
        day_output = f", {result_day}"
    else:
        day_output = ""

    # next day &  __n days later
    if days_later == 1:
        days_output = " (next day)"
    elif days_later > 1:
        days_output = f" ({days_later} days later)"
    else:
        days_output = ""

    # Final result
    result_time = f"{display_hour}:{str(result_minutes).zfill(2)} {period}{day_output}{days_output}"
    return result_time
