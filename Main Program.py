#NIGEL CHAN WEI EN
#TP059179

# Modules
from datetime import *


# Functions
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

        # Landing Page Menus
        if num == 0.0:
            menu = "Welcome to SUPER CAR RENTAL SERVICES!\nWould you like to:\n1 - Register\n2 - Login\n3 - Browse as Guest\n4 - Login as Admin\n5 - Exit\n"

        # Registration Page Menus
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

        # Login Page Menus
        elif num == 2.1:
            menu = "=- Login -=\nPlease enter your alias:\nOther options:\n1 - Back\n2 - Exit\n\n> "
        elif num == 2.2:
            menu = "=- Login -=\nPlease enter your password:\nOther options:\n1 - Back\n2 - Exit\n\n> "
        elif num == 2.3:
            menu = "Successfully logged in!\nNow redirecting to main browsing page."
        elif num == 2.4:
            menu = "=- Login -=\nLogin as:\n1 - User\n2 - Admin\n\nMore options:\n3 - Back\n"

        # Member Dashboard Menus (member browsing page)
        elif num == 3.0:
            menu = "=- Member Dashboard -=\nWhat would you like to do?\n1 - Browse cars\n2 - View account details\n3 - Log out\n4 - Exit\n"

        # Admin Dashboard Menus (admin browsing page)
        elif num == 4.0:
            menu = "=- Admin Dashboard -=\nWhat would you like to do?\n1 - Add a car\n2 - Modify car details\n3 - View records (Cars or Payments)\n4 - Search specific records\n5 - Return a car\n6 - Log out\n7 - Exit\n"
        elif num == 4.1:
            menu = "Is the above data correct?\n1 - yes\n2 - No\n\nPlease enter a corresponding value:\n> "

        # Exit Page Menus
        elif num == 5.0:
            menu = "Are you sure you want to exit?\n1 - Yes\n2 - No\n"

        # Main Car Page Menus
        elif num == 6.0:
            menu = ""

    # Bad Input Menu
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
        fileName = "paymentRecords.txt"
    elif num == 6:
        fileName = "bookingRecords.txt"
    return fileName


def _constantVar(num):
    var = ""

    # Layer 1 Separator
    if num == 1:
        var = "#"

    # Layer 2 Separator
    elif num == 2:
        var = ":"

    # Layer 3 Separator
    elif num == 3:
        var = "-"

    # Input Separator
    elif num == 4:
        var = ";"

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
            elif menu == "userDash_1":
                print(_menus(3.0))
            elif menu == "adminDash_1":
                print(_menus(4.0))
            elif menu == "exit":
                print(_menus(5))
    # Continue for as many pages as needed

    return(inp)


def _newRec(file, list):
    string = _constantVar(1).join(str(i) for i in list)
    with open(file, "a") as openedFile:
        openedFile.write(string)
        openedFile.write("\n")


def _addCar():
    carData = []
    confirmation = 0
    while 1 == 1:
        _screenClr()
        carInp = input("=- Car Addition -=\nPlease enter car details in the following format:\n\nID;Model;Type;Status;Rate\n(For status: available - 0, booked - 1)\n\n> ")
        carData = carInp.split(_constantVar(4))
        _loader(3)
        _screenClr()
        while 1 == 1:
            carTemp = "ID: " + carData[0] + "\nModel: " + carData[1] + "\nType: " + carData[2] + "\nStatus: " + carData[3] + "\nRate: " + carData[4]
            print("=- Car Addition -=\n" + carTemp + "\n")
            try:
                confirmation = input(_menus(4.1))
                confirmation = int(confirmation)
                if confirmation == 1 or confirmation == 2:
                    break
                elif confirmation != 2:
                    print(_menus("badInput"))
                    _loader(3)
                    _screenClr()
                    continue
            except:
                print(_menus("badInput"))
                _loader(3)
                _screenClr()
                continue

        if confirmation == 2:
            continue
        else:
            inval = 0

            # Checking for proper syntax of car ID
            if inval == 0 and carData[0].startswith("CA") == False:
                print("Invalid car ID detected! Please try agaain.")
                inval = 1

            if inval == 0:
                try:
                    IDNum = int(carData[0][2::])
                except:
                    print("Invalid car ID detected! Please try agin.")
                    inval = 1


            # Checking length of car ID
            if inval == 0 and len(carData[0]) != 6:
                print("Invalid car ID detected! Please try again")
                inval = 1

            # Checking for repeating car ID
            if inval == 0:
                with open(_fileSelect(4), "r") as openedFile:
                    for lines in openedFile:
                        existingRec = lines.rstrip("\n")
                        if carData[0] == existingRec.split(_constantVar(1))[0]:
                            print("Repeating car ID detected! Please try again.")
                            inval = 1
                            break

            if inval == 1:
                _sleep(0.5)
                _loader(5)
                continue
            else:
                break

    _newRec(_fileSelect(4), carData)
    _screenClr()
    print("Car has been successfully added!\nNow redirecting back to Admin Dashboard.")
    _sleep(0.5)
    _loader(5)



def _pwValidation(pw):
    pwInvalidChars = ["\\", "#", ":"]
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
    uAlias = ""
    uStatus = 0
    uFound = -1
    while 1 == 1:
        _screenClr()

        # Receiving Input (alias)
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

        # Assume that an alias was entered
        except:
            alias = str(alias)

            # Checking for alias
            if userType == 1:
                with open(_fileSelect(1), "r") as openedFile:
                    uFound = -1
                    lineNum = 0
                    for line in openedFile:
                        lineNum = lineNum + 1
                        userData = line.rstrip()
                        if alias == userData.split(_constantVar(1))[0]:
                            _loader(3)
                            uAlias = alias
                            uFound = 1
                            break
                        else:
                            continue

            elif userType == 2:
                with open(_fileSelect(3), "r") as openedFile:
                    uFound = -1
                    lineNum = 0
                    for line in openedFile:
                        lineNum = lineNum + 1
                        userData = line.rstrip()
                        if alias == userData.split(_constantVar(1))[0]:
                            _loader(3)
                            uAlias = alias
                            uFound = 1
                            break
                        else:
                            continue

            # Alias not found
            if uFound == -1:
                print("User not found! Please try again.")
                _loader(3)
                pgNum = 2
                continue
            break

    # Receiving Input (password)
    attempt = 0
    if uFound != -1:
        while 1 == 1:
            _screenClr()
            attempt = attempt + 1
            password = str(input(_menus(2.2)))

            # Exception in case user inputs 1 or 2 (reserved for page navigation)
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

            # Assume that user intends to input a password
            except:

                # Password Validation
                pwValidation = _pwValidation(password)
                if pwValidation == 1:
                    _loader(3)
                    continue

                # Checking if password matches
                if password == userData.split(_constantVar(1))[1]:
                    pgNum = 3
                    if userType == 1:
                        uStatus = 1
                    elif userType == 2:
                        uStatus = 2
                    _loader(3)
                    _screenClr()
                    print(_menus(2.3))
                    _sleep(0.5)
                    _loader(5)
                    break

                # To limit the amount of attempts users have
                elif attempt > 10:
                    print("Too many failed attempts! Please enter your alias again.")
                    _loader(10)
                    pgNum = 2
                    uStatus = 0
                    break
                else:
                    print("Incorrect password! Please try again")
                    _loader(3)

    # Preparing output of function
    list1.append(pgNum)
    list1.append(uStatus)
    list1.append(uAlias)
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

        # Try+Except blocks to check if user has entered a string or an integer value. If string, assume user has entered their alias.
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

        # Assume that user has entered an alias
        except:
            alias = str(alias)

            # Validation of user's alias
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

# Checking availability of user's alias

            # Checking in user file
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

            # Checking in pending registration file
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

            # Checking in admin file
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

        # Asking users to confirm their alias
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

        # Prompting users to create a password
        if aliasConfirm == 1:
            while 1 == 1:
                pwValidation = 0
                _screenClr()
                password = input(_menus(1.3))

                # Validation of user's password
                pwValidation = _pwValidation(password)
                if pwValidation == 1:
                    _loader(3)
                    continue

                # Prompting user to enter their password again as double confirmation
                _loader(3)
                _screenClr()
                passwordCheck = input(_menus(1.4))

                # Checking if 2nd password the user has entered matches their original/desired password
                if passwordCheck != password or len(passwordCheck) != len(password):
                    print("Passwords do not match! Please try again.")
                    _loader(3)
                    continue
                else:
                    _loader(3)
                    break

            # Compiling user's data into a string as preparation to be written into registration text file for admin approval
            userDataList = []
            userDataList.append(alias)
            userDataList.append(password)
            userDataList.append("")
            userDataList.append("")

            # Start writing user data into registration text file for admin approval
            _newRec(_fileSelect(2), userDataList)

            # Provide the user with feedback
            _screenClr()
            print(_menus(1.5))
            pgNum = 3
            _sleep(0.5)
            _loader(5)
            list1.append(pgNum)
            return list1
        else:
            continue


def _pageLogin():
    list1 = []
    pgNum = 0
    print(_menus(2.4))

    # Receive input (login as user/admin)
    while 1 == 1:
        uType = _menuInput("login_1")

        # User Login
        if uType == 1:
            _loader(3)
            list1 = _login(uType)
            break

        # Admin Login
        elif uType == 2:
            _loader(3)
            list1 = _login(uType)
            break

        # Navigate to previous page
        elif uType == 3:
            _loader(3)
            pgNum = 0
            list1.append(pgNum)
            break

        # Invalid input detection
        else:
            print(_menus("badInput"))
            _loader(3)
            _screenClr()
            print(_menus(2.4))
    return list1


def _pageBrowsing(uType, uAlias):
    pgNum = 0
    list1 = []
    while 1 == 1:

        # Go to guest car page
        # if uType == 0:


        # Go to member browsing page
        if uType == 1:
            list1 = _memberBrowse(uAlias)

        # Go to admin browsing page
        elif uType == 2:
            list1 = _adminBrowse(uAlias)


def _pageExit(logout):
    list1 = []
    pgNum = 0
    print(_menus(5))

    # Receiving input from the user (page selection)
    while 1 == 1:
        if logout == 1:
            userExit = 1
            break
        else:
            userExit = _menuInput("exit")
            if userExit >= 1 and userExit <=2:
                _loader(3)
                break
            else:
                print(_menus("badInput"))
                _loader(3)
                _screenClr()
                print(_menus(5))

    # Executing user's selected option
    if userExit == 1:
        _screenClr()
        print("Thank you for using our services!")
        pgNum = 0

        # Clearing account data
        userStatus = 0
        userAlias = ""

        _sleep(0.5)
        _loader(11)
        _sleep(0.5)
    else:
        pgNum = 0

    list1.append(pgNum)
    return list1



# Main Program
outputList = []
pgNo = 0
userStatus = 0 # 0 - Guest, 1 - Member, 2 - Admin
userAlias = ""
while 1 == 1:
    _screenClr()

    # Page 1: Landing Page
    if pgNo == 0:
        outputList = _pageLanding()
        pgNo = outputList[0]
        continue

    # Page 2: Registration Page
    elif pgNo == 1:
        outputList = _pageRegistration()
        pgNo = outputList[0]
        continue

    # Page 3: Login Page
    elif pgNo == 2:
        outputList = _pageLogin()
        pgNo = outputList[0]
        if pgNo != 0:
            userStatus = outputList[1]
            userAlias = outputList[2]
        continue

    # Page 4: Browsing Pages
    elif pgNo == 3:
        outputList = _pageBrowsing(userStatus, userAlias)

    # Page 5: Car Pages
    elif pgNo == 4:
        print("Car Page")

    # Page 6: Exit Page
    elif pgNo == 5:
        outputList = _pageExit(0)
        pgNo = outputList[0]
        if pgNo == 0:
            continue


    break



