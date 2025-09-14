"""
Comprehensive REST API Tutorial
===============================

This module demonstrates how to work with REST APIs in Python using various libraries.
Covers GET, POST, PUT, DELETE operations, authentication, error handling, and async requests.
"""

import asyncio
import json
import time
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

# Synchronous HTTP requests
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("requests library not available. Install with: pip install requests")

# Asynchronous HTTP requests
try:
    import aiohttp
    AIOHTTP_AVAILABLE = True
except ImportError:
    AIOHTTP_AVAILABLE = False
    print("aiohttp library not available. Install with: pip install aiohttp")


@dataclass
class APIResponse:
    """Structure for API response data"""
    status_code: int
    data: Any
    headers: Dict[str, str]
    response_time: float
    url: str


class JSONPlaceholderAPI:
    """
    Client for JSONPlaceholder API (https://jsonplaceholder.typicode.com/)
    A free fake REST API for testing and prototyping
    """

    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.session = None
        if REQUESTS_AVAILABLE:
            self.session = requests.Session()
            self.session.headers.update({
                "Content-Type": "application/json",
                "User-Agent": "Python REST API Tutorial"
            })

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> APIResponse:
        """Make a synchronous HTTP request"""
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests library required for synchronous requests")

        url = f"{self.base_url}{endpoint}"
        start_time = time.time()

        try:
            if method.upper() == "GET":
                response = self.session.get(url)
            elif method.upper() == "POST":
                response = self.session.post(url, json=data)
            elif method.upper() == "PUT":
                response = self.session.put(url, json=data)
            elif method.upper() == "PATCH":
                response = self.session.patch(url, json=data)
            elif method.upper() == "DELETE":
                response = self.session.delete(url)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response_time = time.time() - start_time
            response.raise_for_status()  # Raise exception for bad status codes

            # Try to parse JSON, fall back to text
            try:
                data = response.json()
            except ValueError:
                data = response.text

            return APIResponse(
                status_code=response.status_code,
                data=data,
                headers=dict(response.headers),
                response_time=response_time,
                url=url
            )

        except requests.exceptions.RequestException as e:
            response_time = time.time() - start_time
            return APIResponse(
                status_code=0,
                data={"error": str(e)},
                headers={},
                response_time=response_time,
                url=url
            )

    # CRUD Operations

    def get_posts(self, limit: Optional[int] = None) -> APIResponse:
        """Get all posts or limited number"""
        endpoint = "/posts"
        if limit:
            endpoint += f"?_limit={limit}"
        return self._make_request("GET", endpoint)

    def get_post(self, post_id: int) -> APIResponse:
        """Get a specific post by ID"""
        return self._make_request("GET", f"/posts/{post_id}")

    def create_post(self, title: str, body: str, user_id: int = 1) -> APIResponse:
        """Create a new post"""
        post_data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self._make_request("POST", "/posts", post_data)

    def update_post(self, post_id: int, title: str, body: str, user_id: int = 1) -> APIResponse:
        """Update an existing post completely"""
        post_data = {
            "id": post_id,
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self._make_request("PUT", f"/posts/{post_id}", post_data)

    def patch_post(self, post_id: int, **kwargs) -> APIResponse:
        """Partially update a post"""
        return self._make_request("PATCH", f"/posts/{post_id}", kwargs)

    def delete_post(self, post_id: int) -> APIResponse:
        """Delete a post"""
        return self._make_request("DELETE", f"/posts/{post_id}")

    def get_users(self) -> APIResponse:
        """Get all users"""
        return self._make_request("GET", "/users")

    def get_user(self, user_id: int) -> APIResponse:
        """Get a specific user"""
        return self._make_request("GET", f"/users/{user_id}")

    def get_user_posts(self, user_id: int) -> APIResponse:
        """Get all posts by a specific user"""
        return self._make_request("GET", f"/users/{user_id}/posts")

    def get_comments(self, post_id: Optional[int] = None) -> APIResponse:
        """Get comments, optionally for a specific post"""
        endpoint = "/comments"
        if post_id:
            endpoint += f"?postId={post_id}"
        return self._make_request("GET", endpoint)


class AsyncJSONPlaceholderAPI:
    """
    Async client for JSONPlaceholder API
    """

    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    async def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> APIResponse:
        """Make an asynchronous HTTP request"""
        if not AIOHTTP_AVAILABLE:
            raise ImportError("aiohttp library required for asynchronous requests")

        url = f"{self.base_url}{endpoint}"
        start_time = time.time()

        async with aiohttp.ClientSession() as session:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "User-Agent": "Python Async REST API Tutorial"
                }

                if method.upper() == "GET":
                    async with session.get(url, headers=headers) as response:
                        response_data = await response.json()
                elif method.upper() == "POST":
                    async with session.post(url, json=data, headers=headers) as response:
                        response_data = await response.json()
                elif method.upper() == "PUT":
                    async with session.put(url, json=data, headers=headers) as response:
                        response_data = await response.json()
                elif method.upper() == "PATCH":
                    async with session.patch(url, json=data, headers=headers) as response:
                        response_data = await response.json()
                elif method.upper() == "DELETE":
                    async with session.delete(url, headers=headers) as response:
                        response_data = await response.json()
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")

                response_time = time.time() - start_time
                response.raise_for_status()

                return APIResponse(
                    status_code=response.status,
                    data=response_data,
                    headers=dict(response.headers),
                    response_time=response_time,
                    url=url
                )

            except Exception as e:
                response_time = time.time() - start_time
                return APIResponse(
                    status_code=0,
                    data={"error": str(e)},
                    headers={},
                    response_time=response_time,
                    url=url
                )

    async def get_posts(self, limit: Optional[int] = None) -> APIResponse:
        """Get all posts asynchronously"""
        endpoint = "/posts"
        if limit:
            endpoint += f"?_limit={limit}"
        return await self._make_request("GET", endpoint)

    async def get_multiple_posts(self, post_ids: List[int]) -> List[APIResponse]:
        """Get multiple posts concurrently"""
        tasks = [self._make_request("GET", f"/posts/{post_id}") for post_id in post_ids]
        return await asyncio.gather(*tasks)

    async def create_post(self, title: str, body: str, user_id: int = 1) -> APIResponse:
        """Create a new post asynchronously"""
        post_data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return await self._make_request("POST", "/posts", post_data)


def demonstrate_sync_api():
    """Demonstrate synchronous API operations"""
    if not REQUESTS_AVAILABLE:
        print("Skipping sync API demo - requests library not available")
        return

    print("=" * 60)
    print("SYNCHRONOUS REST API OPERATIONS")
    print("=" * 60)

    api = JSONPlaceholderAPI()

    # 1. GET request - fetch posts
    print("\n1. GET Request - Fetching posts:")
    response = api.get_posts(limit=3)
    if response.status_code == 200:
        print(f"✅ Success! Got {len(response.data)} posts")
        print(f"Response time: {response.response_time:.3f}s")
        print(f"First post title: {response.data[0]['title']}")
    else:
        print(f"❌ Error: {response.data}")

    # 2. GET request - fetch specific post
    print("\n2. GET Request - Fetching specific post:")
    response = api.get_post(1)
    if response.status_code == 200:
        print(f"✅ Success! Post title: {response.data['title']}")
        print(f"Post body: {response.data['body'][:50]}...")
    else:
        print(f"❌ Error: {response.data}")

    # 3. POST request - create new post
    print("\n3. POST Request - Creating new post:")
    new_post_data = {
        "title": "My New Post from Python",
        "body": "This is a post created using Python and the requests library!",
        "userId": 1
    }
    response = api.create_post(
        title=new_post_data["title"],
        body=new_post_data["body"],
        user_id=new_post_data["userId"]
    )
    if response.status_code == 201:
        print(f"✅ Success! Created post with ID: {response.data['id']}")
        print(f"Title: {response.data['title']}")
    else:
        print(f"❌ Error: {response.data}")

    # 4. PUT request - update post
    print("\n4. PUT Request - Updating post:")
    updated_data = {
        "title": "Updated Post Title",
        "body": "This post has been updated using PUT request",
        "userId": 1
    }
    response = api.update_post(1, **updated_data)
    if response.status_code == 200:
        print(f"✅ Success! Updated post title: {response.data['title']}")
    else:
        print(f"❌ Error: {response.data}")

    # 5. PATCH request - partial update
    print("\n5. PATCH Request - Partial update:")
    response = api.patch_post(1, title="Partially Updated Title")
    if response.status_code == 200:
        print(f"✅ Success! New title: {response.data['title']}")
    else:
        print(f"❌ Error: {response.data}")

    # 6. DELETE request
    print("\n6. DELETE Request - Deleting post:")
    response = api.delete_post(1)
    if response.status_code == 200:
        print(f"✅ Success! Post deleted")
    else:
        print(f"❌ Error: {response.data}")

    # 7. Working with users and relationships
    print("\n7. GET Request - User and their posts:")
    user_response = api.get_user(1)
    posts_response = api.get_user_posts(1)

    if user_response.status_code == 200 and posts_response.status_code == 200:
        user = user_response.data
        posts = posts_response.data
        print(f"✅ User: {user['name']} ({user['email']})")
        print(f"✅ User has {len(posts)} posts")
        print(f"Latest post: {posts[0]['title']}")

    # 8. Comments for a post
    print("\n8. GET Request - Comments for a post:")
    comments_response = api.get_comments(post_id=1)
    if comments_response.status_code == 200:
        comments = comments_response.data
        print(f"✅ Post has {len(comments)} comments")
        print(f"First comment by: {comments[0]['name']}")


async def demonstrate_async_api():
    """Demonstrate asynchronous API operations"""
    if not AIOHTTP_AVAILABLE:
        print("Skipping async API demo - aiohttp library not available")
        return

    print("\n" + "=" * 60)
    print("ASYNCHRONOUS REST API OPERATIONS")
    print("=" * 60)

    api = AsyncJSONPlaceholderAPI()

    # 1. Single async request
    print("\n1. Async GET Request:")
    response = await api.get_posts(limit=3)
    if response.status_code == 200:
        print(f"✅ Success! Got {len(response.data)} posts")
        print(f"Response time: {response.response_time:.3f}s")

    # 2. Multiple concurrent requests
    print("\n2. Multiple Concurrent Requests:")
    start_time = time.time()

    # Get multiple posts concurrently
    post_ids = [1, 2, 3, 4, 5]
    responses = await api.get_multiple_posts(post_ids)

    end_time = time.time()
    successful_responses = [r for r in responses if r.status_code == 200]

    print(f"✅ Fetched {len(successful_responses)} posts concurrently")
    print(f"Total time: {end_time - start_time:.3f}s")
    print(f"Average response time per request: {sum(r.response_time for r in responses) / len(responses):.3f}s")

    for i, response in enumerate(responses):
        if response.status_code == 200:
            print(f"  Post {i+1}: {response.data['title'][:30]}...")

    # 3. Async POST request
    print("\n3. Async POST Request:")
    response = await api.create_post(
        title="Async Created Post",
        body="This post was created using async/await!",
        user_id=1
    )
    if response.status_code == 201:
        print(f"✅ Success! Created post with ID: {response.data['id']}")

    # 4. Batch operations
    print("\n4. Batch Async Operations:")
    start_time = time.time()

    # Create multiple posts concurrently
    post_tasks = [
        api.create_post(f"Async Post {i}", f"Body for async post {i}", 1)
        for i in range(1, 4)
    ]

    create_responses = await asyncio.gather(*post_tasks)
    end_time = time.time()

    successful_creates = [r for r in create_responses if r.status_code == 201]
    print(f"✅ Created {len(successful_creates)} posts concurrently")
    print(f"Batch creation time: {end_time - start_time:.3f}s")


class APIErrorHandler:
    """Utility class for handling API errors and responses"""

    @staticmethod
    def handle_response(response: APIResponse, operation: str = "API call") -> bool:
        """Handle and log API response"""
        if response.status_code == 0:
            print(f"❌ {operation} failed: Network error - {response.data.get('error', 'Unknown error')}")
            return False
        elif 200 <= response.status_code < 300:
            print(f"✅ {operation} successful (Status: {response.status_code})")
            print(f"   Response time: {response.response_time:.3f}s")
            return True
        elif response.status_code == 404:
            print(f"⚠️ {operation}: Resource not found (404)")
            return False
        elif 400 <= response.status_code < 500:
            print(f"❌ {operation}: Client error (Status: {response.status_code})")
            print(f"   Error: {response.data}")
            return False
        elif 500 <= response.status_code < 600:
            print(f"❌ {operation}: Server error (Status: {response.status_code})")
            return False
        else:
            print(f"❓ {operation}: Unexpected status code {response.status_code}")
            return False

    @staticmethod
    def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
        """Decorator for retrying failed API calls"""
        def decorator(func):
            async def async_wrapper(*args, **kwargs):
                for attempt in range(max_retries):
                    try:
                        result = await func(*args, **kwargs)
                        if isinstance(result, APIResponse) and result.status_code > 0:
                            return result
                    except Exception as e:
                        print(f"Attempt {attempt + 1} failed: {e}")

                    if attempt < max_retries - 1:
                        await asyncio.sleep(delay)

                return None  # All retries failed

            def sync_wrapper(*args, **kwargs):
                for attempt in range(max_retries):
                    try:
                        result = func(*args, **kwargs)
                        if isinstance(result, APIResponse) and result.status_code > 0:
                            return result
                    except Exception as e:
                        print(f"Attempt {attempt + 1} failed: {e}")

                    if attempt < max_retries - 1:
                        time.sleep(delay)

                return None  # All retries failed

            return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
        return decorator


def demonstrate_error_handling():
    """Demonstrate error handling patterns"""
    if not REQUESTS_AVAILABLE:
        print("Skipping error handling demo - requests library not available")
        return

    print("\n" + "=" * 60)
    print("API ERROR HANDLING PATTERNS")
    print("=" * 60)

    api = JSONPlaceholderAPI()
    handler = APIErrorHandler()

    # 1. Successful request
    print("\n1. Successful Request:")
    response = api.get_post(1)
    handler.handle_response(response, "Get post 1")

    # 2. Resource not found
    print("\n2. Resource Not Found:")
    response = api.get_post(999999)  # Non-existent post
    handler.handle_response(response, "Get non-existent post")

    # 3. Invalid endpoint (will cause error)
    print("\n3. Invalid Endpoint:")
    try:
        # Manually create invalid request
        invalid_response = api._make_request("GET", "/invalid-endpoint")
        handler.handle_response(invalid_response, "Invalid endpoint")
    except Exception as e:
        print(f"❌ Exception caught: {e}")


# Real-world example: Weather API (if you have an API key)
class WeatherAPI:
    """Example of real-world API with authentication"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_weather(self, city: str) -> Dict[str, Any]:
        """Get weather for a city (requires valid API key)"""
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests library required")

        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise Exception("Invalid API key")
        elif response.status_code == 404:
            raise Exception(f"City '{city}' not found")
        else:
            raise Exception(f"API error: {response.status_code}")


def main():
    """Main function demonstrating all REST API concepts"""
    print("🌐 COMPREHENSIVE REST API TUTORIAL")
    print("This tutorial covers HTTP methods, async requests, error handling, and best practices.")
    print("Using JSONPlaceholder API (https://jsonplaceholder.typicode.com/)")

    # Check library availability
    print(f"\nLibrary Status:")
    print(f"✅ requests: {'Available' if REQUESTS_AVAILABLE else '❌ Not installed'}")
    print(f"✅ aiohttp: {'Available' if AIOHTTP_AVAILABLE else '❌ Not installed'}")

    # Run synchronous examples
    demonstrate_sync_api()

    # Run error handling examples
    demonstrate_error_handling()


async def main_async():
    """Run async examples"""
    if AIOHTTP_AVAILABLE:
        await demonstrate_async_api()
    else:
        print("\nSkipping async examples - aiohttp not installed")
        print("Install with: pip install aiohttp")


if __name__ == "__main__":
    # Run synchronous examples
    main()

    # Run asynchronous examples
    asyncio.run(main_async())

    print("\n" + "=" * 60)
    print("REST API TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\n💡 Key Takeaways:")
    print("- Use requests library for synchronous HTTP requests")
    print("- Use aiohttp library for asynchronous HTTP requests")
    print("- Always handle errors and check status codes")
    print("- Use async/await for concurrent API calls")
    print("- Implement retry logic for unreliable APIs")
    print("- Use session objects for connection pooling")
    print("- Include proper headers and authentication")
    print("- Structure your API responses with proper data classes")

    print("\n📚 Next Steps:")
    print("- Learn about API authentication (OAuth, JWT, API keys)")
    print("- Explore GraphQL APIs")
    print("- Build your own REST API with Flask/FastAPI")
    print("- Learn about API rate limiting and caching")
    print("- Study RESTful design principles")