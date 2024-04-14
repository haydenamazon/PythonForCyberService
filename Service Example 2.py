#Filebomb

import os
import shutil
#import time

x = 0
for i in range (0, 60):
    x = x + 1
    f = open("file" + str(x) + "spam.txt", "w")
    f.write(str(x))
    f.close()
    filename = "file" + str(x) + "spam.txt"
    os.startfile("file" + str(x) + "spam.txt")
    

def move_spam_files_to_futurebin():
    source_folder = os.getcwd()  # Current working directory
    futurebin_folder = os.path.join(source_folder, "futurebin")

    if not os.path.exists(futurebin_folder):
        os.makedirs(futurebin_folder)

    files = os.listdir(source_folder)

    for file in files:
        if file.endswith("spam.txt"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(futurebin_folder, file)
            shutil.move(source_path, destination_path)
'''
if __name__ == "__main__":
    move_spam_files_to_futurebin()
'''
