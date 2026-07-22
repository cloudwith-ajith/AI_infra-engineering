#pymongo is the libary used to connect the mongobd using the python 

import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1/27017')
mydb = client['student']

student_info = mydb.student_info

#used to insert  one value
student_info.insert_one(record)

#used to insert many values, should define in the list 

student_info.insert_many(record)

#it returns the first element
student_info.find_one()

#it returns all the element in the mong db
for i  in student_info.find({}):
    print(i)

