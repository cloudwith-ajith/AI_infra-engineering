#pymongo is the libary used to connect the mongobd using the python 

import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1/27017')
mydb = client['student']

student_info = mydb.student_info

student_info.find_one()
