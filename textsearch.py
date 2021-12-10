import sys
import os

allfiles = os.listdir('./')
try:
    entryQuestion = sys.argv[1]
except:
    entryQuestion = str(input("Enter a keyword: "))

for k in allfiles:
    if k.endswith('.txt'):
        with open(k,'r') as file:
            key = file.readlines()
            for r in key:
                if entryQuestion in r:
                    print("\n[+] in file : {} ".format(k),"found line :\n",r)
                else:
                    pass
    else:
        pass