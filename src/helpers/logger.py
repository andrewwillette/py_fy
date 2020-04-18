import os

def writeToFile(toWrite, file):
    with open(os.environ['absolute_log_location'] + file, 'a') as f:
        print(toWrite, file=f)
        f.close()

def writeGraphToFile(figure, filename):
    figure.savefig(os.environ['absolute_log_location'] + 'graphs/' + filename)