import csv
import os
path=os.getcwd()
file_path=os.path.abspath(os.path.dirname(path)+os.path.sep+"..")+"\\testdatafile\ind_interface\\test_updateuser.csv"
print(file_path)
file=open(file_path,"r")
table=csv.reader(file)
for row in table:
    print(row)