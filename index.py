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
        time = str(year) + " years and " + str(month-(year*12)) + " months."
    elif (ms >= 2592000000):
        month = floatToInt(ms/2592000000)
        day = floatToInt(ms/86400000)
        time = str(month) + " months and " + str(day-(month*30)) + " days."
    elif (ms >= 86400000):
        day = floatToInt(ms/86400000)
        hour = floatToInt(ms/3600000)
        time = str(day) + " days and " + str(hour-(day*24)) + " hours."
    elif (ms >= 3600000):
        hour = floatToInt(ms/3600000)
        minute = floatToInt(ms/60000)
        time = str(hour) + " hours and " + str(minute-(hour*60)) + " minutes."
    elif (ms >= 60000):
        minute = floatToInt(ms/60000)
        second = floatToInt(ms/1000)
        time = str(minute) + " minutes and " + str(second-(minute*60)) + " seconds."
    elif (ms >= 1000):
        second = floatToInt(ms/1000)
        time = str(second) + "seconds."

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
        print("Level " + str(slvl) + " to Level " + str(elvl) + ":\n" + "Needed XP: " + xp + "\nNeeded Messages: " + str(nMessages) + "\n" + time)
    else:
        print("One or more of the specified variables isn't a number!")
