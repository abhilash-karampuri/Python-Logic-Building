from datetime import date
day, month, year = 11, 12, 2003
date_obj = date(year, month, day)
day_of_week_index = date_obj.weekday()
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"The day of the week for {date_obj} is {days_of_week[day_of_week_index]}.")
