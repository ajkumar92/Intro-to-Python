

lstTable = open("Student.txt", "r")
for dicRow in lstTable:
    lstRow = row.split(",")
    lstTable = {"Code":lstRow[0].strip(),"Student":lstRow[1].strip(),"Course":lstRow[2].strip()}
    lstTable.append(dicRow)
lstTable.close()

while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print("")

    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["Code"] + ',' + dicRow["Student"] + ',' + dicRow["Course"] + ',')
        print("Please choose your option? ")

        continue

    elif(strChoice.strip() == '2'):
        strCode = str(input("What is Code Item? ")).strip()
        strStudent = str(input("Who is the Student? ")).strip()
        strCourse = str(input("What is the Course?" )).strip()
        dicRow = {"Code": strCode, "Student": strStudent, "Course": strCourse}
        lstTable.append(dicRow)
        print("Current Data in table:")
        for dicRow in lstTable:
            print('Please chose your option? ')
        for dicRow in lstTable:
            print(dicRow["Code"] + ',' + dicRow["Student"] + ',' + dicRow["Course"] + ',')
        print('Please chose your option? ')

        continue

    elif(strChoice.strip() == '3'):
        strKeyToRemove = input("Which TASK would you like removed? ")
        blnItemRemoved = False
        intRowNumber = 0
        while(intRowNumber) < len(lstTable):
            if strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0]):
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        if blnItemRemoved == True:
            print("The entry was removed.")
        else:
            print("The Entry was not removed")

        continue

        print("Please chose your option?")
        for dicRow in lstTable:
            print(dicRow["Code"] + ',' + dicRow["Student"] + ',' + dicRow["Course"] + ',')
        print('Please chose your option? ')
        continue

    elif(strChoice.strip() == '4'):
        print('Please chose your option? ')
        for dicRow in lstTable:
            print(dicRow["Code"] + ',' + dicRow["Student"] + ',' + dicRow["Course"] + ',')
        print('Please chose your option? ')
        if ("y" == str(input("Save data to file? (yes or no)- ")).strip().lower()):
            lstTable = open("Student.txt", "w")
            for dicRow in lstTable:
                lstTable.write(dicRow["Code"] + "," + dicRow["Student"] + "," + dicRow["Course"] + "\n")
            lstTable.close()
            input('Saved data to file! Press the [Enter] to key return to menu.')
        else:
            input('New data was NOT Saved, but previous data still exists! Press the[Enter] key to return to menu.')

        continue

    elif(strChoice.strip() == '5'):
        break