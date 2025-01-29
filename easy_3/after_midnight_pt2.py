def get_hours_and_minutes(time):
    total_minutes = 0
    if not (time == "24:00" or time == "00:00"):
        hours = int(time[0:2])
        minutes = int(time[3:5])
        total_minutes = (hours * 60) + minutes
    
    return total_minutes
    
def after_midnight(time):
    mins_after_midnight = get_hours_and_minutes(time)
    
    return mins_after_midnight

def before_midnight(time):
    mins_before_midnight = get_hours_and_minutes(time)
    if mins_before_midnight == 0:
        return mins_before_midnight
    else:
        return abs((mins_before_midnight - 1440))

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True