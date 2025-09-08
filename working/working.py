import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    groups = match.groups()

    start_time = format_time(groups[0], groups[1], groups[2])
    end_time = format_time(groups[3], groups[4], groups[5])

    return f"{start_time} to {end_time}"

def format_time(hour_str, minute_str, am_pm):
    hour = int(hour_str)
    minute = int(minute_str) if minute_str else 0

    if not (1 <= hour <= 12 and 0 <= minute <= 59):
        raise ValueError("Invalid hour or minute value")

    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
