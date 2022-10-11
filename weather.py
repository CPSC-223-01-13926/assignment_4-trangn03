# Name: Trang Ngo
# Date: 09/28/2022
# File Purpose: Create weather module

import json
import calendar

def read_data(filename):
    try: 
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
            return {}

def write_data(data,filename):
    with open(filename, 'w') as file:
        json.dump(data,file)
    
def max_temperature(data,date):
    x = -999
    for key in data:
        if date == key[0:8]: # first eight number
            if data[key]['t'] > x: 
                x = data[key]['t']
    return x

def min_temperature(data,date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]['t'] < x: 
                x = data[key]['t']
    return x 

def max_humidity(data,date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] > x:
                x = data[key]['h']
    return x

def min_humidity(data,date):
    x = 99999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] < x:
                x = data[key]['h']
    return x

def tot_rain(data,date):
    rain = 0
    for key in data:
        if date == key[0:8]:
            rain += data[key]['r']
    return rain

def report_daily(data, date):
    display = '========================= DAILY REPORT ========================\n'
    display += 'Date                      Time  Temperature  Humidity  Rainfall\n'
    display += '====================  ========  ===========  ========  ========\n'

    for key in data:
        if date == key[0:8]:
            mdy = calendar.month_name[int(date[4:6])]+ ' ' + str(int(date[6:8])) + ', ' + str(int(date[0:4]))
            tm = key[8:10] + ':' + key[10:12] + ':' + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            display = display + f'{mdy:22}{tm:10}{t:11}{h:10}{r:10.2f}\n'
    
    return display

def report_historical(data):
    display =  '============================== HISTORICAL REPORT ===========================\n'
    display += '                          Minimum      Maximum   Minumum   Maximum     Total\n'
    display += 'Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n'
    display += '====================  ===========  ===========  ========  ========  ========\n'
    temp = None
    for key in data:
        date = key[0:8]
        if temp == date: 
            continue
        mdy = calendar.month_name[int(date[4:6])]+ ' '+ str(int(date[6:8]))+ ', '+ str(int(date[0:4]))
        min_temp = min_temperature(data, date)
        max_temp = max_temperature(data, date)
        min_hum = min_humidity(data, date)
        max_hum = max_humidity(data, date)
        rain = tot_rain(data, date)
        display += f'{mdy:20}{min_temp:13}{max_temp:13}{min_hum:10}{max_hum:10}{rain:10.2f}\n'
        temp = date
    return display