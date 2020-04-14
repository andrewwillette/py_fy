import os

def printToFile(toPrint, file):
    with open(os.environ['absolute_log_location'] + file, 'a') as f:
        print(toPrint, file=f)
        f.close()