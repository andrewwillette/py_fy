from datetime import datetime

# for saving datetime as strings in postgre
def convertDatetimeToString(datetime):
    return datetime.strftime("%Y-%m-%d")