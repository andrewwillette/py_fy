import os

def printToFile(argument):
    with open(os.environ['absolute_log_location'], 'a') as f:
        print(argument, file=f)
        f.close()