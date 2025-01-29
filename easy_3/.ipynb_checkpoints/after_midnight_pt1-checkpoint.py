def get_hours(total_minutes):
    hours = (total_minutes // 60) % 24
    hours = hours if hours >= 0 else hours + 24
    
    return hours

def get_minutes(total_minutes):
    minutes = total_minutes % 60
    minutes = minutes if minutes >= 0 else minutes + 60
    
    return minutes

def time_of_day(total_minutes):
    hours = get_hours(total_minutes)
    minutes = get_minutes(total_minutes)
    formatted_time = f"{hours:02}:{minutes:02}"
    
    return formatted_time

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True