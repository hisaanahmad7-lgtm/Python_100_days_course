import time

print(time.time())
print(time.localtime())
time.sleep(2)
print("I Execute after 2 sec..")


print(time.ctime())
t = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))

start = time.perf_counter()
for i in range(100000):
    print(f"The time is {i}")
    i = i+1
end = time.perf_counter()
print(end - start)


starttime = time.perf_counter()
c = 0
while c <= 100000:
    print(f"The time is {c}") 
    c = c+1
endtime = time.perf_counter()
print(end - start)
print(endtime - starttime)