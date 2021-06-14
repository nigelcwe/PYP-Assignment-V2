

def _rentalHistory(uAlias):
    pgNum = 0
    list1 = []
    uData = []
    uRentalHistory = []
    counter = 0

    while 1 == 1:
        with open("memberList.txt", "r") as openedFile:
            for line in openedFile:
                uData = line.rstrip("\n").split("#")
                if uAlias == uData[0]:
                    uRentalHistory = uData[3].split("|")
                    try:
                        rentalData = uRentalHistory[counter].split("$")
                        break
                    except:
                        rentalData = ["Null", "Null", "Null", "Null", "Null", "Null!Null", "Null"]
                        break

        if rentalData[0] != "Null":
            print(rentalData)
            print("=- Rental History -=\nCar ID    : " + rentalData[0] + "\nModel     : " + rentalData[1] + "\nType      : " + rentalData[2] + "\nDate      : " + rentalData[5].split("!")[0] + "\nTime      : " + rentalData[5].split("!")[1] + "\nDays      : " + rentalData[6])

        else:
            print("=- Rental History -=\nCar ID    : " + rentalData[0] + "\nModel     : " + rentalData[1] + "\nType      : " + rentalData[2] + "\nDate      : " + rentalData[5].split(_constantVar(4)[0]) + "\nTime      : " + rentalData[5].split(_constantVar(4)[1]) + "\nDays      : " +rentalData[6])
            print("_______End of List_______")



list1 = []

list1 = _rentalHistory("Alexis")
# print(list1)
# if list1[0] == "":
#     list1 = ["Null", "Null", "Null", "Null", "Null"]
#
# print("=- Rental History -=\nCar ID    : " + list1[0] + "\nModel     : " + list1[1] + "\nType      : " + list1[2] + "\nDate      : " + list1[5].split("!")[0] + "\nTime      : " + list1[5].split("!")[1] + "\nDays      : " + list1[6])