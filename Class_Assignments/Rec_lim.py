import sys
sys.setrecursionlimit(5)
print (sys.getrecursionlimit())

def first():
    return second()

def second():
    return third()

def third():
    return fourth()

def fourth():
    return fifth()

def fifth():
    return 0