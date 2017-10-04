
import sys
from sys import argv



def isItTrue(testValue):
    if len(str(testValue)) <=4 :
        return str(testValue)+' is True.'
    else:
        return str(testValue)+ ' is False'

def test_isItTrue():
    #test if true
    print isItTrue('1')
    #test if false
    print isItTrue('Thing')
#test_isItTrue()
#sys.exit()

def main():
    if isItTrue(argv[1]):
        print isItTrue(argv[1])
    else:
        print 'Usage: ex7.py '

main()



