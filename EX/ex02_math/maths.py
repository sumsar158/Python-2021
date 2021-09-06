"""Math."""


def ects(ects, weeks):
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours. If it's not possible in
    time then return a string "Impossible!".

    Examples:
    1. ects(30, 12) == 65
    2. ects(1, 1) == 26
    3. ects(1, 0) == "Impossible!"
    """
    ects_in_hours = ects * 26
    weeks_in_hours = weeks * 7 * 24

    if ects_in_hours > weeks_in_hours:
        return "Impossible!"
    else:
        return ects_in_hours / weeks


def average(a, b, c, d):
    """
    Implement a function that has 4 numeric parameters. Each parameter must be multiplied by number of its position
    in the function (x, y, z = 1, 2, 3). Calculate and return the average.

    Examples:
    1. average(0, 0, 0, 4) === 4
    2. average(1, 2, 3, 4) == 7.5
    3. average(5, 0, 5, 1) == 6
    """
    b = b * 2
    c = c * 3
    d = d * 4
    return (a+b+c+d)/4


def clock(päevad, tunnid, minutid, sekundid):
    """
    Implement a function that has 4 numeric parameters. The values are: days, hours, minutes, seconds. Calculate how many
    minutes are in total and return the value.

    Examples:
    1. clock(1, 24, 60, 60) === 2941
    3. clock(0, 0, 0, 60) == 1
    3. clock(0, 0, 1, 60) == 2
    """
    days_in_minutes = päevad * 24 * 60
    hours_in_minutes = tunnid * 60
    seconds_in_minutes = sekundid / 60

    return days_in_minutes + hours_in_minutes + seconds_in_minutes + minutid
