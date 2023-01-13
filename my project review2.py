import os,shutil,docx,time
information = input("What are you looking for")
old_time = int(input("Put your time in days")) 
new_time = old_time * 86400

copy = input("Where to put the file")

def look_for():
    for adress,dirs,files in os.walk(input("Put the start")):
        for file in files:
            full_path = os.path.join(adress,file)
            if ".docx" in full_path and "$" not in full_path and time.time() - os.path.getctime(full_path ) < new_time:
                yield full_path
def checking_files(our_file) :
    doc = docx.Document(our_file)
    for paragraph in doc.paragraphs:
        text_file = paragraph.text
        if information in text_file:
            return copying_files(our_file)
def copying_files(our_file):
    name_file = our_file.split("\\") [-1] 

    shutil.copyfile(our_file,os.path.join(copy,name_file)) 
    print("File is copied",name_file)       
for i in look_for():
    
    
    try:
        checking_files(i) 
    except Exception as errors:
        with open("mistakes12.txt",'a') as r:
            r.write(str(errors) + '\n' + i + '\n')