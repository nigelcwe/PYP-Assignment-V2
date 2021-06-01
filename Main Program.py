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
            menu = "=- Registration -=\nAre you sure want to go by that alias?\n1 - Yes\n2 - No\n\n> "
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
            elif menu == "exit":
                print(_menus(5))
            #continue for as many pages as needed

    return(inp)


def _newRec(file, list):
    string = _constantVar(1).join(str(i) for i in list)
    with open(file, "a") as openedFile:
        openedFile.write(string)
        openedFile.write("\n")


def _pageLanding():
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
    return pgNum


def _pageRegistration():
    aliasInvalidChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "\\", "|", "[", "]", "{", "}", "/", "?", "`", "~", ";", ":", "'", '"', ",", ".", "<", ">"]
    pwInvalidChars = ["\\", "#"]
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

            if aliasValidation == 1:
                continue
            break

    if alias == 1 or alias == 2:
        return pgNum

##--Asking user to confirm their desired alias
    _loader(3)
    _screenClr()
    print(_menus(1.2))
    while 1 == 1:
        aliasConfirm = _menuInput(_menus(1.2))
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
            for i in password:
                for j in pwInvalidChars:
                    if i == j:
                        print("Invalid password! Please try again.")
                        pwValidation = 1
                        break
                if pwValidation == 1:
                    break

            if len(password) == 0 and pwValidation == 0:
                print("Please enter a password!")
                pwValidation = 1

            if len(password) > 30 and pwValidation == 0:
                print("Password is too long! Please try again.")
                pwValidation = 1

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
        return pgNum
    else:
        return pgNum


# def _pageLogin():
#     while 1 == 1:
#         _screenClr()
#
# ##------Receiving user input (alias)
#         try:
#             alias = input(_menus(2.1))
#             alias = int(alias)
#             if alias == 1:
#                 _loader(3)
#                 pgNum = 0
#                 break
#             if alias == 2:
#                 _loader(3)
#                 pgNum = 5
#                 break
#
# ##------Assumed that user has entered their alias
#         except:
#             alias = str(alias)
#
# ##------Checking for user's alias
#         with open(_fileSelect(2), "r") as openedFile:
#             userIndex = -1
#             for line in openedFile:
#                 userData = line.rstrip()
#                 if alias == userData.split(_constantVar(1))[0]:
#                     _loader(3)
#                     userIndex = line
#                     break
#                 else:
#                     continue
#
# ##----------User's alias not found
#             if userIndex == -1:
#                 print("User not found! Please try again.")
#                 pgNum = 2
#                 break
#
# ##----------Receiving input (password)
#             _screenClr()
#             attempt = 0
#             while 1 == 1:
#                 attempt = attempt + 1
#                 password = str(input(_menus(2.2)))
#                 if password == userData.split(_constantVar(1))[0]:
#                     userStatus = 1
#                     print(_menus(2.3))
#                     _loader(10)
#                     break
#                 elif attempt > 10:
#                     print("Too many failed attempts! Please enter your alias again.")
#                 else:
#                     print("Incorrect password! Please try again")


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
while 1 == 1:
    pgNo = 0
    while 1 == 1:
        _screenClr()

##------Page 1: Landing Page
        if pgNo == 0:
            pgNo = _pageLanding()
            continue

#-------Page 2: Registration Page
        elif pgNo == 1:
            pgNo = _pageRegistration()
            continue

#-------Page 3: Login Page
        elif pgNo == 2:
            print("Login Page")

#-------Page 4: Browsing Page
        elif pgNo == 3:
            print("Browsing Page")

#-------Page 5: Exit Page
        elif pgNo == 5:
            pgNo = _pageExit()
            if pgNo == 0:
                continue


        break
    break


