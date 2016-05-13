import main_met_data.py

"""
Run the function extract_data as in the following examples.
This will extract data for the given parameters (Don't include Time as a parameter.)
It will start at start_time, go up to stop_time, in increments of interval. Each a tuple of (month,day,hour,minutes).
If print_output=True, prints the extracted data.
If output_file="Blah.csv", saves extracted data in csv format to the file "Blah.csv". If output_file=None, doesn't.
"""

extract_data(parameters=["WS","WD","TW","TI","AT","BP","BC","BS","ST","LA","LO",], start_time=(8,11,18,0), stop_time=(8,13,23,30), interval=(0,0,1,23), print_output=True, output_file=None)#warm up. Doesn't save to file. Just prints it. Only studies from Aug-11-6pm to Aug-13-11:30pm, in increments of 1hr23min.


extract_data(parameters=["WS","WD","TW","TI","AT","BP","BC","BS","ST","LA","LO",], start_time=(8,11,18,0), stop_time=(10,11,23,30), interval=(0,0,1,23), print_output=True, output_file="first_try.csv")#more involved. Doesn't print, but saves to file "first_try.csv" (rewrites it, if it already existed). Starts at Aug-11-6pm, goes up to Oct-11-11:30pm, in increments of 1hr 23min.


#Just comment out the above example extract_data functions, and write your own.
