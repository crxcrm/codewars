# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
# Note that spaces are important.

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def format_duration(seconds):
    if not seconds:
        now = "now"
        return now
    seg = seconds%60
    minutes = int(seconds/60)
    hours = int(minutes/60)
    minutes = minutes%60
    days = int(hours/24)
    hours = hours%24
    years = int(days/365)
    days = days%365
    str_year = ""
    str_day = ""
    str_hour = ""
    str_minute = ""
    str_second = ""
    if(years != 0):
        if(years == 1):
            str_year = "1 year, "
        else:
            str_year = str(years) + " years, "
    if(days != 0):
        if(days == 1):
            str_day = "1 day, "
        else:
            str_day = str(days) + " days, "
    if(hours != 0):
        if(hours == 1):
            str_hour = "1 hour, "
        else:
            str_hour = str(hours) + " hours, "
    if(minutes != 0):
        if(minutes == 1):
            str_minute = "1 minute, "
        else:
            str_minute = str(minutes) + " minutes, "           
    if(seg != 0):
        if(seg == 1):
            str_second = "1 second"
        else:
            str_second = str(seg) + " seconds"
    
    r = (str_year + str_day + str_hour + str_minute + str_second)         
    largo = (len(str_year) + len(str_hour) + len(str_day) + len(str_minute) + len(str_second))
    if (largo <=11):
        return rreplace(r, ', ', '', 1)
    else:
        if(r[-1] == " "):
            return rreplace(r[0:-2], ', ', ' and ', 1)
        return rreplace(r, ', ', ' and ', 1)
         
