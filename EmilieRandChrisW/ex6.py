def isNumeric(testString):
    """Input test string in: '' format only please."""
    if (type (testString) != type ('')):
        return False
    elif testString.isdigit()== True:
            return True
    elif testString[0] == '-':
       if testString[1:].isdigit():
            return True
       else:
        return False
    else:
        return False



def test_isNumeric():
    #expect true for next 2
   print isNumeric('23')
   print isNumeric('-23')
   #expect false
   print isNumeric(23)
   print isNumeric('hello')
   print isNumeric('-number')
   print isNumeric('*5')

def main():
    test_isNumeric()

if __name__=='__main__':
    main()

