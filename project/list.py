# List all the files in the list of folder that user provides
'''
algorithm for the program
1. read input from the user
2. loop through the folder use for loop  --> list files
3. identify the module
4. print files
5. handle any known error
'''

import os

folders = input("enter the name of folder and add space in between: ").split()

for folder in folders:
    file = os.listdir(folder)
    print('please ')
    for f in file:
        print(f)




