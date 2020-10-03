import datetime
import calendar

# returns array of all days in month
def getAllDaysOfMonth(year, month):
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
    return days

def getDatetimeFromString(stringDate):
    return datetime.strptime(stringDate, '%Y-%m-%d')