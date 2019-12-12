import csv
import os


def reader(filename):
    # path="../test_data/"+filename
    base_path=os.path.dirname(__file__)
    path=base_path.replace("func","test_data/"+filename)

    # file=open(path)
    # data=csv.reader(file)
    # return data
    list=[]
    with open(path) as file:
        data=csv.reader(file)
        i=0
        for row in data:
            if i==0:
                pass
            else:
                list.append(row)
            i=i+1
        return list
if __name__ == '__main__':
    print(reader("register_testcases.csv"))




