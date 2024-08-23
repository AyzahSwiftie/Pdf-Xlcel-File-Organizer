# A code to move PDF and Excel files from one folder to another

import os
import shutil

from_folder = "C:/Users/rabiy/Downloads"
to_folder = "C:/Users/rabiy/Downloads/DownloadedPdfExelFiles"
list_of_files = os.listdir(from_folder)
PdfXl_extensions = ['.pdf', '.xlsx']

for file_name in list_of_files:
    root, ext = os.path.splitext(file_name)
    if ext == '':
        continue
    if ext in PdfXl_extensions:  # Checks to see if the file has the extensions from the list
        source_dir = os.path.join(from_folder, file_name)
        if os.path.exists(to_folder):  # Check to see if the folder exists
            destination_dir = os.path.join(to_folder, file_name)
            print("Moving.... " + file_name + " to PDF and Excel folder........")
            shutil.move(source_dir, destination_dir)
        else:  # If the folder doesn’t exist, make one
            new_folder = os.path.join(from_folder, "DownloadedPdfExelFiles")
            os.makedirs(new_folder)
            print("Moving.... " + file_name + " to PDF and Excel folder........")
            shutil.move(source_dir, os.path.join(new_folder, file_name))  # Move it to the new path
