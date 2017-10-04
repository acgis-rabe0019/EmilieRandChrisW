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
    str(featurecode)
    if featurecode==1:
        return 'point'
    elif featurecode==2:
        return 'polyline'
    elif featurecode==3:
        return 'polygon'
    else:
        return 'Feature code must be a 1,2 or 3. No other numbers will work.'

def test_getFeatureType():
    #test point
   print getFeatureType(1)
    #test polyline
   print getFeatureType(2)
    #test polygon
   print getFeatureType(3)
   #test error
   print getFeatureType(1234)

def main():
    test_getFeatureType()

if __name__=='__main__':
    main()

