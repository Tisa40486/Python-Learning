import os

FileName = input("enter your file name: ")

# Vérifier que le fichier existe vraiment
def checkFile(fileName: str): 
    if os.path.exists(fileName):
        print("✓ File found")
    else:
        print("✗ FIle NOT found")
        print("Files in the Folder :", os.listdir())
        
checkFile(FileName)
        