# Use the `csv` module to read in and count the different file types.

import csv
from pathlib import Path

filescount = Path("/home/joe/Desktop/filescount.csv")

with open(filescount, "r") as csvfile:
    csv_reader = csv.DictReader(csvfile, fieldnames=["Folder", "TXT", "JPG"])
    counts = list(csv_reader)

print(counts)

