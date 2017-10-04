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

def main():
    pass
def isDivisibleBy(numerator, denominator):
    numerate=str(numerator)
    denominate=str(denominator)
    if numerate.isdigit():
        if denominate.isdigit():
            if int(numerate)%int(denominate) !=0:
                return 'Dividing ' + str(numerator) +' by ' +str(denominator)+ ' has a remainder.'
            else:
                return 'Dividing '+ str(numerator)+ ' by '+str(denominator)+' does not have a remainder.'

        else:
            return 'Both arguments must be numeric.'

    else:
        return 'Both Arguments must be numeric.'

def test_isDivisibleBy():
    #test to see if letter numerator works
    print isDivisibleBy('q',7)
    #test to see if letter denominator works
    print isDivisibleBy(7,'d')
    #test to see if both numbers with remainder works
    print isDivisibleBy('7',8)
    #test to see if both numbers without remainder works
    print isDivisibleBy(1,1)
test_isDivisibleBy()
if __name__ == '__main__':
    main()
