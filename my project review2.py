import os
import shutil
import docx
import time
information = input("What are you looking for")
seconds_in_day = 86400
new_time = int(input("Put your time in days")) * seconds_in_day
copy = input("Where to put the file")


def look_for():
    for adress, dirs, files in os.walk(input("Put the start")):
        for file in files:
            full_path = os.path.join(adress, file)
            if ".docx" in full_path and "$" not in full_path and time.time() - os.path.getctime(full_path) < new_time:
                yield full_path


def checking_files(our_file):
    doc = docx.Document(our_file)
    for paragraph in doc.paragraphs:
        text_file = paragraph.text
        if information in text_file:
            return copying_files(our_file)


def copying_files(our_file):
    last_index = -1
    name_file = our_file.split("\\")[last_index]
    shutil.copyfile(our_file, os.path.join(copy, name_file))
    print("File is copied", name_file)


for path in look_for():

    try:
        checking_files(path)
    except Exception as errors:
        with open("mistakes12.txt", "a") as file_errors:
            file_errors.write(str(errors) + "\n" + path + "\n")
