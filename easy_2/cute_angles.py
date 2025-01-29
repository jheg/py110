DEGREE = "\u00B0"

def dms(angle):
    # Get whole number from angle
    degrees = int(angle)

    # calculate fraction for minutes
    mins_remainder = angle - degrees
    minutes = int(mins_remainder * 60)

    # calculate fraction for seconds
    seconds_remainder = (mins_remainder * 60) - minutes
    seconds = int(seconds_remainder * 60)

    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)

    
    # print(f"{degrees}{DEGREE}{minutes}'{seconds}\"")
    return(f"{degrees}{DEGREE}{minutes}'{seconds}\"") 

	
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")