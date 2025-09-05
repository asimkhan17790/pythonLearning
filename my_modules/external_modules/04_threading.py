# inbuilt module for threading
import threading
# Another module used for multi threading and run multiple processes parallely
import multiprocessing
import time


def worker(num, prefix):

    print(f"Thread {num} {prefix}: Starting")
    time.sleep(3)  # Simulating some time consuming task
    print(f"Thread {num}: Finishing")


threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i, 'Test'))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads completed...")
