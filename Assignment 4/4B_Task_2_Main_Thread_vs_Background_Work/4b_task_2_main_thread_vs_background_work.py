from concurrent.futures import ThreadPoolExecutor
import time

def work(n):
 total=0
 for i in range(1,n): total+=(i*i)%997
 return total
N=500000
print("4B TASK 2 - MAIN THREAD VS BACKGROUND")
t=time.perf_counter(); a=work(N); main=time.perf_counter()-t
t=time.perf_counter()
with ThreadPoolExecutor(max_workers=1) as pool: b=pool.submit(work,N).result()
worker=time.perf_counter()-t
print("Iterations:",N)
print(f"Main execution: {main:.4f}s")
print(f"Worker incl. dispatch: {worker:.4f}s")
print("Same result:",a==b)
print("Worker execution protects the Android UI thread; these are host timings, not Android measurements.")
print("Tiny tasks may be slower in a worker due to scheduling overhead; use bounded workers/batching.")
