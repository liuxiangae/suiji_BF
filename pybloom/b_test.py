from pybloom import BloomFilter
import  datetime
#读入文件
arr = []
with open('test.txt','r') as f:
    for i in range(0,999999):
        arr.append(f.readline())
f.close()

#申明Bf 载入数据
f = BloomFilter(capacity=999999, error_rate=0.001)

for x in arr:
    f.add(x)

look = []
for x in range(1,300000):
    look.append(arr[x])

time1 = datetime.datetime.now()
for k in look:
    k in f
time2 = datetime.datetime.now()
print("the time is :", (time2-time1).total_seconds(),'s')






