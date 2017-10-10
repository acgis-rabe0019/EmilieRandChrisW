def isNumeric(testString):
    if (type (testString) != type ('')):
        return False
    if testString[0] == '-':
       return isNumeric(testString[1:])
    else:
        return testString.isdigit()


def test_isNumeric():

def main():
    test_isNumeric()

if __name__=='__main__':
    main()