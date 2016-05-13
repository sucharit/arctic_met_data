
calendar=dict()#number of days in calendar months.
calendar[8]=31
calendar[9]=30
calendar[10]=31

def extract_data(parameters, start_time, stop_time, interval, print_output, output_file):
    """
    This will extract data for the given parameters (Don't include Time as a parameter.)
    It will start at start_time, go up to stop_time, in increments of interval. Each a tuple of (month,day,hour,minutes).
    If print_output=True, prints the extracted data.
    If output_file="Blah.csv", saves extracted data in csv format to the file "Blah.csv". If output_file=None, doesn't.
    """

    if "Time" in parameters:
        del parameters[parameters.index("Time")]#We will record time separately.

    outp="Month,Day,Hour,Min,"+",".join(parameters)#This is the output to be printed to screen or written to file.

    file_list=[]#This is a list of files to be opened by the program
    time_list=[]#This is a double list, so that time_list[i] is a list of times to be studied from the i-th file.

    #Now we will generate file_list and time_list
    (mm,dd,hr,mi)=start_time#This is the current time being studied by the program
    while (mm,dd,hr,mi)<=stop_time:
        file_name="15"+'{0:02}'.format(mm)+'{0:02}'.format(dd)+".MET"
        
        if file_list==[] or file_name!=file_list[-1]:
            file_list.append(file_name)
            time_list.append([])
        time_list[-1].append((mm,dd,hr,mi))
    
        mi+=interval[3]
        hr+=int(mi/60)
        mi=mi%60

        hr+=interval[2]
        dd+=int(hr/24)
        hr=hr%24

        dd+=interval[1]
        while dd>calendar[mm]:
            dd-=calendar[mm]
            mm+=1

        mm+=interval[0]


    for ind_file,file_name in enumerate(file_list):
        ff=open(file_name,"r")

        count=0#record which line of the file are we reading
        ind_time=0#record which time instance of time_list[ind_file] is under consideration.
        for lin in ff.readlines():
            count+=1

            stuff=lin.split()
            if count==4:
                if stuff[0]!="#Time":
                    raise Exception("oops")#We better have the header line here, with time as first parameter.
                parameter_indices=[stuff.index(foo) for foo in parameters]#what are the indices of the parameters
                
            if count>4:

                (file_hr,file_mi)=(int(stuff[0][:2]),int(stuff[0][2:4]))
                while ind_time<len(time_list[ind_file]) and time_list[ind_file][ind_time][2:]<=(file_hr,file_mi):
                        outp+="\n"+",".join([repr(foo) for foo in time_list[ind_file][ind_time]])+","+",".join([stuff[ind] for ind in parameter_indices])
                        if time_list[ind_file][ind_time][2:]<(file_hr,file_mi):
                            outp+=",(wrote data for "+"-".join([repr(foo) for foo in time_list[ind_file][ind_time][:2]+(file_hr,file_mi)])+" instead)"
                        ind_time+=1

        while ind_time<len(time_list[ind_file]):#didn't find all time instances.
            outp+="\n"+",".join([repr(foo) for foo in time_list[ind_file][ind_time]])+","+",".join([stuff[ind] for ind in parameter_indices])
            outp+=",(wrote data for "+"-".join([repr(foo) for foo in time_list[ind_file][ind_time][:2]+(file_hr,file_mi)])+" instead)"
            ind_time+=1

        ff.close()

    if output_file!=None:
        writing=open(output_file,"w")
        writing.write(outp)
        writing.close()

    if print_output:
        print outp

