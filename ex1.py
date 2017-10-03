#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     03-10-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-----------------------------------------------------------------------------
def getfeaturetype(featurecode):
    if featurecode==1:
        return 'point'
    elif featurecode==2:
        return 'polyline'
    elif featurecode==3:
        return 'polygon'

def test_getfeaturetype():
    getfeaturetype(1)
    getfeaturetype(2)
    getfeaturetype(3)

def main():
    test_getfeaturetype()

if __name__=='__main__':
    main()
