import math
import time
import concurrent.futures

def calculate(start,end):
    result = 0
    for i in range(start,end):
        result += math.sqrt(i) + i**2
    return result



if __name__ == "__main__":
    Num = 10000000
    chunk_size = Num // 4

    tasks = [(i ,i + chunk_size) for i in range(1,Num,chunk_size)]


    #单线程
    print("开始测试【单线程】...")
    start_time = time.perf_counter()
    for start, end in tasks:
        calculate(start, end)
    end_time = time.perf_counter()
    print(f"单线程耗时: {end_time - start_time:.4f} 秒\n")
    #多线程
    print("开始测试【多线程】...")
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(calculate, start, end) for start, end in tasks]
        # 等待所有任务执行完毕
        concurrent.futures.wait(futures)
    end_time = time.perf_counter()
    print(f"多线程耗时: {end_time - start_time:.4f} 秒\n")
    #多进程
    print("开始测试【多进程】...")
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(calculate, start, end) for start, end in tasks]
        concurrent.futures.wait(futures)
    end_time = time.perf_counter()
    print(f"多进程耗时: {end_time - start_time:.4f} 秒\n")