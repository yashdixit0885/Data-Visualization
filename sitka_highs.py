
import csv

fname = 'Data Visualization\data\sitka_weather_07-2018_simple.csv'

with open(fname) as f: # Opens the file and assigns it to the object f
    reader = csv.reader(f) # Contents of the file are read through the reader method and assigned as an object to the variable reader. We will access the contents through this object
    header_row = next(reader) # next method reads the content of the first line of the file and we store it in header row and print it in the next line
    # print(header_row) # Displays the header data to understand how the data is structured
   
# for index,column_header in enumerate(header_row): # enumerate() function returns both the index of each item and the value of each item as you loop through a list
    # print(index,column_header)

# Get high temperatures from this file

    highs =[]

    for row in reader:
        high = int(row[5])
        highs.append(high)
        # print(row) # Prints all the data in the CSV

    print(highs)