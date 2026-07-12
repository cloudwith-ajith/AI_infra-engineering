# parallel procees in thread

import time
from concurrent.futures import ThreadPoolExecutor 
start = time.time()
def num(n):
    return n
    
# Fixed max_workers and matched the import name
with ThreadPoolExecutor(max_workers=None) as Executer:
    for x in Executer.map(num, range(10)):
        print(x)

print(time.time()-start)
----------------------------------SHA256-------------hash algorithm
import hashlib

key = "Ajith got 1000million in blockchain"

info = hashlib.sha256(key.encode())

print(info.hexdigest())

