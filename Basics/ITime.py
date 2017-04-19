import time, datetime
ctime = datetime.datetime.now()
count = 10**5
nums=[]
for i in range(count):
    nums.append(i)
nums.reverse()
#     nums.insert(0,i)
ntime = datetime.datetime.now()
dtime = ntime - ctime
print(dtime)