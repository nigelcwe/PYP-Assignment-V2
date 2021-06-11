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
            menu = "Welcome to SUPER CAR RENTAL SERVICES!\nWould you like to:\n1 - Register\n2 - Login\n3 - Browse as Guest\n4 - Exit\n"

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
            menu = "=- Admin Dashboard -=\nWhat would you like to do?\n1 - Add a car\n2 - Modify car details\n3 - View records (Cars or Payments)\n4 - Search specific records (Bookings or Payments)\n5 - Return a car\n6 - Log out\n7 - Exit\n"
        elif num == 4.1:
            menu = "Is the above data correct?\n1 - yes\n2 - No\n\nPlease enter a corresponding value:\n> "
        elif num == 4.2:
            menu = ""

        # Exit Page Menus
        elif num == 5.0:
            menu = "Are you sure you want to exit?\n1 - Yes\n2 - No\n"

        # Main Car Page Menus
        elif num == 6.0:
            menu = "\nOther options:\n6 - Next Page\n7 - Previous Page\n8 - Back\n\nPlease enter a corresponding value:\n> "
        elif num == 6.1:
            menu = "=- Car List -=\n1 - Login\n2 - Register\n3 - Continue browsing\n"

        # Admin Car Page Menus
        elif num == 7.0:
            menu = "=- Edit Car Details -=\nPlease select details to be modified:\n1 - Car model\n2 - Car type\n3 - Car status\n4 - Rental rate\n5 - Back\n"

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
            elif menu == "guestCar":
                print(_menus(6.1))
            elif menu == "carModify":
                print(_menus(7.0))
            elif menu == "exit":
                print(_menus(5))
    # Continue for as many pages as needed

    return(inp)





def _newRec(file, list):
    string = _constantVar(1).join(str(i) for i in list)
    with open(file, "a") as openedFile:
        openedFile.write(string + "\n")





def _carModify(carID):
    carList = []
    carListOld = []
    carListNew = []
    adminMod = ""
    newList = []
    newCar = ""
    output = 0
    while 1 == 1:
        _screenClr()
        print(_menus(7.0))
        adminInp = _menuInput("carModify")
        if (adminInp >= 1 and adminInp <= 5) == False:
            print(_menus("badInput"))
            _loader(3)
            continue
        _loader(3)
        break

    if adminInp != 5:
        with open (_fileSelect(4), "r") as openedFile:
            for line in openedFile:
                carList = line.rstrip("\n").split(_constantVar(1))
                if carID == carList[0]:
                    _screenClr()
                    adminMod = str(input("=- Edit Car Details -=\nCar to be edited: " + " # ".join(str(i) for i in carList) + "\n\nData to be edited: " + carList[adminInp] + "\n\nPlease enter the new data:\n\n> "))
                    _loader(3)
                    carListOld = carList[::]
                    carListNew = carList[::]
                    carListNew[adminInp] = adminMod
                    newList.append(carListNew)
                else:
                    newList.append(carList)

        while 1 == 1:
            _screenClr()
            try:
                confirmation = int(input("=- Edit Car Details -=\nConfirm the following changes?\n\nOriginal: " + " # ".join(str(i) for i in carListOld) + "\nEdited  : " + " # ".join(str(i) for i in carListNew) + "\n\n1 - Yes\n2 - No\n\n> "))
                if confirmation == 1 or confirmation == 2:
                    break
                else:
                    print(_menus("badInput"))
                    _loader(3)
                    continue
            except:
                print(_menus("badInput"))
                _loader(3)
                continue

        _loader(3)
        if confirmation == 2:
            output = 0
            return output


        with open (_fileSelect(4), "w") as openedFile:
            for ind in range(len(newList)):
                newCar = _constantVar(4).join(newList[ind])
                openedFile.write(newCar + "\n")

        output = 1
        return output





def _carSelect(uStatus, uAlias = "", mode = 0):        # mode: Admin  (0 = View cars available for rental, 1 = Modify, 2 = Return)
    carLine = ""                                       #       Member (0 = Select car to book [only shows available cars])
    carData = []
    counter = -1
    fileList = []
    pad = " "
    list1 = []
    carID = ""
    while 1 == 1:
        loadedCarID = []
        if counter < -1:
            counter = -1
        _screenClr()
        with open (_fileSelect(4), "r") as openedFile:
            fileList = openedFile.readlines()
            print("=- Cars List -=\n\tModel                 Type             Status           Rate             ID\n")
            try:
                for i in range(5):
                    carLine = fileList[(counter + 1)].rstrip("\n")
                    carData = carLine.split("#")
                    loadedCarID.append(carData[0])
                    if int(carData[3]) == 0:
                        carData[3] = "Available"
                    elif int(carData[3]) == 1:
                        carData[3] = "Unavailable"

                    # For admins and members to view only cars that are available for rental
                    if (uStatus == 2 or uStatus == 1) and mode == 0:
                        if int(carData[3]) == 1:
                            continue

                    print(str(i + 1) + " - " + (carData[1] + pad * (20 - len(carData[1]))) + ": " + (carData[2] + pad * (15 - len(carData[2]))) + ": " + (carData[3] + pad * (15 - len(carData[3]))) + ": " + (carData[4] + pad * (15 - len(carData[4]))) + ": " + (carData[0] + pad * (15 - len(carData[0]))))
                    counter = counter + 1
            except:
                print("_______End of List_______")

        try:
            uInp = input(_menus(6.0))
            uInp = int(uInp)

            # Storing selected car ID
            if uStatus == 1 or uStatus == 2:
                if uInp == 1:
                    carID = loadedCarID[0]
                elif uInp == 2:
                    carID = loadedCarID[1]
                elif uInp == 3:
                    carID = loadedCarID[2]
                elif uInp == 4:
                    carID = loadedCarID[3]
                elif uInp == 5:
                    carID = loadedCarID[4]

            _loader(3)

            # Car Selection
            if uInp >= 1 and uInp <= 5:

                # Guest Mode
                if uStatus == 0:
                    guestInp = 0
                    _screenClr()
                    print(_menus(6.1))
                    while 1 == 1:
                        guestInp = _menuInput("guestCar")
                        if guestInp == 1:
                            pgNum = 2
                            list1.append(pgNum)
                            return list1
                        elif guestInp == 2:
                            pgNum = 1
                            list1.append(pgNum)
                            return list1
                        elif guestInp == 3:
                            break
                        else:
                            print(_menus("badInput"))
                            _loader(3)
                            continue
                    if guestInp == 3:
                        counter = counter - 5
                        _loader(3)
                        continue
                    else:
                        break

                # Member Mode
                # elif uStatus == 1:

                # Admin Mode
                elif uStatus == 2:

                    # View cars available to be rented
                    if mode == 0:
                        print(_menus("badInput"))
                        _loader(3)
                        continue

                    # Modify car details
                    elif mode == 1:
                        while 1 == 1:
                            outputMod = _carModify(carID)
                            _loader(3)
                            if outputMod == 1:
                                _screenClr()
                                print("Car details have successfully updated!")
                            # Ask user for input if they want to modify any more details for the same car ( yes - continue, no - break )

                            elif outputMod == 0:
                            # input for (Process was cancelled! Would you like to try again?)
                            else:
                                break
                        continue

            # Next Car Page
            elif uInp == 6:
                continue

            # Previous Car Page
            elif uInp == 7:
                counter = counter - 10
                continue

            # Back to previous page (exit car page)
            elif uInp == 8:
                if uStatus == 0:
                    pgNum = 0
                    list1.append(pgNum)
                    return list1
                else:
                    pgNum = 3
                    list1.append(pgNum)
                    return list1

        except:
            print(_menus("badInput"))
            counter = -1
            _loader(3)
            continue

    # if endPage != 1:

    return list1





def _carAdd():
    list1 = []
    carData = []
    confirmation = 0
    pgNum = 0
    while 1 == 1:
        _screenClr()

        # Receiving input (new car details)
        carInp = input("=- Car Addition -=\nPlease enter car details in the following format:\n\nID;Model;Type;Status;Rate\n(For status: available - 0, booked - 1)\n\nOther options:\n1 - Back\n\n> ")
        try:
            carInp = int(carInp)
            if carInp == 1:
                pgNum = 3
                list1.append(pgNum)
                _loader(3)
            else:
                print(_menus("badInput"))
                _loader(3)
                continue
        except:
            carData = carInp.split(_constantVar(4))

            # Validating that the user has entered the correct amount of fields
            if len(carData) != 5:
                print(_menus("badInput"))
                _loader(3)
                continue

        if pgNum == 3:
            return list1

        _loader(3)
        while 1 == 1:
            _screenClr()

            # Displaying input details for user to double-check details
            carTemp = "ID: " + carData[0] + "\nModel: " + carData[1] + "\nType: " + carData[2] + "\nStatus: " + carData[3] + "\nRate: " + carData[4]
            print("=- Car Addition -=\n" + carTemp + "\n")
            try:

                # Receiving input (confirmation of details to be added)
                confirmation = input(_menus(4.1))
                confirmation = int(confirmation)
                if confirmation == 1 or confirmation == 2:
                    break
                elif confirmation != 2:
                    print(_menus("badInput"))
                    _loader(3)
                    continue
            except:
                print(_menus("badInput"))
                _loader(3)
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

    # Writing car data into car file
    _newRec(_fileSelect(4), carData)
    _loader(3)
    _screenClr()
    print("Car has been successfully added!\nNow redirecting back to Admin Dashboard.")
    _sleep(0.5)
    _loader(5)
    pgNum = 3
    list1.append(pgNum)
    return list1





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
        if pgNum >= 1 and pgNum <= 4:
            _loader(3)
            if pgNum == 1:
                pgNum = 1
            elif pgNum == 2:
                pgNum = 2
            elif pgNum == 3:
                pgNum = 4
            elif pgNum == 4:
                pgNum = 5
            list1.append(pgNum)
            return list1
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
                list1.append(pgNum)
                return list1
            elif alias == 2:
                _loader(3)
                pgNum = 5
                list1.append(pgNum)
                return list1
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
            return list1

        # Admin Login
        elif uType == 2:
            _loader(3)
            list1 = _login(uType)
            return list1

        # Navigate to previous page
        elif uType == 3:
            _loader(3)
            pgNum = 0
            list1.append(pgNum)
            list1.append(0)
            list1.append("")
            return list1

        # Invalid input detection
        else:
            print(_menus("badInput"))
            _loader(3)
            _screenClr()
            print(_menus(2.4))



def _pageBrowsing(uType, uAlias):
    pgNum = 0
    list1 = []
    while 1 == 1:

        # Go to guest car page
        # if uType == 0:


        # Go to member browsing page
        if uType == 1:
            list1 = _memberBrowse(uAlias)
            return list1

        # Go to admin browsing page
        elif uType == 2:
            list1 = _adminBrowse(uAlias)


def _pageExit(logout):
    list1 = []
    pgNum = 0
    uStatus = 0
    uAlias = ""
    print(_menus(5))

    # Receiving input from the user (page selection)
    while 1 == 1:
        if logout == 1:
            userExit = 1
            break
        else:
            _screenClr()
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
        uStatus = 0
        uAlias = ""

        _sleep(0.5)
        _loader(11)
        _sleep(0.5)
    else:
        pgNum = 0

    list1.append(pgNum)
    list1.append(uStatus)
    list1.append(uAlias)

    return list1



# Main Program
outputList = []
pgNo = 0
userStatus = 0 # 0 - Guest, 1 - Member, 2 - Admin
userAlias = ""
while 1 == 1:
    _screenClr()
    if userStatus == 1 or userStatus == 2:
        pgNo = 3

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
        pgNo = outputList[0]
        userStatus = outputList[1]
        userAlias = outputList[2]
        continue

    # Page 5: Car Pages
    elif pgNo == 4:
        outputList = _carSelect(userStatus, userAlias, 0)
        pgNo = outputList[0]
        continue

    # Page 6: Exit Page
    elif pgNo == 5:
        outputList = _pageExit(0)
        pgNo = outputList[0]
        userStatus = outputList[1]
        userAlias = outputList[2]
        if pgNo == 0:
            continue


    break



