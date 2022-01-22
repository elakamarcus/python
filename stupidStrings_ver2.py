#!/usr/bin/python

import sys
import csv
import datetime

def shortType(str):
    """
    The function splits the string delimited by -, _ or blank space, and returns
    the first and second value. This should be sufficient to create an overview in pivot table.
    """
    if str.find("-") > 0:
        newstr = str.split("-")
        return newstr[0]+"-"+newstr[1]
    elif str.find("_") > 0:
        newstr = str.split("_")
        return newstr[0]+"-"+newstr[1]
    elif str.find(" ") > 0:
        newstr = str.split(" ")
        return newstr[0]+"-"+newstr[1]
    else:
        return str

def test():
    print("You encountered some error, so here a sample:")
    string="some-string-here"
    string2="another_string_here"
    string3="string with another separator"
    print(f'{string}:-> {shortType(string)}')
    print(f'{string2}:-> {shortType(string2)}')
    print(f'{string3}:-> {shortType(string3)}')

# Extracted the function for modular support
def readWriteCSV(inFile, outFile):
    """
    TODO: push the read into a dictionary, and then print the dictionary.
    That would be a much nicer implementation...
    """
    fopen = open(outFile, 'w')
    outWrite = csv.writer(fopen)

    try: 
        with open(inFile.strip()) as in_file:
            readCSV = csv.reader(in_file)
            cnt = 0
            for row in readCSV:
                if cnt == 0:
                    #print(f'{", ".join(row).strip()}')
                    cnt += 1
                    outWrite.writerow([row[0], row[1], row[2]])
                else:
                    #print(f'{row[0], row[1], shortType(row[2])})
                    outWrite.writerow([row[0], row[1], shortType(row[2])])
                    cnt += 1

            # clean up...
        fopen.close()  
        print(f'worked on {cnt} rows in {in_file.name}')
        print(f'See output in {outFile}')
        
    except:
        print(f'Error opening file. Did you put the right name?\n{sys.argv[1]}')


def main():
    now = datetime.datetime.now()
    filename = f'{now.strftime("%Y%m%d")}.new.csv'
    readWriteCSV(sys.argv[1], filename) if len(sys.argv) > 1 else test()
    
"""
This space intentionally left blank, potentially the script won't run without this
blank space in the middle. You may try, but at your own risk.

Enjoy.
"""

if __name__ == '__main__':
    main()