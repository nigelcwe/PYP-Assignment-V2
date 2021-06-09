#NIGEL CHAN WEI EN
#TP059179

##----------------------------------------Modules
from datetime import *


##----------------------------------------Functions
def _screenClr():
    print("\n" * 100)


def _sleep(seconds):
    t1 = timedelta(seconds=seconds)
    t2 = datetime.now()
    while 1 == 1:
        t3 = datetime.now()
        if t3 - t2 < t1:
            continue
        else:
            break


def _loader(dots):
    while dots > 0:
        _sleep(0.33)
        print(" . ", end="")
        dots = dots - 1
    _sleep(0.33)
    print()


def _menus(num):
    try:
        num = float(num)
        if num == 0.0:
            menu = "Welcome to SUPER CAR RENTAL SERVICES!\nWould you like to:\n1 - Register\n2 - Login\n3 - Browse as Guest\n4 - Login as Admin\n5 - Exit\n"
        elif num == 1.1:
            menu = "=- Registration -=\nPlease enter an alias: (5 to 20 characters)\nOther options:\n1 - Back\n2 - Exit\n\n> "
        elif num == 1.2:
            menu = "=- Registration -=\nAre you sure want to go by that alias?\n1 - Yes\n2 - No\n"
        elif num == 1.3:
            menu = "=- Registration -=\nPlease create a password. (Invalid characters are \\ and #)\n\n> "
        elif num == 1.4:
            menu = "=- Registration -=\nPlease enter your password again.\n\n> "
        elif num == 1.5:
            menu = "=- Registration -=\nDear user, your application has been recorded and sent for Admin approval.\n\nNow proceeding to browse as guest."
        elif num == 2.1:
            menu = "=- Login -=\nPlease enter your alias:\nOther options:\n1 - Back\n2 - Exit\n\n> "
        elif num == 2.2:
            menu = "=- Login -=\nPlease enter your password:\nOther options:\n1 - Back\n2 - Exit\n\n> "
        elif num == 2.3:
            menu = "Successfully logged in!\nNow redirecting to main browsing page."
        elif num == 2.4:
            menu = "=- Login -=\nLogin as:\n1 - User\n2 - Admin\n\nMore options:\n3 - Back\n"
        elif num == 3.0:
            menu = "Hi"
        elif num == 4.0:
            menu = ""
        elif num == 5.0:
            menu = "Are you sure you want to exit?\n1 - Yes\n2 - No\n"
        elif num == 6.0:
            menu = ""
    except:
        num = str(num)
        if num == "badInput":
            menu = "Invalid input! Please try again."
    return menu


def _fileSelect(num):
    fileName = ""
    if num == 1:
        fileName = "memberList.txt"
    elif num == 2:
        fileName = "registrationList.txt"
    elif num == 3:
        fileName = "adminList.txt"
    elif num == 4:
        fileName = "carList.txt"
    elif num == 5:
        fileName = "counter.txt"
    return fileName


def _constantVar(num):
    var = ""
    if num == 1:
        var = "#"

    return var


def _menuInput(menu):
    inp = 0
    while 1 == 1:
        try:
            inp = int(input("Please enter a corresponding value:\n> "))
            break
        except:
            print(_menus("badInput"))
            _loader(3)
            _screenClr()
            if menu == "landing":
                print(_menus(0))
            elif menu == "registration_1":
                print(_menus(1.1))
            elif menu == "registration_2":
                print(_menus(1.2))
            elif menu == "login_1":
                print(_menus(2.4))
            elif menu == "exit":
                print(_menus(5))
            #continue for as many pages as needed

    return(inp)


def _newRec(file, list):
    string = _constantVar(1).join(str(i) for i in list)
    with open(file, "a") as openedFile:
        openedFile.write(string)
        openedFile.write("\n")


def _pwValidation(pw):
    pwInvalidChars = ["\\", "#"]
    pwValidation = 0
    for i in pw:
        for j in pwInvalidChars:
            if i == j:
                print("Invalid password! Please try again.")
                pwValidation = 1
                break
        if pwValidation == 1:
            break

    if pwValidation == 0:
        pwLetter = 0
        pwNumber = 0
        for i in pw:
            try:
                i = int(i)
                pwNumber = 1
            except:
                pwLetter = 1
        if pwLetter == 0 or pwNumber == 0:
            print("Password must contain both letters and numbers!")
            pwValidation = 1

    if len(pw) == 0 and pwValidation == 0:
        print("Please enter a password!")
        pwValidation = 1

    if len(pw) > 30 and pwValidation == 0:
        print("Password is too long! Please try again.")
        pwValidation = 1

    return pwValidation


def _login(userType):
    list1 = []
    uStatus = 0
    uIndex = -1
    while 1 == 1:
        _screenClr()

##------Receiving input (alias)
        try:
            alias = input(_menus(2.1))
            alias = int(alias)
            if alias == 1:
                _loader(3)
                pgNum = 2
                break
            if alias == 2:
                _loader(3)
                pgNum = 5
                break

##------Assumed that an alias was entered
        except:
            alias = str(alias)

##------Checking for Alias
            if userType == 1:
                with open(_fileSelect(1), "r") as openedFile:
                    uIndex = -1
                    lineNum = 0
                    for line in openedFile:
                        lineNum = lineNum + 1
                        userData = line.rstrip()
                        if alias == userData.split(_constantVar(1))[0]:
                            _loader(3)
                            uIndex = lineNum
                            break
                        else:
                            continue

            elif userType == 2:
                with open(_fileSelect(3), "r") as openedFile:
                    uIndex = -1
                    lineNum = 0
                    for line in openedFile:
                        lineNum = lineNum + 1
                        userData = line.rstrip()
                        if alias == userData.split(_constantVar(1))[0]:
                            _loader(3)
                            uIndex = lineNum
                            break
                        else:
                            continue

##----------Alias not found
            if uIndex == -1:
                print("User not found! Please try again.")
                _loader(3)
                pgNum = 2
                break
            break

##--Receiving input (password)
    attempt = 0
    if uIndex != -1:
        while 1 == 1:
            _screenClr()
            attempt = attempt + 1
            password = str(input(_menus(2.2)))

##----------Exception in case user inputs 1 or 2 (reserved for page navigation)
            try:
                password = int(password)
                if password == 1:
                    _loader(3)
                    pgNum = 2
                    break
                elif password == 2:
                    _loader(3)
                    pgNum = 5
                    break
                else:
                    print(_menus("badInput"))
                    _loader(3)
                    continue

##----------Assumed that user intends to enter a password
            except:

##--------------Validating password
                pwValidation = _pwValidation(password)
                if pwValidation == 1:
                    _loader(3)
                    continue

##--------------Checking if password matches
                if password == userData.split(_constantVar(1))[1]:
                    pgNum = 3
                    if userType == 1:
                        uStatus = 1
                    elif userType == 2:
                        uStatus = 2
                    print(_menus(2.3))
                    _loader(10)
                    break

##------------------To limit the amount of attempts users have
                elif attempt > 10:
                    print("Too many failed attempts! Please enter your alias again.")
                    _loader(10)
                    pgNum = 2
                    uStatus = 0
                    break
                else:
                    print("Incorrect password! Please try again")
                    _loader(3)

##----------Preparing output of function
    list1.append(pgNum)
    list1.append(uStatus)
    list1.append(uIndex)
    return list1


def _pageLanding():
    list1 = []
    print(_menus(0))
    while 1 == 1:
        pgNum = _menuInput("landing")
        if pgNum >= 1 and pgNum <= 5:
            _loader(3)
            break
        else:
            print(_menus("badInput"))
            _loader(3)
            _screenClr()
            print(_menus(0))
    list1.append(pgNum)
    return list1


def _pageRegistration():
    list1 = []
    aliasInvalidChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "\\", "|", "[", "]", "{", "}", "/", "?", "`", "~", ";", ":", "'", '"', ",", ".", "<", ">"]
    while 1 == 1:
        _screenClr()

#-------Try+Except blocks to check if user has entered a string or an integer value. If string, assume user has entered their alias.
        try:
            alias = input(_menus(1.1))
            alias = int(alias)
            if alias == 1:
                _loader(3)
                pgNum = 0
                break
            elif alias == 2:
                _loader(3)
                pgNum = 5
                break
            else:
                print("Alias does not contain a letter.")
                _loader(3)
                _screenClr()
                continue

##------Assumed that user has entered an alias
        except:
            alias = str(alias)

##----------Validation of user's alias
            aliasValidation = 0
            for i in alias:
                for j in aliasInvalidChars:
                    if i == j:
                        print("Invalid alias! Please try again.")
                        _loader(3)
                        aliasValidation = 1
                        break
                if aliasValidation == 1:
                    break

            if len(alias) == 0 and aliasValidation == 0:
                print("Please enter an alias!")
                _loader(3)
                aliasValidation = 1

            if len(alias) < 5 and aliasValidation == 0:
                print("Alias is too short! Please try again.")
                _loader(3)
                aliasValidation = 1

            if len(alias) > 20 and aliasValidation == 0:
                print("Alias is too long! Please try again.")
                _loader(3)
                aliasValidation = 1

##----------Checking availability of user's alias

##----------Checking in user file
            if aliasValidation == 0:
                with open(_fileSelect(1), "r") as openedFile:
                    for line in openedFile:
                        userData = line.rstrip()
                        if alias == userData.split(_constantVar(1))[0]:
                            print("Alias already exists! Please try again.")
                            _loader(3)
                            aliasValidation = 1
                            break
                        else:
                            continue

##----------Checking in pending registration file
            if aliasValidation == 0:
                with open(_fileSelect(2), "r") as openedFile:
                    for line in openedFile:
                        userData = line.rstrip()
                        if alias == userData.split(_constantVar(1))[0]:
                            print("Alias already exists! Please try again.")
                            _loader(3)
                            aliasValidation = 1
                            break
                        else:
                            continue

##----------Checking in admin file
            if aliasValidation == 0:
                with open(_fileSelect(3), "r") as openedFile:
                    for line in openedFile:
                        userData = line.rstrip()
                        if alias == userData.split(_constantVar(1))[0]:
                            print("Alias already exists! Please try again.")
                            _loader(3)
                            aliasValidation = 1
                            break
                        else:
                            continue

            if aliasValidation == 1:
                continue

        if alias == 1 or alias == 2:
            list1.append(pgNum)
            return list1

##--Asking user to confirm their desired alias
        _loader(3)
        while 1 == 1:
            _screenClr()
            print(_menus(1.2))
            aliasConfirm = _menuInput("registration_2")
            if aliasConfirm >= 1 and aliasConfirm <= 2:
                _loader(3)
                break
            else:
                print(_menus("badInput"))
                _loader(3)
                _screenClr()
                print(_menus(1.2))

##--Prompting user to create a password
        if aliasConfirm == 1:
            while 1 == 1:
                pwValidation = 0
                _screenClr()
                password = input(_menus(1.3))

##----------Validation of user's password
                pwValidation = _pwValidation(password)
                if pwValidation == 1:
                    _loader(3)
                    continue

##----------Prompting user to enter their password again as double confirmation
                _loader(3)
                _screenClr()
                passwordCheck = input(_menus(1.4))

##----------Checking if 2nd password the user has entered matches their original/desired password
                if passwordCheck != password or len(passwordCheck) != len(password):
                    print("Passwords do not match! Please try again.")
                    _loader(3)
                    continue
                else:
                    _loader(3)
                    break

##------Compiling user's data into a string as preparation to be written into registration text file for admin approval
            userDataList = []
            userDataList.append(alias)
            userDataList.append(password)

#-------Start writing user data into registration text file for admin approval
            _newRec(_fileSelect(2), userDataList)

#-------Provide the user with feedback
            _screenClr()
            print(_menus(1.5))
            pgNum = 3
            _loader(10)
            list1.append(pgNum)
            return list1
        else:
            continue


def _pageLogin():
    list1 = []
    pgNum = 0
    print(_menus(2.4))
    while 1 == 1:
        uType = _menuInput("login_1")
        if uType == 1:
            _loader(3)
            list1 = _login(uType)
            break
        elif uType == 2:
            _loader(3)
            list1 = _login(uType)
            break
        elif uType == 3:
            _loader(3)
            pgNum = 0
            list1.append(pgNum)
            break
        else:
            print(_menus("badInput"))
            _loader(3)
            _screenClr()
            print(_menus(2.4))
    return list1




def _pageExit():
    print(_menus(5))

##--Receiving input from the user (page selection)
    while 1 == 1:
        userExit = _menuInput("exit")
        if userExit >= 1 and userExit <=2:
            _loader(3)
            break
        else:
            print(_menus("badInput"))
            _loader(3)
            _screenClr()
            print(_menus(5))

##--Executing user's seected option
    if userExit == 1:
        _screenClr()
        print("Thank you for using our services!")

        ## Need to clear account login info

        _sleep(0.5)
        _loader(11)
        _sleep(0.5)
    else:
        pgNum = 0
        return pgNum



##----------------------------------------Main Program
outputList = []
pgNo = 0
userStatus = 0 #0 - Guest, 1 - Member, 2 - Admin
userIndex = -1
while 1 == 1:
    _screenClr()

##------Page 1: Landing Page
    if pgNo == 0:
        outputList = _pageLanding()
        pgNo = outputList[0]
        continue

#-------Page 2: Registration Page
    elif pgNo == 1:
        outputList = _pageRegistration()
        pgNo = outputList[0]
        continue

#-------Page 3: Login Page
    elif pgNo == 2:
        outputList = _pageLogin()
        pgNo = outputList[0]
        if pgNo != 0:
            userStatus = outputList[1]
            userIndex = outputList[2]
            print(userStatus)
            print(userIndex)
        continue

#-------Page 4: Browsing Page
    elif pgNo == 3:
        print("Browsing Page")

#-------Page 5: Exit Page
    elif pgNo == 5:
        pgNo = _pageExit()
        if pgNo == 0:
            continue


    break



