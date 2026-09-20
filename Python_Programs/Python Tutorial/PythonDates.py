from datetime import datetime

date_text = input("Enter date and time (YYYY-MM-DD HH:MM): ")
date = datetime.strptime(date_text, "%Y-%m-%d %H:%M")
print("Date:", date.strftime("%d-%m-%Y"))
