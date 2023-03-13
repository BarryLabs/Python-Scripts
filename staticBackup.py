import os
import datetime
import zipfile
import shutil

# Get one or more files to backup.
bFiles = []
f1 = input("Please enter the first directory to backup: \n")
bFiles.append(f1)
while True:
    answer = input("Would you like to backup another directory? (y/n): \n")
    if answer == "y":
        fC = input("Please enter the directory: \n")
        bFiles.append(fC)
    else:
        break

# Get one or more destinations to backup to.
dLoc = []
d1 = input("Enter a desired folder to backup to: \n")
dLoc.append(d1)
while True:
    answer = input("Would you like to backup to another directory? (y/n): \n")
    if answer == "y":
        dL = input("Please enter the directory: \n")
        bFiles.append(dL)
    else:
        break

# Check If Backup Location Exists.
for locCheck in dLoc:
    lC = str(locCheck)
    if os.path.exists(lC):

# Backup Files
        for file in bFiles:
            sfile = str(file)
            try:
                cC = shutil.copy2(sfile, lC)
                if os.path.exists(os.path.join(lC, sfile)):
                    os.chdir(lC)
                    fZip = zipfile.ZipFile('archive.zip', 'w', compression=zipfile.ZIP_LZMA)
                    for file in os.listdir(lC):
                        if file != 'archive.zip':
                            fZip.write(file)
                    fZip.close()

# Remove Unnecessary Files
                    for file in os.listdir(lC):
                        if file != 'archive.zip' and file != 'bLog.txt':
                            os.remove(file)

# Log The Backup
                    os.chdir(lC)
                    bLog = open("bLog.txt", "w")
                    bLog.write(str(datetime.datetime.now()))
                    bLog.close()
# Handling
            except shutil.SameFileError:
                i = 0
                filename = os.path.basename(lC)
                while os.path.exists(os.path.join(lC, f'{filename}_{i}')):
                    i += 1
                cFolder = shutil.copy2(bFiles, os.path.join(lC, f'{filename}_{i}'))
            except PermissionError:
                print("Permissions Denied. Please run as administrator.\n")
