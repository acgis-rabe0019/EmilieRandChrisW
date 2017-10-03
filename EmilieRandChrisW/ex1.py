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
def getFeatureType(featurecode):
    if featurecode==1:
        return 'point'
    elif featurecode==2:
        return 'polyline'
    elif featurecode==3:
        return 'polygon'

def test_getFeatureType():
    getFeatureType(1)
    getFeatureType(2)
    getFeatureType(3)

def main():
    test_getFeatureType()

if __name__=='__main__':
    main()

