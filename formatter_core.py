# Importing BeautifulSoup class from the bs4 module 
import os
import sys
from colorama import init, Fore
init(autoreset=True)

from bs4 import BeautifulSoup

sm_column_pad = 20
med_column_pad = 50
lg_column_pad = 100

#function to change the default column pad values
def set_column_pad_values(sm,med,lg):
    global sm_column_pad, med_column_pad, lg_column_pad
    sm_column_pad = sm
    med_column_pad = med
    lg_column_pad = lg
#end function

#calculates and pads to the end of value, a number of empty spaces
def pad_column_width(value):
    l = len(value)
    if l < sm_column_pad:
        l = sm_column_pad 
    elif l < med_column_pad:
        l = med_column_pad 
    else:
        l = lg_column_pad 

    #ljust function did not work after replacing the space with underscore,
    #have not understood why just yet
    #val_space = val.ljust(l,'-')
    #work around to ljust failures
    padded_value = value.ljust(l,'_')
    return padded_value
#end function

#parses and formats one line of data, the first one, as it represents the table header
def format_table_header(line_input):
    row = ""
    val = ""
    i = 0
    while i < len(line_input):
        c = line_input[i]
        if c != ',':
            #special column header formatting to replace all spaces between words with an underscore
            if c == ' ':
                c = '_'
            val += c                
        else:
            row += pad_column_width(val)
            val= ""
        i = i+1
    #end loop
    if val:
        row += pad_column_width(val)
    return row
#end function



#parses and formats one line of input and returns one table row
def format_table_row(line_input):
    row = ""
    i = 0
    val = ""
    while i < len(line_input):
        c = line_input[i]
        if c != ',':
            val += c                
        else:
            row += pad_column_width(val)
            val= ""
        i = i+1
    #end loop
    if val:
        row += pad_column_width(val)
    return row
#end function

def write_table_line(f,input):
        f.write(input + '\n')
#end function

#this function will write the input file to the formatted file
def output_formatted_file(dataset_text, output_filename="customers_100.txt"):
    # """
    # Writes the formatted dataset to a text file.

    # Parameters:
    #     dataset_text (iterable): An iterable of strings, each representing a line from the dataset (e.g., file object or list of lines).
    #     output_filename (str): The name of the output file to write the formatted table to. Defaults to "customers_100.txt".

    # The first line of dataset_text is treated as the table header and formatted accordingly.
    # """
    is_table_header = True #flag used to format table header

    with open(output_filename, "w", encoding="utf-8") as f:
        for ln in dataset_text:
            #strip function removes whitespace from the beginning and end of the line, this is important to remove the newline character at the end of each line
            ln = ln.strip()
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
#end function

#TODO:build out this function so it is highly testable
#this will write the input file as a table to the html file 
def output_html_file(dataset_text, output_html=None):
    """
    Write the CSV dataset as a simple HTML table.

    Parameters:
        dataset_text (iterable): Lines of CSV data
        output_html (str, optional): Path to write HTML file. Defaults to dataset_text name with .html
    """
  

    if output_html is None:
        # fallback default
        output_html = "output.html"

    try:
        # Start HTML structure
        html_content = "<html><head><meta charset='utf-8'><title>CSV Table</title></head><body>"
        html_content += "<table border='1' style='border-collapse:collapse;'>"

        first_row = True
        for line in dataset_text:
            line = line.strip()
            cells = line.split(",")

            if first_row:
                html_content += "<thead><tr>"
                for cell in cells:
                    html_content += f"<th>{cell}</th>"
                html_content += "</tr></thead><tbody>"
                first_row = False
            else:
                html_content += "<tr>"
                for cell in cells:
                    html_content += f"<td>{cell}</td>"
                html_content += "</tr>"

        html_content += "</tbody></table></body></html>"

        # Write to file
        
        soup = BeautifulSoup(html_content, "html.parser")
        pretty_html = soup.prettify()

        with open(output_html, "w", encoding="utf-8") as f:
         f.write(pretty_html)

        print(Fore.GREEN + f"HTML file written to {output_html}")

    except Exception as e:
       print(Fore.RED + f"Error writing HTML file: {e}")
    return output_html



#ask user to choose output to file or html
def choose_output():
    try:
        choice = int(input(Fore.CYAN + "choose output, enter 1 for file, enter 2 for html page: "))
        return choice
    except:
        print(Fore.RED + f"Invalid input. Please choose again.")
    #end try
#end function

#the entry point for the application

def main():
    # Check if user provided an input file
    if len(sys.argv) < 2:
        print(Fore.CYAN + f"Usage: formatcsv <input_csv_file>")
        sys.exit(1)

    input_path = sys.argv[1]  # get input file from command line

    # Optional: default output filename
    output_file = input_path.rsplit('.', 1)[0] + "_formatted.txt"

    try:
        # Open the CSV file
        with open(input_path, "r") as input_file:
            # Ask the user how they want the output
            choice = choose_output()

            if choice == 1:
                # Output to text file
                output_formatted_file(input_file, output_filename=output_file)
                print(Fore.GREEN + f"Formatted file saved as {output_file}")
            elif choice == 2:
                # Output to HTML
                output_html_file(input_file)
                print(Fore.GREEN + "Formatted HTML output completed")
            else:
                print(Fore.RED +"Invalid choice, exiting.")

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + f"Input file not found: {input_path}")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
