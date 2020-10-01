import csv
from datetime import datetime

open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file)

highs = []
dates = [] 
lows = [] 

for row in csv_file:
    try:
        high = int(row[4]) 
        low = int(row[5]) 
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError: 
        print(f"Missing data for {current_date}")
    else:   
        highs.append(high)
        lows.append(low)
        dates.append(current_date)



x = datetime.strptime('2018-07-01', '%Y-%m-%d')

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows,c="blue", alpha=0.5)

plt.title("Daily high and low temperatures - 2018\n Death Valley", fontsize=16)
plt.xlabel("", fontsize=12) 

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both",labelsize=12)

plt.show()