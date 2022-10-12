# Name: Trang Ngo
# Date: 09/28/2022
# File Purpose: Combine out the program

import weather
w_data = {}

while True:
    print('      *** TUFFY TITAN WEATHER LOGGER MAIN MENU \n\n')
    print("1. Set data filename")
    print("2. Add weather data") 
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program\n")
    menu_choice = int(input("Enter menu choice: "))
    print("\n")

    if (menu_choice == 1):
        newfile = input("Enter data file name: ")
        print('\n')
        w_data = weather.read_data(filename=newfile)
    elif (menu_choice == 2):
        date = input("Enter date (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        temperature = int(input("Enter temperature: "))
        humidity = int(input("Enter humidity: "))
        rainfall = float(input("Enter rainfall: "))
        w_data[date + time] = {"t": temperature, "h": humidity, "r": rainfall}
        weather.write_data(data = w_data, filename="w.dat")
    elif (menu_choice == 3):
        date = input("Enter date (YYYYMMDD): ")
        print("\n")
        print(weather.report_daily(data=w_data, date=date))
    elif (menu_choice == 4):
        print("\n")
        print(weather.report_daily(data=w_data, date=date))
    elif (menu_choice == 9):
        break
    else:
        print("Invalid Choice.")