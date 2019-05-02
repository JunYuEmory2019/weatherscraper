import json
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.axes.Axes.plot
matplotlib.pyplot.plot
matplotlib.axes.Axes.legend
matplotlib.pyplot.legend

print('What file would you like to open? Please include ".json" at the end.')
filename=input()

with open(filename,'r') as f:
    weatherjson = json.load(f)

    templistlow = []
    templisthigh = []
    days = []

    # Loop to split temps into highs and lows and identify chance of rain
    x = 0
    while x < len(weatherjson):
        dict = weatherjson[x]
        temp = dict["temp"]
        split = temp.split(' ')
        rain = dict["desc"]
        if x % 2 == 0:
            day = dict["day"]
            days.append(day)
        if split[0] == "High:":
            templisthigh.append(int(split[1]))
            x+= 1
        elif split[0] == "Low:":
            templistlow.append(int(split[1]))
            x+= 1
    if weatherjson[0]["day"] =="Tonight" :
        templisthigh.insert(0,None)

    # Output information for user
    print("Highs: ")
    print(templisthigh)
    print("Lows: ")
    print(templistlow)
    if rain == "Slight Chance" or "Showers" or "Chance":
        print('There is a chance of rain this week.')
    print("Opening graph of high and low temperatures...")
    time.sleep(2) # pause so user can see print statements before plot pops up

    # Data for plotting
    t = days[:4]
    s1 = templistlow[:4]
    s2 = templisthigh[:4]

    fig, ax = plt.subplots()
    ax.plot(t,s1,'b--',label='Low')
    ax.plot(t,s2,'r--',label='High')

    ax.set(xlabel='Days', ylabel='Temperature (F)',
           title='Weather Forecast')
    ax.grid()
    legend = ax.legend(loc='upper center', shadow=False, fontsize='small')
    legend.get_frame().set_facecolor('C9')

    filename = filename[:-5] # removes ".json" from file name
    fig.savefig(filename+".png") # saves figure as file name
    plt.show()
