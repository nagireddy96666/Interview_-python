import calendar
year=int(raw_input("Enter Year::"))
def get_cal(year):
    a=calendar.prcal(year)
    return a
print get_cal(year)
