import time,statistics,gc

def primes(n):
 c=0
 for x in range(2,n):
  if all(x%d for d in range(2,int(x**0.5)+1)): c+=1
 return c

def allocations(n):
 a=[{"id":i,"value":str(i)} for i in range(n)]; return sum(len(x["value"]) for x in a)
print("4B TASK 3 - RUNTIME BENCHMARK")
for name,fn in [("CPU primes under 5000",lambda:primes(5000)),("Allocation 50000 objects",lambda:allocations(50000))]:
 samples=[]
 for _ in range(5): gc.collect(); t=time.perf_counter(); result=fn(); samples.append(time.perf_counter()-t)
 print(name,"result=",result,"median=",round(statistics.median(samples),4),"s","samples=",[round(x,4) for x in samples])
print("\nADB ART commands:")
for c in ["adb shell dumpsys package com.example.benchmark","adb shell cmd package compile -m speed-profile -f com.example.benchmark","adb shell cmd package get-compile-status com.example.benchmark","adb logcat | grep -i -E 'art|gc'","adb shell am force-stop com.example.benchmark"]: print(c)
print("Host benchmark only; it does not alter ART modes or measure Android GC.")
