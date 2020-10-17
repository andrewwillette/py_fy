import os

debugFile = os.environ['absolute_log_location'] + "py_fy.log"

if(os.path.exists(debugFile)):
    os.remove(debugFile)

with open(debugFile, 'w') as f: 
    pass

class Logger:
    @staticmethod
    def all(toWrite):
        print("[ALL]: {}".format(toWrite))
        with open(debugFile, 'a') as f:
            print(toWrite, file=f)
            f.close()

    @staticmethod
    def trace(toWrite):
        if(int(os.environ['log_level'])>=4):
            print('[TRACE]: {}'.format(toWrite))
        with open(debugFile, 'a') as f:
            print("[TRACE]: {}".format(toWrite), file=f)
            f.close()

    @staticmethod
    def debug(toWrite):
        if(int(os.environ['log_level'])>=3):
            print('[DEBUG]: {}'.format(toWrite))
        with open(debugFile, 'a') as f:
            print("[DEBUG]: {}".format(toWrite), file=f)
            f.close()

    @staticmethod
    def info(toWrite):
        if(int(os.environ['log_level'])>=2):
            print("[INFO]: {}".format(toWrite))
        with open(debugFile, 'a') as f:
            print("[INFO]: {}".format(toWrite), file=f)
            f.close()

    @staticmethod
    def warn(toWrite):
        if(int(os.environ['log_level'])>=1):
            print("[WARN]: {}".format(toWrite))
        with open(debugFile, 'a') as f:
            print("[WARN]: {}".format(toWrite), file=f)
            f.close()

    @staticmethod
    def error(toWrite):
        if(int(os.environ['log_level'])>=0):
            print("[ERROR]: {}".format(toWrite))
        with open(debugFile, 'a') as f:
            print("[ERROR]: {}".format(toWrite), file=f)
            f.close()

    @staticmethod
    def fatal(toWrite):
        if(int(os.environ['log_level'])>=0):
            print("[FATAL]: {}".format(toWrite))
        with open(debugFile, 'a') as f:
            print("[FATAL]: {}".format(toWrite), file=f)
            f.close()

    def writeGraphToFile(figure, filename):
        figure.savefig(os.environ['absolute_log_location'] + 'graphs/' + filename)