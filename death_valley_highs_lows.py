import csv

from datetime import datetime


import matplotlib.pyplot as plt

fname = 'Data Visualization\data\death_valley_2018_simple.csv'

with open(fname) as f: # Opens the file and assigns it to the object f
    reader = csv.reader(f) # Contents of the file are read through the reader method and assigned as an object to the variable reader. We will access the contents through this object
    header_row = next(reader) # next method reads the content of the first line of the file and we store it in header row and print it in the next line
    # print(header_row) # Displays the header data to understand how the data is structured
   
# for index,column_header in enumerate(header_row): # enumerate() function returns both the index of each item and the value of each item as you loop through a list
#     print(index,column_header)

    dates,highs,lows =[],[],[]

    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:

            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data on {current_date}")
        else:

            highs.append(high)
            dates.append(current_date)
            lows.append(low)
        # print(row) # Prints all the data in the CSV

    

# Plot high temperatures

    plt.style.use('seaborn')

    fig,ax = plt.subplots() 
    ax.plot(dates,highs, c = 'red',alpha=.5) 
    ax.plot(dates,lows, c='blue',alpha=.5)
    ax.fill_between(dates,highs,lows,facecolor='blue',alpha=.1)# alpha is used to show color transparency. alpha=0 means completely transparent and 1 means fully opaque
    # Set chart title and label axes
    ax.set_title("Daily High and Low Temperatures- 2018", fontsize=24) 
    ax.set_xlabel('', fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperatures(F)", fontsize=16)
    #set size of tick labels
    ax.tick_params(axis='both', which='major',labelsize=16)

    plt.show()
