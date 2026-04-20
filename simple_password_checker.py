isUpperLower = False
isNumber = False
isCharacter = False

InpPassword = str(input("Input Password: "))

if len(InpPassword) < 6:
    print("weak")
elif len(InpPassword) >= 6 and len(InpPassword) <= 10:
    print("medium")
elif len(InpPassword) > 10: 
    #print("strong")
    for pwdStr in InpPassword:
       if pwdStr.isupper() or pwdStr.islower():
           isUpperLower = True
           continue
       elif pwdStr.isdigit():
           isNumber = True
           continue
       elif not pwdStr.isalnum():
           isCharacter = True
           continue
    if isNumber == True and isUpperLower == True and isCharacter == True:
        print("Password: ", InpPassword)
    else:
        if isNumber == False:
            print("Invalid Password! It must have a number")
        elif isUpperLower == False:
            print("Invalid Password! It must have atelast lower or upper case letter")
        elif isCharacter == False:
            print("Invalid Password! It must have a special character")

