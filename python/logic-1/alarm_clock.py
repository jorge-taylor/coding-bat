def alarm_clock(day, vacation):
    if vacation:
        if day == 6 or day == 0:
            return "off"
        else:
            return "10:00"
    elif not vacation and 1 <= day <= 5:
        return "7:00"
    else:
        return "10:00"
