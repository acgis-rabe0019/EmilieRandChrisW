#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     03-10-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def isPointInBox(x,y,xmin,ymin,xmax,ymax):
    if x<=xmin and y<=ymin:
        if x<=xmax:
            if y<=ymax:
                return False
            else:
                return'y'
        else:
            return False
    elif x>xmin and x<xmax and y>ymin and y<ymax:
        return True
    else:
        return "try again"

def test_isPointInBox():
    print 'expect: True'
    print 'actual:', isPointInBox(9,9,8,8,10,10)
    print 'expect: False'
    print 'actual:', isPointInBox(3,3,4,4,8,8)


def main():
    test_isPointInBox()



if __name__=='__main__':
    main()
