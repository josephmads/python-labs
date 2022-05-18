# Write the file counts to a `.csv` file.

import csv

counts = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts.csv", "a") as csvfile:
    countswriter = csv.writer(csvfile)
    data = [counts[''], counts['.csv'], counts['.md'], counts[".png"]]
    countswriter.writerow(data) 