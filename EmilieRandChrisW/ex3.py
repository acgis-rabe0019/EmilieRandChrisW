#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     03-10-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#------------------------------------------------------------------------------
def main():
    pass

def isPointOnLine(x,y,m,b):
    calc=m*x+b
    if calc==y:
        return True
    else:
        return False

def test_isPointOnLine():
    print "Expected: True"
    print "Actual:", isPointOnLine(0,2,3,2)

test_isPointOnLine()
if __name__ == '__main__':
    main()
