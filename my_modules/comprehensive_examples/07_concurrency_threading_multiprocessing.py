"""
Comprehensive Concurrency: Threading vs Multiprocessing Tutorial
================================================================

This module demonstrates the differences between threading and multiprocessing in Python:
- Threading: I/O-bound tasks, shared memory, GIL limitations
- Multiprocessing: CPU-bound tasks, separate memory, true parallelism
- Concurrent.futures: High-level interface for both
- Async programming vs threading comparison
- Performance analysis and best practices
"""

import threading
import multiprocessing
import time
import os
import sys
import queue
import concurrent.futures
import asyncio
from typing import List, Any, Callable, Optional
from dataclasses import dataclass
from datetime import datetime
import requests
import json
import math


# ============================================================================
# THREADING EXAMPLES
# ============================================================================

class ThreadExample:
    """Comprehensive threading examples"""

    def __init__(self):
        self.shared_data = 0
        self.lock = threading.Lock()
        self.results = []

    def basic_threading_example(self):
        """Basic threading with multiple workers"""
        print("=" * 60)
        print("BASIC THREADING EXAMPLE")
        print("=" * 60)

        def worker(thread_id: int, delay: float):
            """Worker function that simulates I/O-bound task"""
            print(f"Thread {thread_id}: Starting work")
            time.sleep(delay)  # Simulate I/O operation
            print(f"Thread {thread_id}: Completed work after {delay}s")
            return f"Result from thread {thread_id}"

        print("\\n1. Creating and starting threads:")
        threads = []
        start_time = time.time()

        # Create and start threads
        for i in range(5):
            thread = threading.Thread(
                target=worker,
                args=(i, i * 0.5 + 1),
                name=f"Worker-{i}"
            )
            threads.append(thread)
            thread.start()
            print(f"   Started thread {i}")

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        end_time = time.time()
        print(f"\\n✅ All threads completed in {end_time - start_time:.2f} seconds")
        print(f"Active threads: {threading.active_count()}")

    def thread_with_return_values(self):
        """Threading with return values using queue"""
        print("\\n" + "=" * 60)
        print("THREADING WITH RETURN VALUES")
        print("=" * 60)

        def fetch_data(thread_id: int, result_queue: queue.Queue):
            """Simulate fetching data from external source"""
            delay = thread_id * 0.3 + 0.5
            time.sleep(delay)  # Simulate network delay

            data = {
                "thread_id": thread_id,
                "data": f"Data from source {thread_id}",
                "fetch_time": delay,
                "timestamp": datetime.now().isoformat()
            }
            result_queue.put(data)
            print(f"Thread {thread_id}: Data fetched in {delay:.1f}s")

        print("\\n1. Using Queue to collect results:")
        result_queue = queue.Queue()
        threads = []

        # Start threads
        for i in range(4):
            thread = threading.Thread(target=fetch_data, args=(i, result_queue))
            threads.append(thread)
            thread.start()

        # Wait for completion
        for thread in threads:
            thread.join()

        # Collect results
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        print("\\n2. Results collected:")
        for result in sorted(results, key=lambda x: x['thread_id']):
            print(f"   Thread {result['thread_id']}: {result['data']}")

        return results

    def thread_synchronization_example(self):
        """Thread synchronization with locks and shared resources"""
        print("\\n" + "=" * 60)
        print("THREAD SYNCHRONIZATION")
        print("=" * 60)

        print("\\n1. Without synchronization (race condition):")
        shared_counter = {"value": 0}

        def increment_unsafe(counter: dict, iterations: int):
            """Unsafe increment without lock"""
            for _ in range(iterations):
                current = counter["value"]
                time.sleep(0.0001)  # Simulate some processing
                counter["value"] = current + 1

        # Unsafe version
        threads = []
        for i in range(3):
            thread = threading.Thread(target=increment_unsafe, args=(shared_counter, 100))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"   Expected: 300, Got: {shared_counter['value']} (likely less due to race condition)")

        print("\\n2. With synchronization (thread-safe):")
        safe_counter = {"value": 0}
        counter_lock = threading.Lock()

        def increment_safe(counter: dict, lock: threading.Lock, iterations: int):
            """Safe increment with lock"""
            for _ in range(iterations):
                with lock:
                    current = counter["value"]
                    time.sleep(0.0001)  # Simulate processing
                    counter["value"] = current + 1

        # Safe version
        threads = []
        for i in range(3):
            thread = threading.Thread(target=increment_safe, args=(safe_counter, counter_lock, 100))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"   Expected: 300, Got: {safe_counter['value']} ✅")

    def producer_consumer_example(self):
        """Producer-Consumer pattern with threading"""
        print("\\n" + "=" * 60)
        print("PRODUCER-CONSUMER PATTERN")
        print("=" * 60)

        task_queue = queue.Queue(maxsize=5)
        result_queue = queue.Queue()

        def producer(name: str, num_items: int):
            """Produce tasks"""
            for i in range(num_items):
                task = f"Task-{i}-from-{name}"
                task_queue.put(task)
                print(f"Producer {name}: Created {task}")
                time.sleep(0.2)
            print(f"Producer {name}: Finished producing {num_items} tasks")

        def consumer(name: str):
            """Consume tasks"""
            while True:
                try:
                    task = task_queue.get(timeout=2)
                    print(f"Consumer {name}: Processing {task}")
                    time.sleep(0.5)  # Simulate processing
                    result = f"Processed-{task}"
                    result_queue.put(result)
                    task_queue.task_done()
                    print(f"Consumer {name}: Completed {task}")
                except queue.Empty:
                    print(f"Consumer {name}: No more tasks, shutting down")
                    break

        print("\\n1. Starting producers and consumers:")

        # Start producers
        producer_threads = []
        for i in range(2):
            thread = threading.Thread(target=producer, args=(f"P{i}", 3))
            producer_threads.append(thread)
            thread.start()

        # Start consumers
        consumer_threads = []
        for i in range(2):
            thread = threading.Thread(target=consumer, args=(f"C{i}"))
            consumer_threads.append(thread)
            thread.start()

        # Wait for all producers to finish
        for thread in producer_threads:
            thread.join()

        # Wait for all tasks to be processed
        task_queue.join()

        # Wait for consumers to finish
        for thread in consumer_threads:
            thread.join()

        print("\\n2. Collecting results:")
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        print(f"   Total results: {len(results)}")
        for result in results[:3]:  # Show first 3
            print(f"   - {result}")


# ============================================================================
# MULTIPROCESSING EXAMPLES
# ============================================================================

class MultiprocessingExample:
    """Comprehensive multiprocessing examples"""

    @staticmethod
    def cpu_intensive_task(n: int) -> dict:
        """CPU-intensive task for multiprocessing demo"""
        start_time = time.time()

        # Calculate prime numbers up to n (CPU-intensive)
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        primes = [i for i in range(2, n + 1) if is_prime(i)]

        end_time = time.time()

        return {
            "process_id": os.getpid(),
            "range": n,
            "primes_found": len(primes),
            "first_few_primes": primes[:10],
            "execution_time": end_time - start_time
        }

    def basic_multiprocessing_example(self):
        """Basic multiprocessing with CPU-intensive tasks"""
        print("\\n" + "=" * 60)
        print("BASIC MULTIPROCESSING EXAMPLE")
        print("=" * 60)

        print(f"\\n1. System info:")
        print(f"   CPU cores: {multiprocessing.cpu_count()}")
        print(f"   Current process ID: {os.getpid()}")

        print("\\n2. Sequential processing:")
        start_time = time.time()
        sequential_results = []

        ranges = [1000, 1500, 2000, 2500]
        for r in ranges:
            result = self.cpu_intensive_task(r)
            sequential_results.append(result)
            print(f"   Range {r}: Found {result['primes_found']} primes in {result['execution_time']:.2f}s")

        sequential_time = time.time() - start_time
        print(f"   Sequential total time: {sequential_time:.2f}s")

        print("\\n3. Parallel processing:")
        start_time = time.time()

        with multiprocessing.Pool(processes=4) as pool:
            parallel_results = pool.map(self.cpu_intensive_task, ranges)

        parallel_time = time.time() - start_time

        print("   Parallel results:")
        for result in parallel_results:
            print(f"   Process {result['process_id']}: Range {result['range']}, "
                  f"{result['primes_found']} primes in {result['execution_time']:.2f}s")

        print(f"   Parallel total time: {parallel_time:.2f}s")
        print(f"   ⚡ Speedup: {sequential_time / parallel_time:.2f}x")

    def process_communication_example(self):
        """Inter-process communication examples"""
        print("\\n" + "=" * 60)
        print("INTER-PROCESS COMMUNICATION")
        print("=" * 60)

        print("\\n1. Using Queue for communication:")

        def worker_with_queue(worker_id: int, input_queue: multiprocessing.Queue,
                            output_queue: multiprocessing.Queue):
            """Worker that processes data from queue"""
            while True:
                try:
                    data = input_queue.get(timeout=2)
                    if data is None:  # Sentinel value to stop
                        break

                    # Process data (simulate work)
                    result = {
                        "worker_id": worker_id,
                        "process_id": os.getpid(),
                        "input": data,
                        "output": data ** 2,
                        "processed_at": datetime.now().isoformat()
                    }

                    output_queue.put(result)
                    print(f"   Worker {worker_id} (PID {os.getpid()}): Processed {data}")

                except Exception as e:
                    print(f"   Worker {worker_id}: Error - {e}")
                    break

        # Create queues
        input_queue = multiprocessing.Queue()
        output_queue = multiprocessing.Queue()

        # Add work to input queue
        work_items = [1, 4, 9, 16, 25, 36, 49, 64]
        for item in work_items:
            input_queue.put(item)

        # Start worker processes
        processes = []
        for i in range(3):
            process = multiprocessing.Process(
                target=worker_with_queue,
                args=(i, input_queue, output_queue)
            )
            processes.append(process)
            process.start()

        # Add sentinel values to stop workers
        for _ in range(3):
            input_queue.put(None)

        # Wait for processes to finish
        for process in processes:
            process.join()

        # Collect results
        results = []
        while not output_queue.empty():
            results.append(output_queue.get())

        print("\\n   Results:")
        for result in sorted(results, key=lambda x: x['input']):
            print(f"   {result['input']}² = {result['output']} "
                  f"(Worker {result['worker_id']}, PID {result['process_id']})")

    def shared_memory_example(self):
        """Shared memory between processes"""
        print("\\n" + "=" * 60)
        print("SHARED MEMORY EXAMPLE")
        print("=" * 60)

        def worker_shared_memory(shared_array: multiprocessing.Array,
                               lock: multiprocessing.Lock, worker_id: int):
            """Worker that modifies shared memory"""
            with lock:
                print(f"   Worker {worker_id} (PID {os.getpid()}): Accessing shared memory")
                for i in range(len(shared_array)):
                    shared_array[i] += worker_id
                    time.sleep(0.1)  # Simulate work
                print(f"   Worker {worker_id}: Updated shared array")

        print("\\n1. Creating shared memory:")
        # Create shared array
        shared_array = multiprocessing.Array('i', [1, 2, 3, 4, 5])  # 'i' = integer
        lock = multiprocessing.Lock()

        print(f"   Initial array: {list(shared_array)}")

        # Start processes that modify shared memory
        processes = []
        for i in range(3):
            process = multiprocessing.Process(
                target=worker_shared_memory,
                args=(shared_array, lock, i + 1)
            )
            processes.append(process)
            process.start()

        # Wait for all processes
        for process in processes:
            process.join()

        print(f"   Final array: {list(shared_array)}")


# ============================================================================
# CONCURRENT.FUTURES - HIGH-LEVEL INTERFACE
# ============================================================================

class ConcurrentFuturesExample:
    """High-level concurrency with concurrent.futures"""

    def thread_pool_executor_example(self):
        """ThreadPoolExecutor for I/O-bound tasks"""
        print("\\n" + "=" * 60)
        print("CONCURRENT.FUTURES - THREADPOOLEXECUTOR")
        print("=" * 60)

        def fetch_url_simulation(url: str, delay: float) -> dict:
            """Simulate fetching URL (I/O-bound)"""
            print(f"   Fetching {url}...")
            time.sleep(delay)  # Simulate network delay
            return {
                "url": url,
                "status": 200,
                "content_length": len(url) * 100,
                "fetch_time": delay
            }

        urls_and_delays = [
            ("https://api.example1.com", 1.0),
            ("https://api.example2.com", 0.8),
            ("https://api.example3.com", 1.2),
            ("https://api.example4.com", 0.6),
            ("https://api.example5.com", 1.4),
        ]

        print("\\n1. Using ThreadPoolExecutor:")
        start_time = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            # Submit tasks
            future_to_url = {
                executor.submit(fetch_url_simulation, url, delay): url
                for url, delay in urls_and_delays
            }

            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    print(f"   ✅ {url}: {result['status']} ({result['content_length']} bytes)")
                except Exception as e:
                    print(f"   ❌ {url}: Error - {e}")

        total_time = time.time() - start_time
        print(f"\\n   Total execution time: {total_time:.2f}s")

    def process_pool_executor_example(self):
        """ProcessPoolExecutor for CPU-bound tasks"""
        print("\\n" + "=" * 60)
        print("CONCURRENT.FUTURES - PROCESSPOOLEXECUTOR")
        print("=" * 60)

        def calculate_factorial(n: int) -> dict:
            """CPU-intensive factorial calculation"""
            start_time = time.time()

            result = 1
            for i in range(1, n + 1):
                result *= i

            return {
                "input": n,
                "factorial": str(result)[:50] + "..." if len(str(result)) > 50 else str(result),
                "process_id": os.getpid(),
                "calculation_time": time.time() - start_time
            }

        numbers = [1000, 2000, 3000, 4000, 5000]

        print("\\n1. Using ProcessPoolExecutor:")
        start_time = time.time()

        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
            # Submit all tasks
            futures = [executor.submit(calculate_factorial, n) for n in numbers]

            # Get results in order of completion
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(f"   Process {result['process_id']}: "
                      f"{result['input']}! = {result['factorial']} "
                      f"({result['calculation_time']:.3f}s)")

        total_time = time.time() - start_time
        print(f"\\n   Total execution time: {total_time:.2f}s")

    def future_callbacks_example(self):
        """Using callbacks with futures"""
        print("\\n" + "=" * 60)
        print("FUTURE CALLBACKS")
        print("=" * 60)

        def process_data(data: int) -> int:
            """Simple data processing"""
            time.sleep(0.5)
            return data * data

        def success_callback(future: concurrent.futures.Future):
            """Callback for successful completion"""
            result = future.result()
            print(f"   ✅ Callback: Task completed with result {result}")

        def error_callback(future: concurrent.futures.Future):
            """Callback for error handling"""
            exception = future.exception()
            if exception:
                print(f"   ❌ Callback: Task failed with error {exception}")

        print("\\n1. Adding callbacks to futures:")

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            for i in range(3):
                future = executor.submit(process_data, i + 1)
                future.add_done_callback(success_callback)
                print(f"   Submitted task {i + 1}")

        print("\\n   All tasks completed with callbacks!")


# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

class PerformanceComparison:
    """Compare threading vs multiprocessing performance"""

    def io_bound_comparison(self):
        """Compare performance for I/O-bound tasks"""
        print("\\n" + "=" * 60)
        print("PERFORMANCE COMPARISON - I/O BOUND TASKS")
        print("=" * 60)

        def io_task(task_id: int) -> dict:
            """Simulate I/O-bound task"""
            start = time.time()
            time.sleep(0.5)  # Simulate I/O delay
            return {
                "task_id": task_id,
                "duration": time.time() - start,
                "process_id": os.getpid()
            }

        tasks = list(range(8))

        print("\\n1. Sequential execution:")
        start_time = time.time()
        sequential_results = [io_task(task_id) for task_id in tasks]
        sequential_time = time.time() - start_time
        print(f"   Time: {sequential_time:.2f}s")

        print("\\n2. Threading execution:")
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            thread_results = list(executor.map(io_task, tasks))
        thread_time = time.time() - start_time
        print(f"   Time: {thread_time:.2f}s, Speedup: {sequential_time/thread_time:.2f}x")

        print("\\n3. Multiprocessing execution:")
        start_time = time.time()
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            process_results = list(executor.map(io_task, tasks))
        process_time = time.time() - start_time
        print(f"   Time: {process_time:.2f}s, Speedup: {sequential_time/process_time:.2f}x")

        print("\\n📊 Results:")
        print(f"   Sequential: {sequential_time:.2f}s")
        print(f"   Threading:  {thread_time:.2f}s ({sequential_time/thread_time:.1f}x faster)")
        print(f"   Multiproc:  {process_time:.2f}s ({sequential_time/process_time:.1f}x faster)")
        print("   💡 Threading is better for I/O-bound tasks!")

    def cpu_bound_comparison(self):
        """Compare performance for CPU-bound tasks"""
        print("\\n" + "=" * 60)
        print("PERFORMANCE COMPARISON - CPU BOUND TASKS")
        print("=" * 60)

        def cpu_task(n: int) -> dict:
            """CPU-intensive task"""
            start = time.time()

            # Calculate sum of squares
            total = sum(i * i for i in range(n))

            return {
                "input": n,
                "result": total,
                "duration": time.time() - start,
                "process_id": os.getpid()
            }

        tasks = [100000, 200000, 300000, 400000]

        print("\\n1. Sequential execution:")
        start_time = time.time()
        sequential_results = [cpu_task(n) for n in tasks]
        sequential_time = time.time() - start_time
        print(f"   Time: {sequential_time:.2f}s")

        print("\\n2. Threading execution:")
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            thread_results = list(executor.map(cpu_task, tasks))
        thread_time = time.time() - start_time
        print(f"   Time: {thread_time:.2f}s, Speedup: {sequential_time/thread_time:.2f}x")

        print("\\n3. Multiprocessing execution:")
        start_time = time.time()
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            process_results = list(executor.map(cpu_task, tasks))
        process_time = time.time() - start_time
        print(f"   Time: {process_time:.2f}s, Speedup: {sequential_time/process_time:.2f}x")

        print("\\n📊 Results:")
        print(f"   Sequential: {sequential_time:.2f}s")
        print(f"   Threading:  {thread_time:.2f}s ({sequential_time/thread_time:.1f}x)")
        print(f"   Multiproc:  {process_time:.2f}s ({sequential_time/process_time:.1f}x faster)")
        print("   💡 Multiprocessing is better for CPU-bound tasks!")


# ============================================================================
# ASYNC VS THREADING COMPARISON
# ============================================================================

async def async_io_task(task_id: int) -> dict:
    """Async I/O task for comparison"""
    start = time.time()
    await asyncio.sleep(0.5)  # Simulate async I/O
    return {
        "task_id": task_id,
        "duration": time.time() - start,
        "type": "async"
    }

def threading_io_task(task_id: int) -> dict:
    """Threading I/O task for comparison"""
    start = time.time()
    time.sleep(0.5)  # Simulate blocking I/O
    return {
        "task_id": task_id,
        "duration": time.time() - start,
        "type": "threading"
    }

async def async_vs_threading_comparison():
    """Compare async/await vs threading for I/O-bound tasks"""
    print("\\n" + "=" * 60)
    print("ASYNC/AWAIT VS THREADING COMPARISON")
    print("=" * 60)

    tasks = list(range(10))

    print("\\n1. Async/await execution:")
    start_time = time.time()
    async_results = await asyncio.gather(*[async_io_task(task_id) for task_id in tasks])
    async_time = time.time() - start_time
    print(f"   Time: {async_time:.2f}s")

    print("\\n2. Threading execution:")
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        thread_results = list(executor.map(threading_io_task, tasks))
    thread_time = time.time() - start_time
    print(f"   Time: {thread_time:.2f}s")

    print("\\n📊 Comparison:")
    print(f"   Async/await: {async_time:.2f}s")
    print(f"   Threading:   {thread_time:.2f}s")

    if async_time < thread_time:
        print(f"   ⚡ Async is {thread_time/async_time:.1f}x faster!")
    else:
        print(f"   ⚡ Threading is {async_time/thread_time:.1f}x faster!")

    print("\\n💡 Key Differences:")
    print("   • Async: Single-threaded, event-driven, lower memory overhead")
    print("   • Threading: Multi-threaded, can have more overhead, easier debugging")
    print("   • Both excel at I/O-bound tasks")


# ============================================================================
# BEST PRACTICES AND GUIDELINES
# ============================================================================

def demonstrate_best_practices():
    """Demonstrate concurrency best practices"""
    print("\\n" + "=" * 60)
    print("CONCURRENCY BEST PRACTICES")
    print("=" * 60)

    print("\\n🎯 When to Use What:")

    print("\\n1. Use THREADING for:")
    print("   ✅ I/O-bound tasks (file operations, network requests)")
    print("   ✅ Tasks that spend time waiting")
    print("   ✅ When you need shared memory between tasks")
    print("   ✅ When task startup overhead matters")

    print("\\n2. Use MULTIPROCESSING for:")
    print("   ✅ CPU-bound tasks (calculations, data processing)")
    print("   ✅ When you need true parallelism")
    print("   ✅ When tasks can run independently")
    print("   ✅ When you want to avoid GIL limitations")

    print("\\n3. Use ASYNC/AWAIT for:")
    print("   ✅ I/O-bound tasks with many concurrent operations")
    print("   ✅ Network programming (web servers, API clients)")
    print("   ✅ When you need to handle thousands of connections")
    print("   ✅ Single-threaded performance is sufficient")

    print("\\n⚠️ Common Pitfalls:")
    print("   ❌ Using threading for CPU-bound tasks (GIL limitation)")
    print("   ❌ Not using locks for shared data (race conditions)")
    print("   ❌ Creating too many threads/processes (overhead)")
    print("   ❌ Not handling exceptions in concurrent code")
    print("   ❌ Using multiprocessing for small tasks (startup overhead)")

    print("\\n🛠️ Best Practices:")
    print("   ✅ Use context managers (with statements)")
    print("   ✅ Always join threads/processes")
    print("   ✅ Implement proper exception handling")
    print("   ✅ Use queues for thread-safe communication")
    print("   ✅ Consider using concurrent.futures for cleaner code")
    print("   ✅ Profile your code to choose the right approach")

    print("\\n📊 Python GIL (Global Interpreter Lock):")
    print("   • Prevents multiple threads from executing Python code simultaneously")
    print("   • Only affects CPU-bound tasks in threading")
    print("   • I/O operations release the GIL")
    print("   • Multiprocessing bypasses GIL (separate interpreters)")
    print("   • Async/await works within GIL (single-threaded)")


def main():
    """Main function demonstrating all concurrency concepts"""
    print("🔄 COMPREHENSIVE CONCURRENCY TUTORIAL")
    print("Learn the differences between threading and multiprocessing in Python!")

    # Threading examples
    thread_example = ThreadExample()
    thread_example.basic_threading_example()
    thread_example.thread_with_return_values()
    thread_example.thread_synchronization_example()
    thread_example.producer_consumer_example()

    # Multiprocessing examples
    multiprocessing_example = MultiprocessingExample()
    multiprocessing_example.basic_multiprocessing_example()
    multiprocessing_example.process_communication_example()
    multiprocessing_example.shared_memory_example()

    # Concurrent futures examples
    futures_example = ConcurrentFuturesExample()
    futures_example.thread_pool_executor_example()
    futures_example.process_pool_executor_example()
    futures_example.future_callbacks_example()

    # Performance comparisons
    perf_comparison = PerformanceComparison()
    perf_comparison.io_bound_comparison()
    perf_comparison.cpu_bound_comparison()

    # Async vs threading comparison
    asyncio.run(async_vs_threading_comparison())

    # Best practices
    demonstrate_best_practices()

    print("\\n" + "=" * 60)
    print("CONCURRENCY TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\\n💡 Key Takeaways:")
    print("• Threading: Best for I/O-bound tasks, shared memory")
    print("• Multiprocessing: Best for CPU-bound tasks, true parallelism")
    print("• Async/await: Best for high-concurrency I/O-bound tasks")
    print("• Use concurrent.futures for cleaner high-level interfaces")
    print("• Always consider the GIL when choosing concurrency approaches")
    print("• Profile your specific use case to make the best choice")

    print("\\n🚀 Next Steps:")
    print("• Experiment with different task types in your applications")
    print("• Learn about asyncio for web programming")
    print("• Explore distributed computing with tools like Celery")
    print("• Study parallel processing libraries like joblib")


if __name__ == "__main__":
    main()