#Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnigh


def hours_with_suffixes():
    for hour in range(24):
        if hour == 0:
            print(f"12:00:00 AM (Midnight)")
        elif hour == 12:
            print(f"12:00:00 PM (Noon)")
        elif hour < 12:
            print(f"{hour}:00:00 AM")
        else:
            print(f"{hour-12}:00:00 PM")

hours_with_suffixes()