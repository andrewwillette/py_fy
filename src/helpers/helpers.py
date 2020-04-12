def printToFile(argument):
    with open('./../../dist/output.txt', 'a') as f:
        print(argument, file=f)
        f.close()