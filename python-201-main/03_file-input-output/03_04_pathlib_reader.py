# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path
import csv

desktop = Path('/home/joe/Desktop')

text_folder = Path('/home/joe/Desktop/textfolder')
jpg_folder = Path('/home/joe/Desktop/jpgfolder')

file_dict = {'' : 0, 'txt' : 0, 'jpg' : 0}


for filepath in desktop.iterdir():

    if filepath.suffix == '':
        file_dict[''] += 1

    if filepath.suffix == '.txt':
        file_dict['txt'] += 1
        
        if file_dict['txt'] > 3:
            text_folder.mkdir(exist_ok=True)
            new_text_path = text_folder.joinpath(filepath.name)
            filepath.replace(new_text_path)


    elif filepath.suffix == '.jpg':
        file_dict['jpg'] += 1

        if file_dict['jpg'] > 3:
            jpg_folder.mkdir(exist_ok=True)
            new_jpg_path = jpg_folder.joinpath(filepath.name)
            filepath.replace(new_jpg_path)

with open(desktop.joinpath("filescount.csv"), "a") as csvfile:
    countswriter = csv.writer(csvfile)
    data = [file_dict[''], file_dict['txt'], file_dict['jpg']]
    countswriter.writerow(data)