from multiprocessing import Pool
import time
import os

def f(x):
    # return x
    return sum(list(range(100000)))

if __name__ == '__main__':
    t0 = time.time()
    n = 5000
    with Pool(os.cpu_count()) as p:
        y = p.map(f, range(n))
    t1 = time.time()
    total_time = t1-t0
    print(f"Time taken: {total_time} seconds. Avg: {total_time/n}")