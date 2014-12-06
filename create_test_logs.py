"""
    Script to create test logs
"""
from datetime import datetime
import time

def create():
    f = open('test.log', 'w')

    for i in range(0, 100, 2):
        f.write("ERROR : test\n")
    for i in range(1, 101, 2):
        f.write("WARNING : test\n")
    for i in range(2, 102, 2):
        f.write("INFO : test\n")

    for i in range(0,100):
        f.write("%s:%s\n" % (str(datetime.utcnow()), "test"))
        #time.sleep(0.5)

    f.close()

if "__main__" == __name__:
    create()