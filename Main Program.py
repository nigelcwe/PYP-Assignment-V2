#NIGEL CHAN WEI EN
#TP059179


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
    print("")





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
            menu = "=- Login -=\nLogin as:\n1 - Member\n2 - Admin\n\nMore options:\n3 - Back\n"

        # Member Dashboard Menus (member browsing page)
        elif num == 3.0:
            menu = "=- Member Dashboard -=\nWhat would you like to do?\n1 - Browse cars\n2 - View rental history\n3 - Log out\n4 - Exit\n"

        # Member Rental History Menu
        elif num == 3.1:
            menu = "\nOptions:\n1 - Next page\n2 - Previous page\n3 - Back\n\nPlease enter a corresponding value:\n> "

        # Admin Dashboard Menus (admin browsing page)
        elif num == 4.0:
            menu = "=- Admin Dashboard -=\nWhat would you like to do?\n1 - Add a car\n2 - Modify car details\n3 - View records (Cars or Payments)\n4 - Search specific records (Bookings or Payments)\n5 - Return a car\n6 - Confirm registrations\n7 - Log out\n8 - Exit\n"
        elif num == 4.1:
            menu = "=- Admin Dashboard -=\nWhat would you like to do?\n1 - View car records\n2 - View payment records\n3 - Back\n"
        elif num == 4.2:
            menu = "=- Admin Dashboard -=\nWhat would you like to do?\n1 - Search for specific bookings\n2 - Search for specific payments\n3 - Back\n"
        elif num == 4.6:
            menu = "=- View Payment Records -=\n\nPlease enter the rental duration (days):\n\n> "
        elif num == 4.7:
            menu = "=- Search Booking Records -=\nWhat would you like to search by?\n1 - Alias\n2 - Car ID\n3 - Back\n"
        elif num == 4.8:
            menu = "=- Search Payment Records -=\nWhat would you like to search by?\n1 - Alias\n2 - Car ID\n3 - Back\n"
        elif num == 4.9:
            menu = "\nOptions:\n1 - Next page\n2 - Previous page\n3 - Change search criteria\n4 - Back to Admin Dashboard\n\nPlease enter a corresponding value:\n> "

        # Registration Confirmation Menus
        elif num == 4.3:
            menu = "\nOther options:\n6 - Next Page\n7 - Previous Page\n8 - Back\n\nPlease enter a corresponding value:\n> "
        elif num == 4.4:
            menu = "=- Confirm Registration -=\nPlease select an option:\n1 - Confirm another user\n2 - Back\n"
        elif num == 4.5:
            menu = "=- Confirm Registration -=\nPlease select an option:\n1 - Try again\n2 - Confirm another user\n3 - Back\n"

        # Exit Page Menus
        elif num == 5.0:
            menu = "Are you sure you want to exit?\n1 - Yes\n2 - No\n"

        # Main Car Page Menus
        elif num == 6.0:
            menu = "\nOther options:\n6 - Next Page\n7 - Previous Page\n8 - Back\n\nPlease enter a corresponding value:\n> "
        elif num == 6.1:
            menu = "=- Car List -=\nWhat would you like to do?\n1 - Login\n2 - Register\n3 - Continue browsing\n"

        # Admin Car Page Menus
        elif num == 7.0:
            menu = "=- Edit Car Details -=\nPlease select details to be modified:\n1 - Car model\n2 - Car type\n3 - Car status\n4 - Rental rate\n5 - Back\n"
        elif num == 7.1:
            menu = "=- Edit Car Details -=\nPlease select an option:\n1 - Continue editing details of selected car\n2 - Choose another car to edit\n3 - Back to Admin Dashboard\n"
        elif num == 7.2:
            menu = "=- Edit Car Details -=\nPlease select an option:\n1 - Try again\n2 - Choose another car to edit\n3 - Back to Admin Dashboard\n"
        elif num == 7.3:
            menu = "=- Car Return -=\nPlease select an option:\n1 - Return another car\n2 - Back to Admin Dashboard\n"
        elif num == 7.4:
            menu = "=- Car Return -=\nPlease select an option:\n1 - Try again\n2 - Return another car\n3 - Back to Admin Dashboard\n"
        elif num == 7.5:
            menu = "=- Edit Car Details -=\nPlease select an option:\n1 - Choose another car to edit\n2 - Back to Admin Dashboard\n"
        elif num == 7.6:
            menu = "Confirm details?\n1 - Yes\n2 - No\n\nPlease enter a corresponding value:\n> "

        # Member Car Page Menus
        elif num == 8.0:
            menu = "=- Car Booking -=\n\nPlease enter the number of days you wish to rent the car for:\n> "
        elif num == 8.1:
            menu = "=- Car Booking -=\nPlease select an option:\n1 - Try again\n2 - Choose another car to edit\n3 - Back to Member Dashboard\n"

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
        var = "|"

    # Layer 3 Separator
    elif num == 3:
        var = "$"

    # Layer 4 Separator
    elif num == 4:
        var = "!"

    # Input Separator
    elif num == 5:
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
            elif menu == "rentalHistory_1":
                print(_menus(3.1))
            elif menu == "adminDash_1":
                print(_menus(4.0))
            elif menu == "adminDash_2":
                print(_menus(4.1))
            elif menu == "adminDash_3":
                print(_menus(4.2))
            elif menu == "guestCar":
                print(_menus(6.1))
            elif menu == "carModify":
                print(_menus(7.0))
            elif menu == "carModify_1":
                print(_menus(7.1))
            elif menu == "carModify_2":
                print(_menus(7.2))
            elif menu == "carModify_3":
                print(_menus(7.5))
            elif menu == "carReturn_1":
                print(_menus(7.3))
            elif menu == "carReturn_2":
                print(_menus(7.4))
            elif menu == "regConfirm_1":
                print(_menus(4.4))
            elif menu == "regConfirm_2":
                print(_menus(4.5))
            elif menu == "carBook_1":
                print(_menus(8.1))
            elif menu == "searchFunctions":
                print(_menus(4.9))
            elif menu == "paymentRecords_1":
                print(_menus(4.8))
            elif menu == "bookingRecords_1":
                print(_menus(4.7))
            elif menu == "exit":
                print(_menus(5))
    # Continue for as many pages as needed

    return(inp)





def _newRec(file, list):
    string = _constantVar(1).join(str(i) for i in list)
    with open(file, "a") as openedFile:
        openedFile.write(string + "\n")





def _regSelect():
    list1 = []
    pgNum = 0
    counter = -1
    pad = " "
    uLine = ""
    uData = []
    uDataTemp = []
    fileList = []
    i = 0
    newList = []
    uInp = 0
    uInp2 = 0
    while 1 == 1:
        i = 0
        loadedUserAlias = []
        if counter < -1:
            counter = -1
        _screenClr()
        with open(_fileSelect(2), "r") as openedFile:
            fileList = openedFile.readlines()
            print("=- Registration List -=\n\tAlias                 Password\n")
            try:
                while i < 5:
                    uLine = fileList[(counter + 1)].rstrip("\n")
                    uData = uLine.split(_constantVar(1))
                    loadedUserAlias.append(uData[0])
                    print(str(i + 1) + " - " + (uData[0] + pad * (20 - len(uData[0]))) + ": " + (uData[1] + pad * (30 - len(uData[1]))))
                    counter = counter + 1
                    i = i + 1
            except:
                print("_______End of List_______")

        try:
            uInp = input(_menus(4.3))
            uInp = int(uInp)

                # Storing loaded user Alias
            if uInp == 1:
                uAlias = loadedUserAlias[0]
            elif uInp == 2:
                uAlias = loadedUserAlias[1]
            elif uInp == 3:
                uAlias = loadedUserAlias[2]
            elif uInp == 4:
                uAlias = loadedUserAlias[3]
            elif uInp == 5:
                uAlias = loadedUserAlias[4]


            if uInp >= 1 and uInp <= 5:
                _loader(3)
                while 1 == 1:
                    _screenClr()
                    try:
                        confirmation = int(input("=- Confirm Registration -=\nUser to be confirmed: " + uAlias + "\n\nConfirm user?\n1 - Yes\n2 - No\n\nPlease enter a corresponding value:\n> "))

                        if confirmation == 1:
                            with open(_fileSelect(2), "r") as openedFile:

                                # Excluding user from original registration file and saving user data
                                for line in openedFile:
                                    uData = line.rstrip("\n").split(_constantVar(1))
                                    if uAlias == uData[0]:
                                        uDataTemp = uData[::]
                                        continue
                                    else:
                                        newList.append(uData)

                            # Writing new list to registration file
                            with open(_fileSelect(2), "w") as openedFile:
                                for ind in range(len(newList)):
                                    uLine = _constantVar(1).join(newList[ind])
                                    openedFile.write(uLine + "\n")

                            # Appending user data into member file
                            _newRec(_fileSelect(1), uDataTemp)

                            _loader(3)
                            _screenClr()
                            print("User has been registered successfully!")
                            _loader(3)
                            while 1 == 1:
                                _screenClr()
                                print(_menus(4.4))
                                uInp2 = _menuInput("regConfirm_1")
                                if uInp2 == 1:
                                    counter = -1
                                    _loader(3)
                                    break
                                elif uInp2 == 2:
                                    _loader(3)
                                    pgNum = 3
                                    list1.append(pgNum)
                                    return list1
                                else:
                                    print(_menus("badInput"))
                                    _loader(3)
                                    continue
                            break

                        # Process Terminated
                        elif confirmation == 2:
                            _loader(3)
                            _screenClr()
                            print("Process was terminated!")
                            _loader(3)
                            while 1 == 1:
                                _screenClr()
                                print(_menus(4.5))
                                uInp2 = _menuInput("regConfirm_2")
                                if uInp2 == 1:
                                    _loader(3)
                                    break
                                elif uInp2 == 2:
                                    _loader(3)
                                    counter = -1
                                    break
                                elif uInp2 == 3:
                                    _loader(3)
                                    pgNum = 3
                                    list1.append(pgNum)
                                    return list1
                                else:
                                    print(_menus("badInput"))
                                    _loader(3)
                                    continue
                            if uInp2 == 1:
                                continue
                            break

                    except:
                        print(_menus("badInput"))
                        _loader(3)
                        continue

            # Next Page
            elif uInp == 6:
                _loader(3)
                continue

            # Previous Page
            elif uInp == 7:
                counter = counter - 10
                _loader(3)
                continue

            # Back to previous menu
            elif uInp == 8:
                _loader(3)
                pgNum = 3
                list1.append(pgNum)
                return list1

            else:
                print(_menus("badInput"))
                counter = -1
                _loader(3)
                continue

        except:
            print(_menus("badInput"))
            counter = -1
            _loader(3)
            continue





def _carModify(carID, mode):          # Mode: (0 - Modify details, 1 - Return car)
    pgNum = 0
    list1 = []
    adminInp = 0
    carList = []
    carListOld = []
    carListNew = []
    adminMod = ""
    newList = []
    newCar = ""
    output = 0
    uData = []
    uDataNew = []
    uNewList = []
    carFind = 0

    if mode == 0:
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
    else:
        adminInp = 3

    if adminInp != 5:
        with open (_fileSelect(4), "r") as openedFile:
            for line in openedFile:
                carList = line.rstrip("\n").split(_constantVar(1))
                if carID == carList[0]:
                    _screenClr()
                    if mode == 1:
                        adminMod = "0"
                    else:
                        adminMod = str(input("=- Edit Car Details -=\nCar to be edited: " + " # ".join(str(i) for i in carList) + "\n\nData to be edited: " + carList[adminInp] + "\n\nPlease enter the new data:\n> "))
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
                confirmation = int(input("=- Edit Car Details -=\nConfirm the following changes?\n\nOriginal: " + " # ".join(str(i) for i in carListOld) + "\nEdited  : " + " # ".join(str(i) for i in carListNew) + "\n\n1 - Yes\n2 - No\n\nPlease enter a corresponding value:\n> "))
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

        # Modify Mode Output (1 = successful, 2 = failed [process terminated], 3 = failed [car is being rented])
        if mode == 0:
            if confirmation == 1:

                # Checking if car is being rented
                with open(_fileSelect(1), "r") as openedFile:
                    for line in openedFile:
                        if carID == line.rstrip("\n").split(_constantVar(1))[2]:
                            output = 3
                            return output

                # Updating car file
                with open(_fileSelect(4), "w") as openedFile:
                    for ind in range(len(newList)):
                        newCar = _constantVar(1).join(newList[ind])
                        openedFile.write(newCar + "\n")
                    output = 1
                    return output

            elif confirmation == 2:
                output = 2
                return output

        # Return Mode Output (1 = successful, 2 = failed [process terminated], 3 = failed[carID not found in member file])
        elif mode == 1:
            if confirmation == 1:
                with open(_fileSelect(1), "r") as openedFile:
                    carFind = 0
                    for line in openedFile:
                        uData = line.rstrip("\n").split(_constantVar(1))
                        if carID == uData[2]:
                            uDataNew = uData[::]
                            uDataNew[2] = ""
                            uNewList.append(uDataNew)
                            carFind = 1
                        else:
                            uNewList.append(uData)

                # Car is currently rented by a user
                if carFind == 1:

                    # Updating member file
                    with open(_fileSelect(1), "w") as openedFile:
                        for ind in range(len(uNewList)):
                            uLineNew = _constantVar(1).join(uNewList[ind])
                            openedFile.write(uLineNew + "\n")

                    # Updating car file
                    with open(_fileSelect(4), "w") as openedFile:
                        for ind in range(len(newList)):
                            newCar = _constantVar(1).join(newList[ind])
                            openedFile.write(newCar + "\n")

                    _screenClr()
                    print(uDataNew[0] + " has successfully returned car: " + carListNew[1] + " (ID: " + carID + ")")
                    output = 1
                    return output

                elif carFind == 0:
                    _screenClr()
                    print("Error: Car is not currently being rented by any users.")
                    output = 3
                    return output

            elif confirmation == 2:
                output = 2
                return output

    else:
        output = 2
        return output





def _carBooking(uAlias, carID):         # Output: 1 = Successfully booked, 2 = Process terminated, 3 = User already booked a car
    pgNum = 0
    list1 = []
    uListNew = []
    carListNew = []
    carData = []
    carDataTemp = []
    carDataNew = []
    uData = []
    uDataNew = []
    paymentData = []
    bookingData = []
    rentalHistory = ""
    rentalHistory1 = ""
    rentalHistory1List = []
    paymentDateTime = ""
    paymentTimeData = []
    confirmation = 0
    dayNum = 0
    amtDue = 0

    _screenClr()

    # Retrieving car data in a list
    with open(_fileSelect(4), "r") as openedFile:
        for line in openedFile:
            carData = line.rstrip("\n").split(_constantVar(1))
            if carID == carData[0]:
                break

    # Retrieving user data in a list
    with open(_fileSelect(1), "r") as openedFile:
        for line in openedFile:
            uData = line.rstrip("\n").split(_constantVar(1))
            if uAlias == uData[0]:
                rentalHistory1List = uData[3].split(_constantVar(2))
                break

    while 1 == 1:
        try:
            _screenClr()
            if uData[2] != "":
                output = 3
                return output

            # Receiving input (number of days for car to be rented)
            dayNum = int(input(_menus(8.0)))
            _loader(3)
            _screenClr()

            # Receiving input (user confirmation)
            confirmation = int(input("=- Car Booking -=\nBook the following car?\nID             : " + str(carData[0]) + "\nModel          : " + str(carData[1]) + "\nType           : " + str(carData[2]) + "\nRate(per day)  : RM " + str(carData[4]) + "\nDays           : " + str(dayNum) + "\n\nOptions:\n1 - Yes\n2 - No (Back to browsing page)\n\nPlease enter a corresponding value:\n> "))
            if confirmation == 1:
                _loader(3)
                while 1 == 1:
                    _screenClr()
                    try:

                        # Calculation of payment
                        amtDue = int(carData[4]) * int(dayNum)

                        # Receiving user payment
                        amtPayment = int(input("=- Car Booking -=\nAmount due: RM " + str(amtDue) + "\n\nPlease enter payment amount:\n\n> RM "))
                        difference = amtPayment - amtDue
                        if difference > 0:
                            print("Payment amount is greater than amount due! Please try again.")
                            _loader(3)
                            continue
                        elif difference < 0:
                            print("Payment amount is less than amount due! Please try again.")
                            _loader(3)
                            continue
                        _loader(3)
                        _screenClr()
                        print("Payment accepted!")

                        # Preparing Payment Time Data List
                        paymentDateTime = str(datetime.now())
                        paymentTimeData.append(paymentDateTime.split(" ")[0])
                        paymentTimeData.append(paymentDateTime.split(" ")[1])

                        # Preparing Rental History String
                        carDataTemp = carData[::]
                        carDataTemp.append(_constantVar(4).join(paymentTimeData))
                        carDataTemp.append(str(dayNum))
                        rentalHistory = _constantVar(3).join(carDataTemp)
                        if rentalHistory1List[0] == "":
                            rentalHistory1List[0] = rentalHistory
                        else:
                            rentalHistory1List.append(rentalHistory)
                        rentalHistory1 = _constantVar(2).join(rentalHistory1List)

                        # Preparing User Data List
                        uDataNew = uData[::]
                        uDataNew[2] = carData[0][::]
                        uDataNew[3] = rentalHistory1

                        # Preparing Car Data List
                        carDataNew = carData[::]
                        carDataNew[3] = "1"

                        # Preparing Booking Data List
                        bookingData.append(uData[0][::])
                        bookingData.append(_constantVar(2).join(carDataNew))
                        bookingData.append(_constantVar(2).join(paymentTimeData))
                        bookingData.append(str(dayNum))

                        # Preparing Payment Data List
                        paymentData.append(uData[0][::])
                        paymentData.append(amtPayment)
                        paymentData.append(carData[0][::])
                        paymentData.append(str(dayNum))
                        paymentData.append(_constantVar(2).join(paymentTimeData))

                        # Updating User File
                        with open(_fileSelect(1), "r") as openedFile:
                            uListNew = []
                            for line in openedFile:
                                uData = line.rstrip("\n").split(_constantVar(1))
                                if uAlias == uData[0]:
                                    uListNew.append(uDataNew)
                                else:
                                    uListNew.append(uData)

                        with open(_fileSelect(1), "w") as openedFile:
                            for ind in range(len(uListNew)):
                                uNew = _constantVar(1).join(uListNew[ind])
                                openedFile.write(uNew + "\n")

                        # Updating Car File
                        with open(_fileSelect(4), "r") as openedFile:
                            carListNew = []
                            for line in openedFile:
                                carData = line.rstrip("\n").split(_constantVar(1))
                                if carID == carData[0]:
                                    carListNew.append(carDataNew)
                                else:
                                    carListNew.append(carData)

                        with open(_fileSelect(4), "w") as openedFile:
                            for ind in range(len(carListNew)):
                                carNew = _constantVar(1).join(carListNew[ind])
                                openedFile.write(carNew + "\n")

                        # Adding new record to payment file
                        _newRec(_fileSelect(5), paymentData)

                        # Adding new record to booking file
                        _newRec(_fileSelect(6), bookingData)

                        _loader(3)
                        output = 1
                        _screenClr()
                        print("Successfully booked car: " + carDataNew[1] + " (ID: " + carDataNew[0] + ")")
                        _sleep(0.5)
                        _loader(5)
                        return output

                    except:
                        print(_menus("badInput"))
                        _loader(3)
                        continue

            # User cancels booking (terminates process)
            elif confirmation == 2:
                _loader(3)
                output = 2
                return output

            else:
                print(_menus("badInput"))
                _loader(3)
                continue

        except:
            print(_menus("badInput"))
            _loader(3)
            continue





def _carSelect(uStatus, uAlias = "", mode = 0):        # mode: Admin  (0 = View all cars, 1 = Modify, 2 = Return)
    carLine = ""                                       #       Member (0 = Select car to book [only shows available cars])
    carData = []
    counter = -1
    fileList = []
    pad = " "
    list1 = []
    pgNum = 0
    carID = ""
    i = 0
    while 1 == 1:
        i = 0
        loadedCarID = []
        if counter < -1:
            counter = -1
        _screenClr()
        with open (_fileSelect(4), "r") as openedFile:
            fileList = openedFile.readlines()
            print("=- Cars List -=\n\tModel                       Type                Status              Rate(per day)           ID\n")
            try:
                while i < 5 :
                    carLine = fileList[(counter + 1)].rstrip("\n")
                    carData = carLine.split(_constantVar(1))

                    # For members to view only cars that are available for rental
                    if  uStatus == 1 and mode == 0:
                        if int(carData[3]) == 1:
                            counter = counter + 1
                            continue

                    loadedCarID.append(carData[0])
                    if int(carData[3]) == 0:
                        carData[3] = "Available"
                    elif int(carData[3]) == 1:
                        carData[3] = "Unavailable"

                    print(str(i + 1) + " - " + (carData[1] + pad * (20 - len(carData[1]))) + "\t:\t" + (carData[2] + pad * (15 - len(carData[2]))) + "\t:\t" + (carData[3] + pad * (15 - len(carData[3]))) + "\t:\tRM " + (carData[4] + pad * (13 - len(carData[4]))) + "\t:\t" + (carData[0] + pad * (15 - len(carData[0]))))
                    counter = counter + 1
                    i = i + 1
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

            # Car Selection
            if uInp >= 1 and uInp <= 5:

                # Guest Mode
                if uStatus == 0:
                    _loader(3)
                    _screenClr()
                    print("Browsing as guest!")
                    _sleep(0.5)
                    _loader(3)
                    guestInp = 0
                    while 1 == 1:
                        _screenClr()
                        print(_menus(6.1))
                        guestInp = _menuInput("guestCar")
                        if guestInp == 1:
                            pgNum = 2
                            list1.append(pgNum)
                            _loader(3)
                            return list1
                        elif guestInp == 2:
                            pgNum = 1
                            list1.append(pgNum)
                            _loader(3)
                            return list1
                        elif guestInp == 3:
                            break
                        else:
                            print(_menus("badInput"))
                            _loader(3)
                            _screenClr()
                            print(_menus(6.1))
                            continue
                    if guestInp == 3:
                        counter = counter - 5
                        _loader(3)
                        continue
                    else:
                        break

                # Member Mode
                elif uStatus == 1:
                    _loader(3)
                    while 1 == 1:
                        outputBook = _carBooking(uAlias, carID)
                        if outputBook == 1:
                            pgNum = 3
                            list1.append(pgNum)
                            return list1
                        elif outputBook == 2:
                            _screenClr()
                            print("Process was terminated!")

                        elif outputBook == 3:
                            _screenClr()
                            print("Error: User is currently renting a car.")
                            _loader(3)
                            pgNum = 3
                            list1.append(pgNum)
                            return list1

                        _sleep(0.5)
                        _loader(5)
                        while 1 == 1:
                            memInp = 0
                            _screenClr()
                            print(_menus(8.1))
                            memInp = _menuInput("carBook_1")
                            if memInp == 1:
                                _loader(3)
                                break
                            elif memInp == 2:
                                _loader(3)
                                counter = -1
                                break
                            elif memInp == 3:
                                _loader(3)
                                pgNum = 3
                                list1.append(pgNum)
                                return list1
                            else:
                                print(_menus("badInput"))
                                _loader(3)
                                continue

                        if memInp == 1:
                            continue
                        else:
                            break
                    continue

                # Admin Mode
                elif uStatus == 2:

                    # View cars available to be rented
                    if mode == 0:
                        print(_menus("badInput"))
                        counter = -1
                        _loader(3)
                        continue

                    # Modify car details
                    elif mode == 1:
                        _loader(3)
                        while 1 == 1:
                            adminSelect1 = 0
                            outputMod = _carModify(carID, 0)

                            _screenClr()
                            if outputMod == 1:
                                print("Car details have successfully updated!")
                            elif outputMod == 2:
                                print("Process was terminated!")
                            elif outputMod == 3:
                                print("Error! Car is currently rented by a user.")
                            _sleep(0.5)
                            _loader(5)
                            while 1 == 1:
                                _screenClr()
                                if outputMod == 1:
                                    print(_menus(7.1))
                                    adminSelect1 = _menuInput("carModify_1")
                                elif outputMod == 2:
                                    print(_menus(7.2))
                                    adminSelect1 = _menuInput("carModify_2")
                                elif outputMod == 3:
                                    print(_menus(7.5))
                                    adminSelect1 = _menuInput("carModify_3")
                                if adminSelect1 == 1:
                                    if outputMod == 3:
                                        counter = -1
                                    _loader(3)
                                    break
                                elif adminSelect1 == 2:
                                    if outputMod == 3:
                                        _loader(3)
                                        pgNum = 3
                                        list1.append(pgNum)
                                        return list1
                                    else:
                                        counter = -1
                                        _loader(3)
                                        break
                                elif adminSelect1 == 3 and outputMod != 3:
                                    _loader(3)
                                    pgNum = 3
                                    list1.append(pgNum)
                                    return list1
                                else:
                                    print(_menus("badInput"))
                                    _loader(3)
                                    continue
                            if adminSelect1 == 1 and outputMod != 3:
                                continue
                            else:
                                break
                        continue

                    # Car Return Functionality
                    elif mode == 2:
                        _loader(3)
                        while 1 == 1:
                            adminSelect2 = 0
                            outputMod = _carModify(carID, 1)

                            if outputMod == 2:
                                _screenClr()
                                print("Process was terminated!")
                            _sleep(0.5)
                            _loader(5)
                            while 1 == 1:
                                if outputMod == 1:
                                    _screenClr()
                                    print(_menus(7.3))
                                    adminSelect2 = _menuInput("carReturn_1")
                                    if adminSelect2 == 1:
                                        counter = -1
                                        _loader(3)
                                        break
                                    elif adminSelect2 == 2:
                                        _loader(3)
                                        pgNum = 3
                                        list1.append(pgNum)
                                        return list1
                                    else:
                                        print(_menus("badInput"))
                                        _loader(3)
                                        continue
                                elif outputMod == 2:
                                    _screenClr()
                                    print(_menus(7.4))
                                    adminSelect2 = _menuInput("carReturn_2")
                                    if adminSelect2 == 1:
                                        _loader(3)
                                        break
                                    if adminSelect2 == 2:
                                        counter = -1
                                        _loader(3)
                                        break
                                    else:
                                        print(_menus("badInput"))
                                        _loader(3)
                                        continue
                                elif outputMod == 3:
                                    counter = -1
                                    break

                            if adminSelect2 == 1 and outputMod == 0:
                                continue

                            else:
                                break
                        continue

            # Next Car Page
            elif uInp == 6:
                _loader(3)
                continue

            # Previous Car Page
            elif uInp == 7:
                _loader(3)
                counter = counter - 10
                continue

            # Back to previous page (exit car page)
            elif uInp == 8:
                _loader(3)
                if uStatus == 0:
                    pgNum = 0
                    list1.append(pgNum)
                    return list1
                else:
                    pgNum = 3
                    list1.append(pgNum)
                    return list1

            else:
                print(_menus("badInput"))
                counter = -1
                _loader(3)
                continue

        except:
            print(_menus("badInput"))
            counter = -1
            _loader(3)
            continue

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
                return list1
            else:
                print(_menus("badInput"))
                _loader(3)
                continue
        except:
            carData = carInp.split(_constantVar(5))

            # Validating that the user has entered the correct amount of fields
            if len(carData) != 5:
                print(_menus("badInput"))
                _loader(3)
                continue

        _loader(3)
        while 1 == 1:
            _screenClr()

            # Displaying input details for user to double-check details
            carTemp = "ID: " + carData[0] + "\nModel: " + carData[1] + "\nType: " + carData[2] + "\nStatus: " + carData[3] + "\nRate: " + carData[4]
            print("=- Car Addition -=\n" + carTemp + "\n")
            try:

                # Receiving input (confirmation of details to be added)
                confirmation = input(_menus(7.6))
                confirmation = int(confirmation)
                if confirmation == 1 or confirmation == 2:
                    _loader(3)
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
            _screenClr()
            inval = 0

            # Checking for proper syntax of car ID
            if inval == 0 and carData[0].startswith("CA") == False:
                print("Invalid car ID detected! Please try again.")
                inval = 1

            if inval == 0:
                try:
                    IDNum = int(carData[0][2::])
                except:
                    print("Invalid car ID detected! Please try again.")
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




def _rentalHistory(uAlias):
    pgNum = 0
    list1 = []
    uData = []
    uRentalHistory = []
    rentalData = []
    counter = 0

    while 1 == 1:
        _screenClr()
        if counter < 0 :
            counter = 0
        with open(_fileSelect(1), "r") as openedFile:
            for line in openedFile:
                uData = line.rstrip("\n").split(_constantVar(1))
                if uAlias == uData[0]:
                    uRentalHistory = uData[3].split(_constantVar(2))
                    try:
                        rentalData = uRentalHistory[counter].split(_constantVar(3))
                        if rentalData[0] == "":
                            rentalData = ["Null", "Null", "Null", "Null", "Null", "Null!Null", "Null"]
                        break
                    except:
                        rentalData = ["Null", "Null", "Null", "Null", "Null", "Null!Null", "Null"]
                        break

        print("=- Rental History -=\nCar ID    : " + rentalData[0] + "\nModel     : " + rentalData[1] + "\nType      : " + rentalData[2] + "\nDate      : " + rentalData[5].split(_constantVar(4))[0] + "\nTime      : " +rentalData[5].split(_constantVar(4))[1] + "\nDays      : " + rentalData[6])
        if rentalData[0] == "Null":
            print("\n_______End of List_______")

        # Receiving user input (page navigation)
        memInp = input(_menus(3.1))

        # Checking for integer only input
        try:
            memInp = int(memInp)
        except:
            print(_menus("badInput"))
            _loader(3)
            continue

        # Checking for end of list
        if memInp == 1:
            if rentalData[0] != "Null":
                counter = counter + 1
            else:
                counter = counter
            _loader(3)
            continue
        elif memInp == 2:
            counter = counter - 1
            _loader(3)
            continue
        elif memInp == 3:
            pgNum = 3
            list1.append(pgNum)
            _loader(3)
            return list1
        else:
            print(_menus("badInput"))
            _loader(3)
            continue




def _paySearchDur():
    pgNum = 0
    list1 = []
    recData = []
    findList = []
    loadedList = []
    findCount = 0
    counter = -1
    pad = " "
    recList = []
    while 1 == 1:
        counter = -1
        findCount = 0
        findList = []
        loadedList = []
        try:
            _screenClr()
            uInp = int(input(_menus(4.6)))
            _loader(3)
            _screenClr()
            uInp2 = int(input("=- View Payment Records -=\nDays      : " + str(uInp) + "\n\nOptions:\n1 - Proceed to view records\n2 - Back\n\nPlease enter a corresponding value:\n> "))
            if uInp2 == 1:
                _loader(3)
                with open(_fileSelect(5), "r") as openedFile:
                    for line in openedFile:
                        recData = line.rstrip("\n").split(_constantVar(1))
                        if int(recData[3]) == uInp:
                            findList.append(recData)
                            findCount = findCount + 1

                    if findCount == 0:
                        _screenClr()
                        print("No records with rental duration of " + str(uInp) + " found!")
                        _sleep(0.5)
                        _loader(3)
                        pgNum = 3
                        list1.append(pgNum)
                        return list1

            elif uInp2 == 2:
                _loader(3)
                pgNum = 3
                list1.append(pgNum)
                return list1

            else:
                print(_menus("badInput"))
                _loader(3)
                continue

        except:
            print(_menus("badInput"))
            _loader(3)
            continue

        while 1 == 1:
            i = 0
            loadedList = []
            if counter < -1:
                counter = -1
            _screenClr()
            print("=- Payment List -=\n\tAlias                       Amount                  Car ID              Duration            Date                Time\n")
            try:
                while i < 5:
                    loadedList = findList[(counter + 1)]
                    print(str(i + 1) + " - " + (loadedList[0] + pad * (20 - len(loadedList[0]))) + "\t:\tRM " + (loadedList[1] + pad * (13 - len(loadedList[1]))) + "\t:\t" + (loadedList[2] + pad * (15 - len(loadedList[2]))) + "\t:\t" + (loadedList[3] + pad * (15 - len(loadedList[3]))) + "\t:\t" + (loadedList[4].split(_constantVar(2))[0] + pad * (15 - len(loadedList[4].split(_constantVar(2))[0]))) + "\t:\t" + (loadedList[4].split(_constantVar(2))[1] + pad * (15 - len(loadedList[4].split(_constantVar(2))[1]))))
                    counter = counter + 1
                    i = i + 1
            except:
                print("_______End of List_______")

            try:
                uInp3 = int(input(_menus(4.9)))
                if uInp3 == 1:
                    _loader(3)
                    continue
                elif uInp3 == 2:
                    counter = counter - 10
                    _loader(3)
                    continue
                elif uInp3 == 3:
                    _loader(3)
                    break
                elif uInp3 == 4:
                    pgNum = 3
                    list1.append(pgNum)
                    _loader(3)
                    return list1
                else:
                    print(_menus("badInput"))
                    counter = counter - 5
                    _loader(3)
                    continue

            except:
                print(_menus("badInput"))
                counter = counter - 5
                _loader(3)
                continue
        continue





def _bookingSearch():
    pgNum = 0
    list1 = []
    recData = []
    findList = []
    loadedList = []
    findCount = 0
    counter = -1
    pad = " "
    recList = []
    while 1 == 1:
        counter = -1
        findCount = 0
        findList = []
        loadedList = []
        try:
            _screenClr()
            print(_menus(4.7))
            uInp = _menuInput("bookingRecords_1")
            _loader(3)
            _screenClr()
            if uInp == 1:
                uInp2 = input("=- Search Booking Records -=\n\nPlease enter an alias:\n\n> ")
            elif uInp == 2:
                uInp2 = input("=- Search Booking Records -=\n\nPlease enter a car ID:\n\n> ")
            elif uInp == 3:
                pgNum = 3
                list1.append(pgNum)
                return list1
            else:
                print(_menus("badInput"))
                _loader(3)
                continue

            _loader(3)
            with open(_fileSelect(6), "r") as openedFile:
                for line in openedFile:
                    recList = line.rstrip("\n").split(_constantVar(1))
                    recList[1] = recList[1].split(_constantVar(2))
                    recList[2] = recList[2].split(_constantVar(2))
                    recData = recList
                    if (uInp == 1 and recData[0] == uInp2) or (uInp == 2 and recData[1][0] == uInp2):
                        findList.append(recData)
                        findCount = findCount + 1

                if findCount == 0:
                    _screenClr()
                    if uInp == 1:
                        print("No records with alias of " + uInp2 + " found!")
                    elif uInp == 2:
                        print("No records with car ID of " + uInp2 + " found!")
                    _sleep(0.5)
                    _loader(3)
                    pgNum = 3
                    list1.append(pgNum)
                    return list1

        except:
            print(_menus("badInput"))
            _loader(3)
            continue

        while 1 == 1:
            i = 0
            loadedList = []
            if counter < -1:
                counter = -1
            _screenClr()
            print("=- Booking List -=\n\tAlias                       Car ID              Model                       Days                Date                Time\n")
            try:
                while i < 5:
                    loadedList = findList[(counter + 1)]
                    print(str(i + 1) + " - " + (loadedList[0] + pad * (20 - len(loadedList[0]))) + "\t:\t" + (loadedList[1][0] + pad * (15 - len(loadedList[1][0]))) + "\t:\t" + (loadedList[1][1] + pad * (20 - len(loadedList[1][1]))) + "\t:\t" + (loadedList[3] + pad * (15 - len(loadedList[3]))) + "\t:\t" + (loadedList[2][0] + pad * (15 - len(loadedList[2][0]))) + "\t:\t" + (loadedList[2][1] + pad * (15 - len(loadedList[2][1]))))
                    counter = counter + 1
                    i = i + 1
            except:
                print("_______End of List_______")

            try:
                uInp3 = int(input(_menus(4.9)))
                if uInp3 == 1:
                    _loader(3)
                    continue
                elif uInp3 == 2:
                    counter = counter - 10
                    _loader(3)
                    continue
                elif uInp3 == 3:
                    _loader(3)
                    break
                elif uInp3 == 4:
                    pgNum = 3
                    list1.append(pgNum)
                    _loader(3)
                    return list1
                else:
                    print(_menus("badInput"))
                    counter = counter - 5
                    _loader(3)
                    continue

            except:
                print(_menus("badInput"))
                counter = counter - 5
                _loader(3)
                continue
        continue





def _paySearch():
    pgNum = 0
    list1 = []
    recData = []
    findList = []
    loadedList = []
    findCount = 0
    counter = -1
    pad = " "
    recList = []
    while 1 == 1:
        counter = -1
        findCount = 0
        findList = []
        loadedList = []
        try:
            _screenClr()
            print(_menus(4.8))
            uInp = _menuInput("paymentRecords_1")
            _loader(3)
            _screenClr()
            if uInp == 1:
                uInp2 = input("=- Search Payment Records -=\n\nPlease enter an alias:\n\n> ")
            elif uInp == 2:
                uInp2 = input("=- Search Payment Records -=\n\nPlease enter a car ID:\n\n> ")
            elif uInp == 3:
                pgNum = 3
                list1.append(pgNum)
                return list1
            else:
                print(_menus("badInput"))
                _loader(3)
                continue

            _loader(3)
            with open(_fileSelect(5), "r") as openedFile:
                for line in openedFile:
                    recData = line.rstrip("\n").split(_constantVar(1))
                    if (uInp == 1 and recData[0] == uInp2) or (uInp == 2 and recData[2] == uInp2):
                        findList.append(recData)
                        findCount = findCount + 1

                if findCount == 0:
                    _screenClr()
                    if uInp == 1:
                        print("No records with alias of " + uInp2 + " found!")
                    elif uInp == 2:
                        print("No records with car ID of " + uInp2 + " found!")
                    _sleep(0.5)
                    _loader(3)
                    pgNum = 3
                    list1.append(pgNum)
                    return list1

        except:
            print(_menus("badInput"))
            _loader(3)
            continue

        while 1 == 1:
            i = 0
            loadedList = []
            if counter < -1:
                counter = -1
            _screenClr()
            print("=- Payment List -=\n\tAlias\t\t\t\t\t\tAmount\t\t\t\t\tCar ID\t\t\t\tDuration\t\t\tDate\t\t\t\tTime\n")
            try:
                while i < 5:
                    loadedList = findList[(counter + 1)]
                    print(str(i + 1) + " - " + (loadedList[0] + pad * (20 - len(loadedList[0]))) + "\t:\tRM " + (loadedList[1] + pad * (13 - len(loadedList[1]))) + "\t:\t" + (loadedList[2] + pad * (15 - len(loadedList[2]))) + "\t:\t" + (loadedList[3] + pad * (15 - len(loadedList[3]))) + "\t:\t" + (loadedList[4].split(_constantVar(2))[0] + pad * (15 - len(loadedList[4].split(_constantVar(2))[0]))) + "\t:\t" + (loadedList[4].split(_constantVar(2))[1] + pad * (15 - len(loadedList[4].split(_constantVar(2))[1]))))
                    counter = counter + 1
                    i = i + 1
            except:
                print("_______End of List_______")

            try:
                uInp3 = int(input(_menus(4.9)))
                if uInp3 == 1:
                    _loader(3)
                    continue
                elif uInp3 == 2:
                    counter = counter - 10
                    _loader(3)
                    continue
                elif uInp3 == 3:
                    _loader(3)
                    break
                elif uInp3 == 4:
                    pgNum = 3
                    list1.append(pgNum)
                    _loader(3)
                    return list1
                else:
                    print(_menus("badInput"))
                    counter = counter - 5
                    _loader(3)
                    continue

            except:
                print(_menus("badInput"))
                counter = counter - 5
                _loader(3)
                continue
        continue





def _pwValidation(pw):
    pwInvalidChars = ["\\", "#", "|", ".", ";"]
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
            elif alias == 2:
                _loader(3)
                pgNum = 5
                break
            else:
                print(_menus("badInput"))
                _loader(3)
                continue

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


def _memberBrowse(uAlias):
    pgNum = 0
    list1 = []
    oList = []
    uData = ""
    uDetails = ""

    # Page navigation stuff
    while 1 == 1:
        _screenClr()
        print(_menus(3.0))
        uInput = _menuInput("userDash_1")
        if uInput == 1:
            _loader(3)
            list1 = _carSelect(1, uAlias, 0)
            continue
        elif uInput == 2:
            _loader(3)
            list1 = _rentalHistory(uAlias)
            continue
        elif uInput == 3:
            _loader(3)
            list1 = _pageExit(1, uAlias, 1)
            return list1
        elif uInput == 4:
            _loader(3)
            list1 = _pageExit(1, uAlias, 0)
            return list1
        else:
            print(_menus("badInput"))
            _loader(3)
            continue





def _adminBrowse(uAlias):
    pgNum = 0
    list1 = []
    while 1 == 1:
        _screenClr()
        print(_menus(4.0))
        uInput = _menuInput("adminDash_1")

        # Admin Functionality: Add Cars
        if uInput == 1:
            _loader(3)
            list1 = _carAdd()
            continue

        # Admin Functionality: Modify Car Details
        elif uInput == 2:
            _loader(3)
            list1 = _carSelect(2, uAlias, 1)
            continue

        # Admin Functionality: View Records (Cars/Payments)
        elif uInput == 3:
            _loader(3)
            while 1 == 1:
                _screenClr()
                print(_menus(4.1))
                uInput2 = _menuInput("adminDash_2")
                if uInput2 == 1:
                    _loader(3)
                    list1 = _carSelect(2, uAlias, 0)
                    break
                elif uInput2 == 2:
                    _loader(3)
                    list1 = _paySearchDur()
                    break
                elif uInput2 == 3:
                    _loader(3)
                    break
                else:
                    print(_menus("badInput"))
                    _loader(3)
                    continue
            continue

        # Admin Functionality: Search Records (Bookings/Payments)
        elif uInput == 4:
            _loader(3)
            while 1 == 1:
                _screenClr()
                print(_menus(4.2))
                uInput2 = _menuInput("adminDash_3")
                if uInput2 == 1:
                    _loader(3)
                    list1 = _bookingSearch()
                    break
                elif uInput2 == 2:
                    _loader(3)
                    list1 = _paySearch()
                    break
                elif uInput2 == 3:
                    _loader(3)
                    break
                else:
                    print(_menus("badInput"))
                    _loader(3)
                    continue
            continue

        # Admin Functionality: Return A Car
        elif uInput == 5:
            _loader(3)
            list1 = _carSelect(2, uAlias, 2)
            continue

        # Admin Functionality: Confirm Registration
        elif uInput == 6:
            _loader(3)
            list1 = _regSelect()
            continue

        # Logout
        elif uInput == 7:
            _loader(3)
            list1 = _pageExit(2, uAlias, 1)
            return list1

        # Exit
        elif uInput == 8:
            _loader(3)
            list1 = _pageExit(2, uAlias, 0)
            return list1

        else:
            print(_menus("badInput"))
            _loader(3)
            continue





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
            pgNum = 4
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

        # Go to member browsing page
        if uType == 1:
            list1 = _memberBrowse(uAlias)
            list1.append(1)
            list1.append(uAlias)
            return list1

        # Go to admin browsing page
        elif uType == 2:
            list1 = _adminBrowse(uAlias)
            list1.append(2)
            list1.append(uAlias)
            return list1


def _pageExit(uStatus, uAlias, logout):
    list1 = []
    pgNum = 0

    # Receiving input from the user (page selection)
    while 1 == 1:
        if logout == 1:
            userExit = 1
            break
        else:
            _screenClr()
            print(_menus(5))
            userExit = _menuInput("exit")
            if userExit >= 1 and userExit <=2:
                _loader(3)
                break
            else:
                print(_menus("badInput"))
                _loader(3)

    # Executing user's selected option
    if userExit == 1:
        _screenClr()
        print("Thank you for using our services!")
        if logout == 1:
            pgNum = 0
        elif logout == 0:
            pgNum = -1

        # Clearing account data
        uStatus = 0
        uAlias = ""

        list1.append(pgNum)
        list1.append(uStatus)
        list1.append(uAlias)
        _sleep(0.5)
        _loader(11)
        _sleep(0.5)
    else:
        if uStatus == 1 or uStatus == 2:
            pgNum = 3
            list1.append(pgNum)
            list1.append(uStatus)
            list1.append(uAlias)

        else:
            pgNum = 0
            uAlias = ""
            uStatus = 0
            list1.append(pgNum)
            list1.append(uStatus)
            list1.append(uAlias)

    return list1



# Main Program
from datetime import *
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
        outputList = _pageExit(userStatus, userAlias, 0)
        pgNo = outputList[0]
        try:
            userStatus = outputList[1]
            userAlias = outputList[2]
            continue
        except:
            continue

    elif pgNo == -1:
        break

    continue



