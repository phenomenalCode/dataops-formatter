# Importing BeautifulSoup class from the bs4 module 
import requests
from bs4 import BeautifulSoup

sm_column_pad = 20
med_column_pad = 50
lg_column_pad = 100

#function to change the default column pad values
def set_column_pad_values(sm,med,lg):
    sm_column_pad = sm
    med_column_pad = med
    lg_column_pad = lg
#end function

#calculates and pads to the end of value, a number of empty spaces
def pad_column_width(value):
    l = len(value)
    if l < sm_column_pad:
        l = sm_column_pad - l
    elif l < med_column_pad:
        l = med_column_pad - l
    else:
        l = lg_column_pad - l

    #ljust function did not work after replacing the space with underscore,
    #have not understood why just yet
    #val_space = val.ljust(l,'-')
    #work around to ljust failures
    padded_value = value + " " * l
    return padded_value
#end function

#parses and formats one line of data, the first one, as it represents the table header
def format_table_header(line_input):
    row = ""
    val = ""
    while i < len(line_input):
        c = line_input[i]
        if c != ',':
            #special column header formatting to replace all spaces between words with an underscore
            if ch_input == ' ':
                ch_input = '_'
            val += c                
        else:
            row += pad_column_width(val)
            val= ""
        i = i+1
    #end loop
    return row
#end function



#parses and formats one line of input and returns one table row
def format_table_row(line_input):
    row = ""
    while i < len(line_input):
        c = line_input[i]
        if c != ',':
            val += c                
        else:
            row += pad_column_width(val)
            val= ""
        i = i+1
    #end loop
    return row
#end function

def write_table_line(f,input):
        f.write(input + '\n')
#end function

#this function will write the input file to the formatted file
def output_formatted_file(dataset_text):
    f = open("customers_100.txt", "w")
    is_table_header = True #flag used to format table header

    for ln in dataset_text:
        formatted_line = ""
        if is_table_header:
            #passes the first line from dataset as containing the table column headers
            formatted_line = format_table_header(ln)
            write_table_line(f,formatted_line)
            is_table_header = False
        else:
            formatted_line = format_table_row(ln)
            write_table_line(f,formatted_line)
        #end if
    #end for loop
    f.close()
#end function

#TODO:build out this function so it is highly testable
#this will write the input file as a table to the html file 
def output_html_file(dataset_text):
    try:
        #os.sep uses the correct path separator for the os that the app is currently running upon
        #..\dist\index.html -for windows
        #../dist/index.html -for mac os and linux
        html_file = open(".. + os.sep + dist + os.sep + index.html", "w")
        #if file successfully opened
        if html_file:
            #example code from: https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/
            # Opening the html file 
            #html_file = open("index.html", "w") 
            # Reading the file 
            index = html_file.read() 
            # Creating a BeautifulSoup object and specifying the parser 
            S = BeautifulSoup(index, 'lxml') 
            # Using the select-one method to find the thead tag write 
            thead = S.select_one("//div[@id='data_table']/table/thead")

            # Using the select-one method to find the tbody tag write 
            tbody = S.select_one("//div[@id='data_table']/table/tbody")
            #close html file
            html_file.close()
    except:
        print("error opening html file")
#end input_f_output_html_file

#ask user to choose output to file or html
def choose_output():
    try:
        choice = int(input("choose output, enter 1 for file, enter 2 for html page: "))
        return choice
    except:
        print(f"{choice} is an invalid input please choose again.")
    #end try
#end function

#the entry point for the application
def main():
    #open the dataset file
    input_file = open("customers-100.csv", "r")
    if input_file:
        #get the users choice to write to file or html page
        choice = choose_output()
        if choice == 1:
            #output to file
            output_formatted_file(input_file)
        elif choice == 2:
            #output to html
            output_html_file(input_file)
        else:
            pass
        #end if 
    #end if
    if input_file:
        #close input file
        input_file.close()
    #end if
#end function

#start application
main()

