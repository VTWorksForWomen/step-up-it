######
# Description: Parse a VWW Tech Resource CSV for completeness and format
# Author: Allison Miller
# Date: 2015/03/08
######

import csv

# Get file to validate
vwwCsv = input("Please enter the CSV file: ")
vwwOutput = input("Please enter the out file: ")

# Validation rules
requiredCols = ['Name','URL','Phone','Description','Category']
maxLengths = {'Name': 100,'Description':255}
errors = {'missing':{},'length':{}}
entryCounts = {'total':0,'correct':0}

with open(vwwCsv, 'r') as file:
    # Read contents of CSV with first row as keys
    rows = csv.DictReader(file, delimiter=',')
    rowNumber = 0

    # Validate cells
    for row in rows:
        # Count entries
        entryCounts['total'] += 1
        correctEntry = True
        
        # Increment row number
        rowNumber += 1

        # Check required cells
        for col in requiredCols:
            # Ignore whitespace!
            cellVal = row[col].strip()
            
            if not cellVal:
                if not errors['missing'].get(rowNumber):
                    errors['missing'][rowNumber] = []
                errors['missing'][rowNumber].append(col)
                
                # Mark entry as failed
                correctEntry = False

        # Check cell max lengths
        for key in maxLengths:
            # Ignore whitespace!
            cellVal = row[key].strip()

            if len(cellVal) > maxLengths[key]:
                if not errors['length'].get(rowNumber):
                    errors['length'][rowNumber] = []
                errors['length'][rowNumber].append(key)
                
                # Mark entry as failed
                correctEntry = False

        if correctEntry:
            entryCounts['correct'] += 1
            
# Write out which required cells are missing data
with open(vwwOutput, 'w') as file:
    if errors['missing']:
        file.write("Missing data:\n")
        for key in errors['missing']:
            rowString = str(key) + ": " + ' '.join(errors['missing'][key]) + "\n"
            file.write(rowString)
        
    # Write out which cells have exceeded max length
    if errors['length']:
        file.write("Length exceeded:\n")
        for key in errors['length']:
            rowString = str(key) + ": " + ' '.join(errors['length'][key]) + "\n"
            file.write(rowString)

    # Write out entry counts
    file.write("Total entries: " + str(entryCounts['total']) + "\n")
    file.write("Correct entries: " + str(entryCounts['correct']) + "\n")
