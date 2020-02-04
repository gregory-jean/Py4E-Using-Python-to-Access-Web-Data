'''
Assignment 2.1

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
Data Files

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

    Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
    Actual data: http://py4e-data.dr-chuck.net/regex_sum_308887.txt (There are 96 values and the sum ends with 617)


'''
import re
numList = list()

# Open file name given
fname = input('Enter a file name: ')

try :
    fhand = open(fname)
except :
    print('File \'', fname, '\' does not exist.')
    quit()

# Extract numbers from text
for line in fhand :
    line = line.rstrip()
    
    # Find all numbers within the text
    numbers = re.findall('([0-9]+)', line)

    # Add all found numbers to list
    for number in numbers :
        number = float(number)
        numList.append(number)

# Display total of numbers
print(sum(numList))