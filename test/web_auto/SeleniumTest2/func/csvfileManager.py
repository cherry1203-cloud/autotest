import csv

path=r"D:\learngit\web_auto\SeleniumTest2\test_data\register_testcases.csv"
print (path)
file=open(path)
data=csv.reader(file)
for row in data:
    print(row)