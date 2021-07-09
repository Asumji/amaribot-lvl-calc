import os

clear = lambda: os.system('cls')

def floatToInt(float):
    string = str(float)
    string = string.split(".")
    string = string[0]
    integer = int(string)
    return integer

def convertTime(ms):
    time = ""
    if (ms >= 31104000000):
        year = floatToInt(ms/31104000000)
        month = floatToInt(ms/2592000000)
        time = "Years: " + str(year) + " months: " + str(month-(year*12))
    elif (ms >= 2592000000):
        month = floatToInt(ms/2592000000)
        day = floatToInt(ms/86400000)
        time = "Months: " + str(month) + " days: " + str(day-(month*30))
    elif (ms >= 86400000):
        day = floatToInt(ms/86400000)
        hour = floatToInt(ms/3600000)
        time = "Days: " + str(day) + " hours: " + str(hour-(day*24))
    elif (ms >= 3600000):
        hour = floatToInt(ms/3600000)
        minute = floatToInt(ms/60000)
        time = "Hours: " + str(hour) + " minutes: " + str(minute-(hour*60))
    elif (ms >= 60000):
        minute = floatToInt(ms/60000)
        second = floatToInt(ms/1000)
        time = "Minutes: " + str(minute) + " seconds: " + str(second-(minute*60))
    elif (ms >= 1000):
        second = floatToInt(ms/1000)
        time = "Seconds: " + str(second)

    return time

while (True):

    slvl = input("Start Level: ")
    elvl = input("Level Goal: ")
    pmulti = input("Point Multiplier: ")
    cd = input("Cooldown: ")

    if (slvl.isnumeric() and elvl.isnumeric() and pmulti.isnumeric() and cd.isnumeric()):
        slvl = int(slvl)
        elvl = int(elvl)
        pmulti = int(pmulti)
        cd = int(cd)

        if (slvl > 0):
            slvlxp = 20 * ((slvl-1) ** 2) + 35
        else:
            slvlxp = 0

        elvlxpfrom0 = 20 * ((elvl-1) ** 2) + 35

        xp = str(elvlxpfrom0 - slvlxp)

        nMessages = int(xp) / pmulti
        nMessages = floatToInt(nMessages)
        milliseconds = (nMessages * cd) * 1000
        time = convertTime(milliseconds)
        
        clear()
        print("Needed XP: " + xp + "\nNeeded Messages: " + str(nMessages) + "\n" + time)
    else:
        print("One or more of the specified variables isn't a number!")
