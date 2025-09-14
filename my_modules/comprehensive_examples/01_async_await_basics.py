"""
Comprehensive Async/Await Tutorial
==================================

This module demonstrates asynchronous programming in Python using async/await.
Async programming allows you to run multiple operations concurrently without blocking.
"""

import asyncio
import aiohttp
import time
from typing import List, Dict, Any


# Basic async function
async def basic_async_function():
    """Simple async function that waits for 1 second"""
    print("Starting async function...")
    await asyncio.sleep(1)
    print("Async function completed!")
    return "Done!"


# Async function with parameters
async def greet_async(name: str, delay: int = 1) -> str:
    """Async greeting function with custom delay"""
    print(f"Hello {name}! Starting greeting...")
    await asyncio.sleep(delay)
    greeting = f"Hello {name}! Nice to meet you!"
    print(greeting)
    return greeting


# Multiple async tasks running concurrently
async def fetch_data_simulation(data_id: int, delay: float = 1.0) -> Dict[str, Any]:
    """Simulates fetching data from a database or API"""
    print(f"Fetching data {data_id}...")
    await asyncio.sleep(delay)  # Simulate network/database delay

    data = {
        "id": data_id,
        "data": f"Sample data for ID {data_id}",
        "timestamp": time.time(),
        "processed": True
    }

    print(f"Data {data_id} fetched successfully!")
    return data


async def process_multiple_data_concurrent():
    """Process multiple data items concurrently"""
    print("Starting concurrent data processing...")
    start_time = time.time()

    # Create multiple tasks to run concurrently
    tasks = [
        fetch_data_simulation(1, 1.5),
        fetch_data_simulation(2, 1.0),
        fetch_data_simulation(3, 2.0),
        fetch_data_simulation(4, 0.5),
        fetch_data_simulation(5, 1.2)
    ]

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"All data processed in {end_time - start_time:.2f} seconds")
    print(f"Processed {len(results)} items concurrently")

    return results


async def process_multiple_data_sequential():
    """Process multiple data items sequentially for comparison"""
    print("Starting sequential data processing...")
    start_time = time.time()

    results = []
    delays = [1.5, 1.0, 2.0, 0.5, 1.2]

    for i, delay in enumerate(delays, 1):
        result = await fetch_data_simulation(i, delay)
        results.append(result)

    end_time = time.time()
    print(f"All data processed sequentially in {end_time - start_time:.2f} seconds")

    return results


# Async context manager example
class AsyncDatabaseConnection:
    """Simulated async database connection"""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    async def __aenter__(self):
        print(f"Connecting to database: {self.db_name}")
        await asyncio.sleep(0.5)  # Simulate connection time
        self.connected = True
        print(f"Connected to {self.db_name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from {self.db_name}")
        await asyncio.sleep(0.2)  # Simulate disconnection time
        self.connected = False
        print(f"Disconnected from {self.db_name}")

    async def query(self, sql: str) -> List[Dict[str, Any]]:
        """Execute a query"""
        if not self.connected:
            raise Exception("Database not connected!")

        print(f"Executing query: {sql}")
        await asyncio.sleep(0.3)  # Simulate query time

        # Simulate query results
        return [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30},
            {"id": 3, "name": "Charlie", "age": 35}
        ]


async def database_example():
    """Example using async context manager"""
    async with AsyncDatabaseConnection("user_db") as db:
        results = await db.query("SELECT * FROM users")
        print("Query results:", results)
        return results


# Async generator example
async def async_number_generator(start: int, end: int, delay: float = 0.1):
    """Async generator that yields numbers with delay"""
    print(f"Generating numbers from {start} to {end}")
    for i in range(start, end + 1):
        await asyncio.sleep(delay)
        print(f"Generated: {i}")
        yield i


async def consume_async_generator():
    """Consume async generator"""
    print("Consuming async generator...")
    async for number in async_number_generator(1, 5, 0.2):
        print(f"Received: {number}")
        # Process each number as it arrives
        result = number ** 2
        print(f"Processed: {number}² = {result}")


# Error handling in async functions
async def async_function_with_error(should_fail: bool = False):
    """Async function that may raise an exception"""
    await asyncio.sleep(0.5)

    if should_fail:
        raise ValueError("Simulated async error!")

    return "Success!"


async def handle_async_errors():
    """Demonstrate error handling in async functions"""
    print("Testing async error handling...")

    # Test successful execution
    try:
        result = await async_function_with_error(False)
        print(f"Success case: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")

    # Test error case
    try:
        result = await async_function_with_error(True)
        print(f"This won't print: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")

    # Test multiple async operations with some failing
    tasks = [
        async_function_with_error(False),
        async_function_with_error(True),
        async_function_with_error(False),
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i} succeeded: {result}")


# Advanced: Async with semaphore (rate limiting)
async def rate_limited_operation(operation_id: int, semaphore: asyncio.Semaphore):
    """Operation that respects rate limiting"""
    async with semaphore:  # Only allow N concurrent operations
        print(f"Starting operation {operation_id}")
        await asyncio.sleep(1)  # Simulate work
        print(f"Completed operation {operation_id}")
        return f"Result {operation_id}"


async def demonstrate_rate_limiting():
    """Demonstrate rate limiting with semaphore"""
    print("Demonstrating rate limiting (max 2 concurrent operations)...")

    # Create semaphore that allows only 2 concurrent operations
    semaphore = asyncio.Semaphore(2)

    # Create 5 operations
    tasks = [
        rate_limited_operation(i, semaphore)
        for i in range(1, 6)
    ]

    start_time = time.time()
    results = await asyncio.gather(*tasks)
    end_time = time.time()

    print(f"All operations completed in {end_time - start_time:.2f} seconds")
    print(f"Results: {results}")


# Main demonstration function
async def main():
    """Main function demonstrating all async concepts"""
    print("=" * 60)
    print("COMPREHENSIVE ASYNC/AWAIT TUTORIAL")
    print("=" * 60)

    # 1. Basic async function
    print("\n1. Basic Async Function:")
    result = await basic_async_function()
    print(f"Result: {result}")

    # 2. Async function with parameters
    print("\n2. Async Function with Parameters:")
    greeting = await greet_async("Alice", 0.5)

    # 3. Multiple greetings concurrently
    print("\n3. Multiple Async Operations (Concurrent):")
    greet_tasks = [
        greet_async("Bob", 0.3),
        greet_async("Charlie", 0.4),
        greet_async("Diana", 0.2)
    ]
    greetings = await asyncio.gather(*greet_tasks)
    print(f"All greetings: {greetings}")

    # 4. Compare concurrent vs sequential processing
    print("\n4. Concurrent vs Sequential Processing:")
    concurrent_results = await process_multiple_data_concurrent()
    print(f"Concurrent processing completed. Got {len(concurrent_results)} results.")

    print("\nNow trying sequential processing...")
    sequential_results = await process_multiple_data_sequential()
    print(f"Sequential processing completed. Got {len(sequential_results)} results.")

    # 5. Async context manager
    print("\n5. Async Context Manager:")
    db_results = await database_example()

    # 6. Async generator
    print("\n6. Async Generator:")
    await consume_async_generator()

    # 7. Error handling
    print("\n7. Async Error Handling:")
    await handle_async_errors()

    # 8. Rate limiting
    print("\n8. Rate Limiting with Semaphore:")
    await demonstrate_rate_limiting()

    print("\n" + "=" * 60)
    print("ASYNC/AWAIT TUTORIAL COMPLETED!")
    print("=" * 60)


# Example of creating async tasks and managing them
async def task_management_example():
    """Demonstrate task creation and management"""
    print("\nTask Management Example:")

    # Create tasks
    task1 = asyncio.create_task(greet_async("Task1", 1))
    task2 = asyncio.create_task(greet_async("Task2", 0.5))
    task3 = asyncio.create_task(greet_async("Task3", 1.5))

    print("Tasks created, waiting for completion...")

    # Wait for tasks with timeout
    try:
        results = await asyncio.wait_for(
            asyncio.gather(task1, task2, task3),
            timeout=2.0
        )
        print(f"All tasks completed: {results}")
    except asyncio.TimeoutError:
        print("Some tasks didn't complete within timeout!")

        # Cancel remaining tasks
        for task in [task1, task2, task3]:
            if not task.done():
                task.cancel()
                print(f"Cancelled task: {task}")


if __name__ == "__main__":
    # Run the main async function
    asyncio.run(main())

    # Additional example: task management
    asyncio.run(task_management_example())

    print("\n💡 Key Takeaways:")
    print("- Use 'async def' to define async functions")
    print("- Use 'await' to call async functions")
    print("- Use asyncio.gather() to run multiple async operations concurrently")
    print("- Async functions must be called with 'await' or asyncio.run()")
    print("- Async programming is great for I/O-bound operations")
    print("- Use semaphores for rate limiting")
    print("- Always handle exceptions in async code")