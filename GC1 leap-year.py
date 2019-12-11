selectedyear = int(input("What year whould you like to check if it's a leap-year?"))
def isleapyear(year):
    if year/400 == int(year/400):
        return True
    elif year/100 == int(year/100):
        return False
    elif year/4 == int(year/4):
        return True
    else:
        return False

if isleapyear(selectedyear):
    print("'Tis")
else:
    print("'Tisn't")
