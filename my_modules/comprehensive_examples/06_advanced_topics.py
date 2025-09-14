"""
Advanced Python Topics Tutorial
===============================

This module covers advanced Python concepts that every developer should know:
- Regular Expressions (regex)
- Database Operations (SQLite, PostgreSQL)
- Logging and Debugging
- Environment Variables and Configuration
- Performance Optimization
- Memory Management
- Security Best Practices
"""

import re
import sqlite3
import logging
import os
import sys
import time
import json
import hashlib
import secrets
import traceback
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
import configparser

# Try to import optional database libraries
try:
    import psycopg2
    POSTGRES_AVAILABLE = True
except ImportError:
    POSTGRES_AVAILABLE = False

try:
    from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    SQLALCHEMY_AVAILABLE = True
except ImportError:
    SQLALCHEMY_AVAILABLE = False


# ============================================================================
# REGULAR EXPRESSIONS
# ============================================================================

def demonstrate_regex_basics():
    """Demonstrate basic regular expression patterns and operations"""
    print("=" * 60)
    print("REGULAR EXPRESSIONS (REGEX)")
    print("=" * 60)

    print("\\n1. Basic Pattern Matching:")

    # Simple pattern matching
    text = "The quick brown fox jumps over the lazy dog"
    pattern = r"fox"

    if re.search(pattern, text):
        print(f"   ✅ Found '{pattern}' in text")
    else:
        print(f"   ❌ '{pattern}' not found")

    # Case-insensitive matching
    pattern_ci = r"FOX"
    match = re.search(pattern_ci, text, re.IGNORECASE)
    if match:
        print(f"   ✅ Found '{pattern_ci}' (case-insensitive) at position {match.start()}")

    print("\\n2. Common Patterns:")

    # Email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    emails = [
        "user@example.com",
        "test.email+tag@domain.co.uk",
        "invalid.email",
        "another@domain"
    ]

    print("   Email validation:")
    for email in emails:
        if re.match(email_pattern, email):
            print(f"     ✅ {email} - Valid")
        else:
            print(f"     ❌ {email} - Invalid")

    # Phone number patterns
    phone_pattern = r'^\\+?1?[- .]?\\(?([0-9]{3})\\)?[- .]?([0-9]{3})[- .]?([0-9]{4})$'
    phones = [
        "+1-555-123-4567",
        "(555) 123-4567",
        "555.123.4567",
        "5551234567",
        "invalid-phone"
    ]

    print("\\n   Phone number validation:")
    for phone in phones:
        match = re.match(phone_pattern, phone)
        if match:
            print(f"     ✅ {phone} - Valid (Area: {match.group(1)})")
        else:
            print(f"     ❌ {phone} - Invalid")

    print("\\n3. Text Processing:")

    # Find all words
    text = "Python is awesome! It's great for data science, web development, and automation."
    words = re.findall(r'\\b\\w+\\b', text)
    print(f"   Words found: {words[:10]}...")  # First 10 words

    # Extract numbers
    numbers_text = "Order #12345 costs $99.99 and includes 3 items weighing 2.5kg each"
    numbers = re.findall(r'\\d+\\.?\\d*', numbers_text)
    print(f"   Numbers found: {numbers}")

    # Replace patterns
    censored = re.sub(r'\\b(awesome|great)\\b', '***', text, flags=re.IGNORECASE)
    print(f"   Censored text: {censored}")

    print("\\n4. Advanced Patterns:")

    # Named groups
    log_pattern = r'(?P<timestamp>\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}) (?P<level>\\w+) (?P<message>.*)'
    log_line = "2024-01-15 14:30:25 ERROR Failed to connect to database"

    match = re.match(log_pattern, log_line)
    if match:
        print("   Log parsing with named groups:")
        print(f"     Timestamp: {match.group('timestamp')}")
        print(f"     Level: {match.group('level')}")
        print(f"     Message: {match.group('message')}")

    # Lookahead and lookbehind
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$'
    passwords = [
        "Password123!",
        "weakpass",
        "NoSpecialChar123",
        "nouppercasechar123!",
        "NOLOWERCASECHAR123!"
    ]

    print("\\n   Password strength validation:")
    for pwd in passwords:
        if re.match(password_pattern, pwd):
            print(f"     ✅ {pwd} - Strong")
        else:
            print(f"     ❌ {pwd} - Weak")


class RegexProcessor:
    """Advanced regex processing class"""

    def __init__(self):
        # Pre-compile common patterns for better performance
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')
        self.url_pattern = re.compile(r'https?://(?:[-\\w.])+(?:[:\\d]+)?(?:/(?:[\\w/_.])*(?:\\?(?:[&\\w]*))?)?')
        self.phone_pattern = re.compile(r'\\+?1?[- .]?\\(?([0-9]{3})\\)?[- .]?([0-9]{3})[- .]?([0-9]{4})')
        self.ip_pattern = re.compile(r'\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b')

    def extract_emails(self, text: str) -> List[str]:
        """Extract all email addresses from text"""
        return self.email_pattern.findall(text)

    def extract_urls(self, text: str) -> List[str]:
        """Extract all URLs from text"""
        return self.url_pattern.findall(text)

    def extract_phones(self, text: str) -> List[str]:
        """Extract all phone numbers from text"""
        matches = self.phone_pattern.findall(text)
        return [f"({area})-{prefix}-{number}" for area, prefix, number in matches]

    def extract_ips(self, text: str) -> List[str]:
        """Extract all IP addresses from text"""
        return self.ip_pattern.findall(text)

    def clean_text(self, text: str) -> str:
        """Clean text by removing extra whitespace and special characters"""
        # Remove extra whitespace
        text = re.sub(r'\\s+', ' ', text)
        # Remove special characters except basic punctuation
        text = re.sub(r'[^\\w\\s.,!?-]', '', text)
        return text.strip()


# ============================================================================
# DATABASE OPERATIONS
# ============================================================================

class DatabaseManager:
    """Comprehensive database operations with SQLite"""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connection = None

    def connect(self) -> sqlite3.Connection:
        """Create database connection"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Enable dict-like access
            print(f"✅ Connected to SQLite database: {self.db_path}")
            return self.connection
        except sqlite3.Error as e:
            print(f"❌ Database connection error: {e}")
            raise

    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("✅ Database connection closed")

    @contextmanager
    def get_cursor(self):
        """Context manager for database cursor"""
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        try:
            yield cursor
            self.connection.commit()
        except sqlite3.Error as e:
            self.connection.rollback()
            print(f"❌ Database error: {e}")
            raise
        finally:
            cursor.close()

    def create_tables(self):
        """Create sample tables"""
        with self.get_cursor() as cursor:
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')

            # Posts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')

            # Comments table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    post_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (post_id) REFERENCES posts (id),
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')

            print("✅ Database tables created successfully")

    def create_user(self, username: str, email: str, password: str) -> int:
        """Create a new user"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        with self.get_cursor() as cursor:
            cursor.execute('''
                INSERT INTO users (username, email, password_hash)
                VALUES (?, ?, ?)
            ''', (username, email, password_hash))

            user_id = cursor.lastrowid
            print(f"✅ Created user: {username} (ID: {user_id})")
            return user_id

    def get_user_by_email(self, email: str) -> Optional[Dict]:
        """Get user by email"""
        with self.get_cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def create_post(self, user_id: int, title: str, content: str) -> int:
        """Create a new post"""
        with self.get_cursor() as cursor:
            cursor.execute('''
                INSERT INTO posts (user_id, title, content)
                VALUES (?, ?, ?)
            ''', (user_id, title, content))

            post_id = cursor.lastrowid
            print(f"✅ Created post: {title} (ID: {post_id})")
            return post_id

    def get_posts_with_users(self, limit: int = 10) -> List[Dict]:
        """Get posts with user information"""
        with self.get_cursor() as cursor:
            cursor.execute('''
                SELECT p.id, p.title, p.content, p.created_at,
                       u.username, u.email
                FROM posts p
                JOIN users u ON p.user_id = u.id
                ORDER BY p.created_at DESC
                LIMIT ?
            ''', (limit,))

            return [dict(row) for row in cursor.fetchall()]

    def add_comment(self, post_id: int, user_id: int, content: str) -> int:
        """Add comment to a post"""
        with self.get_cursor() as cursor:
            cursor.execute('''
                INSERT INTO comments (post_id, user_id, content)
                VALUES (?, ?, ?)
            ''', (post_id, user_id, content))

            comment_id = cursor.lastrowid
            print(f"✅ Added comment (ID: {comment_id}) to post {post_id}")
            return comment_id

    def get_user_statistics(self) -> Dict[str, Any]:
        """Get user statistics"""
        with self.get_cursor() as cursor:
            # Total users
            cursor.execute('SELECT COUNT(*) as total_users FROM users')
            total_users = cursor.fetchone()['total_users']

            # Active users
            cursor.execute('SELECT COUNT(*) as active_users FROM users WHERE is_active = 1')
            active_users = cursor.fetchone()['active_users']

            # Total posts
            cursor.execute('SELECT COUNT(*) as total_posts FROM posts')
            total_posts = cursor.fetchone()['total_posts']

            # Total comments
            cursor.execute('SELECT COUNT(*) as total_comments FROM comments')
            total_comments = cursor.fetchone()['total_comments']

            # Most active user
            cursor.execute('''
                SELECT u.username, COUNT(p.id) as post_count
                FROM users u
                LEFT JOIN posts p ON u.id = p.user_id
                GROUP BY u.id, u.username
                ORDER BY post_count DESC
                LIMIT 1
            ''')
            most_active = cursor.fetchone()

            return {
                'total_users': total_users,
                'active_users': active_users,
                'total_posts': total_posts,
                'total_comments': total_comments,
                'most_active_user': dict(most_active) if most_active else None
            }


def demonstrate_database_operations():
    """Demonstrate database operations"""
    print("\\n" + "=" * 60)
    print("DATABASE OPERATIONS")
    print("=" * 60)

    print("\\n1. SQLite Database Operations:")

    # Create in-memory database for demo
    db = DatabaseManager(":memory:")
    db.connect()
    db.create_tables()

    # Create sample users
    user1_id = db.create_user("john_doe", "john@example.com", "secure_password123")
    user2_id = db.create_user("jane_smith", "jane@example.com", "another_password456")
    user3_id = db.create_user("bob_wilson", "bob@example.com", "password789")

    # Create sample posts
    post1_id = db.create_post(user1_id, "Getting Started with Python", "Python is a great programming language...")
    post2_id = db.create_post(user2_id, "Database Design Best Practices", "When designing databases, consider...")
    post3_id = db.create_post(user1_id, "Advanced Python Techniques", "Here are some advanced Python concepts...")

    # Add comments
    db.add_comment(post1_id, user2_id, "Great article! Very helpful for beginners.")
    db.add_comment(post1_id, user3_id, "Thanks for sharing this information.")
    db.add_comment(post2_id, user1_id, "Excellent points about database design.")

    print("\\n2. Querying Data:")

    # Get posts with users
    posts = db.get_posts_with_users(5)
    print("\\n   Recent posts:")
    for post in posts:
        print(f"     📝 '{post['title']}' by {post['username']} ({post['created_at']})")

    # Get user by email
    user = db.get_user_by_email("john@example.com")
    if user:
        print(f"\\n   User found: {user['username']} (Active: {bool(user['is_active'])})")

    # Get statistics
    stats = db.get_user_statistics()
    print("\\n   Database statistics:")
    for key, value in stats.items():
        if key == 'most_active_user' and value:
            print(f"     {key}: {value['username']} ({value['post_count']} posts)")
        else:
            print(f"     {key}: {value}")

    db.disconnect()

    print("\\n3. PostgreSQL Example (if available):")
    if POSTGRES_AVAILABLE:
        print("   ✅ PostgreSQL driver available")
        print("   Connection example:")
        print("     conn = psycopg2.connect(")
        print("         host='localhost',")
        print("         database='mydb',")
        print("         user='username',")
        print("         password='password'")
        print("     )")
    else:
        print("   ❌ PostgreSQL driver not available")
        print("   Install with: pip install psycopg2-binary")

    print("\\n4. SQLAlchemy ORM Example:")
    if SQLALCHEMY_AVAILABLE:
        print("   ✅ SQLAlchemy available")
        print("   ORM model example:")
        print("     Base = declarative_base()")
        print("     class User(Base):")
        print("         __tablename__ = 'users'")
        print("         id = Column(Integer, primary_key=True)")
        print("         username = Column(String(50), unique=True)")
    else:
        print("   ❌ SQLAlchemy not available")
        print("   Install with: pip install sqlalchemy")


# ============================================================================
# LOGGING AND DEBUGGING
# ============================================================================

def setup_logging():
    """Setup comprehensive logging configuration"""

    # Create logs directory
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        handlers=[
            # File handler for all logs
            logging.FileHandler(log_dir / 'application.log'),
            # Console handler for warnings and above
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Set console handler to WARNING level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Create loggers for different modules
    app_logger = logging.getLogger('app')
    db_logger = logging.getLogger('database')
    api_logger = logging.getLogger('api')

    # Add handlers to specific loggers
    error_handler = logging.FileHandler(log_dir / 'errors.log')
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s\\n%(pathname)s:%(lineno)d\\n%(funcName)s\\n---')
    error_handler.setFormatter(error_formatter)

    app_logger.addHandler(error_handler)
    db_logger.addHandler(error_handler)
    api_logger.addHandler(error_handler)

    return app_logger, db_logger, api_logger


class PerformanceTimer:
    """Context manager for timing operations"""

    def __init__(self, operation_name: str, logger: logging.Logger = None):
        self.operation_name = operation_name
        self.logger = logger or logging.getLogger(__name__)
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.logger.info(f"Starting {self.operation_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        duration = end_time - self.start_time

        if exc_type:
            self.logger.error(f"{self.operation_name} failed after {duration:.3f}s: {exc_val}")
        else:
            self.logger.info(f"{self.operation_name} completed in {duration:.3f}s")


def demonstrate_logging_and_debugging():
    """Demonstrate logging and debugging techniques"""
    print("\\n" + "=" * 60)
    print("LOGGING AND DEBUGGING")
    print("=" * 60)

    print("\\n1. Setting up logging:")
    app_logger, db_logger, api_logger = setup_logging()

    print("\\n2. Different log levels:")
    app_logger.debug("This is a debug message - detailed information")
    app_logger.info("This is an info message - general information")
    app_logger.warning("This is a warning message - something unexpected")
    app_logger.error("This is an error message - something failed")
    app_logger.critical("This is a critical message - serious problem")

    print("\\n3. Structured logging with context:")

    def process_user_data(user_id: int, operation: str):
        """Example function with logging"""
        logger = logging.getLogger('app.user_processor')

        logger.info(f"Processing user {user_id} for operation: {operation}")

        try:
            # Simulate some processing
            if user_id < 0:
                raise ValueError("User ID cannot be negative")

            # Simulate database operation
            with PerformanceTimer(f"Database query for user {user_id}", db_logger):
                time.sleep(0.1)  # Simulate work

            logger.info(f"Successfully processed user {user_id}")
            return {"status": "success", "user_id": user_id}

        except ValueError as e:
            logger.error(f"Validation error for user {user_id}: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.exception(f"Unexpected error processing user {user_id}")
            return {"status": "error", "error": "Internal error"}

    # Test the function
    process_user_data(123, "update_profile")
    process_user_data(-1, "delete_user")  # This will cause an error

    print("\\n4. Debugging techniques:")

    def debug_example():
        """Example function with debugging"""
        logger = logging.getLogger('app.debug')

        data = {"name": "John", "age": 30, "skills": ["Python", "SQL"]}

        # Debug variable contents
        logger.debug(f"Processing data: {data}")

        # Use assertions for debugging
        assert isinstance(data, dict), "Data must be a dictionary"
        assert "name" in data, "Name field is required"

        # Conditional debugging
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(f"Data keys: {list(data.keys())}")
            logger.debug(f"Skills count: {len(data.get('skills', []))}")

        return data

    debug_example()

    print("\\n5. Exception handling with logging:")

    def risky_operation(value: str):
        """Example of exception handling with logging"""
        logger = logging.getLogger('app.risky')

        try:
            logger.info(f"Starting risky operation with value: {value}")

            # Simulate various types of errors
            if value == "zero":
                result = 10 / 0
            elif value == "type":
                result = int("not_a_number")
            elif value == "key":
                result = {"a": 1}["b"]
            else:
                result = f"Success with {value}"

            logger.info(f"Operation completed successfully: {result}")
            return result

        except ZeroDivisionError:
            logger.error("Division by zero error", exc_info=True)
            raise
        except ValueError as e:
            logger.error(f"Value error: {e}", exc_info=True)
            raise
        except KeyError as e:
            logger.error(f"Key error: {e}", exc_info=True)
            raise
        except Exception:
            logger.exception("Unexpected error in risky operation")
            raise

    # Test exception handling
    for test_value in ["success", "zero", "type", "key"]:
        try:
            risky_operation(test_value)
        except Exception as e:
            print(f"   Handled exception for '{test_value}': {type(e).__name__}")

    print("\\n   ✅ Check 'logs/' directory for detailed log files")


# ============================================================================
# ENVIRONMENT VARIABLES AND CONFIGURATION
# ============================================================================

@dataclass
class AppConfig:
    """Application configuration with environment variable support"""
    database_url: str
    api_key: str
    debug: bool
    log_level: str
    max_connections: int
    timeout: float

    @classmethod
    def from_env(cls) -> 'AppConfig':
        """Create configuration from environment variables"""
        return cls(
            database_url=os.getenv('DATABASE_URL', 'sqlite:///default.db'),
            api_key=os.getenv('API_KEY', 'default-api-key'),
            debug=os.getenv('DEBUG', 'False').lower() == 'true',
            log_level=os.getenv('LOG_LEVEL', 'INFO'),
            max_connections=int(os.getenv('MAX_CONNECTIONS', '10')),
            timeout=float(os.getenv('TIMEOUT', '30.0'))
        )


class ConfigManager:
    """Advanced configuration management"""

    def __init__(self, config_file: str = None):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.env_vars = {}

    def load_from_file(self, filename: str):
        """Load configuration from INI file"""
        try:
            self.config.read(filename)
            print(f"✅ Configuration loaded from {filename}")
        except Exception as e:
            print(f"❌ Failed to load config file {filename}: {e}")

    def load_from_json(self, filename: str):
        """Load configuration from JSON file"""
        try:
            with open(filename, 'r') as f:
                self.json_config = json.load(f)
            print(f"✅ JSON configuration loaded from {filename}")
        except Exception as e:
            print(f"❌ Failed to load JSON config {filename}: {e}")

    def get(self, key: str, section: str = 'DEFAULT', default: Any = None) -> Any:
        """Get configuration value with fallback to environment variables"""
        # First try environment variable
        env_key = f"{section}_{key}".upper()
        env_value = os.getenv(env_key)
        if env_value:
            return self._convert_value(env_value)

        # Then try config file
        try:
            value = self.config.get(section, key)
            return self._convert_value(value)
        except (configparser.NoSectionError, configparser.NoOptionError):
            pass

        # Return default
        return default

    def _convert_value(self, value: str) -> Any:
        """Convert string value to appropriate type"""
        # Boolean
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'

        # Integer
        try:
            return int(value)
        except ValueError:
            pass

        # Float
        try:
            return float(value)
        except ValueError:
            pass

        # String
        return value

    def create_sample_config(self, filename: str):
        """Create a sample configuration file"""
        config_content = """[database]
url = sqlite:///app.db
max_connections = 10
timeout = 30.0

[api]
key = your-api-key-here
base_url = https://api.example.com
rate_limit = 100

[logging]
level = INFO
file = app.log
max_size = 10485760

[security]
secret_key = generate-random-secret-key
password_min_length = 8
session_timeout = 3600
"""
        try:
            with open(filename, 'w') as f:
                f.write(config_content)
            print(f"✅ Sample configuration created: {filename}")
        except Exception as e:
            print(f"❌ Failed to create config file: {e}")


def demonstrate_environment_and_config():
    """Demonstrate environment variables and configuration management"""
    print("\\n" + "=" * 60)
    print("ENVIRONMENT VARIABLES AND CONFIGURATION")
    print("=" * 60)

    print("\\n1. Environment Variables:")

    # Set some environment variables for demo
    os.environ['APP_DEBUG'] = 'true'
    os.environ['APP_API_KEY'] = 'demo-api-key-12345'
    os.environ['APP_MAX_CONNECTIONS'] = '20'

    # Read environment variables
    debug_mode = os.getenv('APP_DEBUG', 'false').lower() == 'true'
    api_key = os.getenv('APP_API_KEY', 'default-key')
    max_conn = int(os.getenv('APP_MAX_CONNECTIONS', '10'))

    print(f"   Debug mode: {debug_mode}")
    print(f"   API key: {api_key[:10]}...")
    print(f"   Max connections: {max_conn}")

    # Show all environment variables (first 5)
    print("\\n   Environment variables (sample):")
    for i, (key, value) in enumerate(os.environ.items()):
        if i >= 5:
            break
        display_value = value[:30] + "..." if len(value) > 30 else value
        print(f"     {key}: {display_value}")

    print("\\n2. Configuration from dataclass:")

    # Create config from environment
    app_config = AppConfig.from_env()
    print(f"   Database URL: {app_config.database_url}")
    print(f"   Debug mode: {app_config.debug}")
    print(f"   Log level: {app_config.log_level}")
    print(f"   Max connections: {app_config.max_connections}")

    print("\\n3. Advanced configuration management:")

    config_mgr = ConfigManager()

    # Create sample config file
    config_file = "sample_app.ini"
    config_mgr.create_sample_config(config_file)
    config_mgr.load_from_file(config_file)

    # Get configuration values
    db_url = config_mgr.get('url', 'database', 'sqlite:///default.db')
    api_key = config_mgr.get('key', 'api', 'no-key')
    log_level = config_mgr.get('level', 'logging', 'WARNING')

    print(f"   Database URL from config: {db_url}")
    print(f"   API key from config: {api_key[:10]}...")
    print(f"   Log level from config: {log_level}")

    print("\\n4. Security considerations:")

    # Generate secure random values
    secret_key = secrets.token_hex(32)
    api_token = secrets.token_urlsafe(32)

    print(f"   Generated secret key: {secret_key[:16]}...")
    print(f"   Generated API token: {api_token[:16]}...")

    # Hash sensitive data
    password = "user_password"
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), b'salt', 100000)

    print(f"   Password hash: {password_hash.hex()[:32]}...")

    print("\\n5. Configuration best practices:")
    print("   ✅ Use environment variables for sensitive data")
    print("   ✅ Provide sensible defaults")
    print("   ✅ Validate configuration values")
    print("   ✅ Separate development and production configs")
    print("   ✅ Never commit secrets to version control")
    print("   ✅ Use proper secret management systems in production")

    # Clean up
    try:
        os.remove(config_file)
        print(f"   🧹 Cleaned up {config_file}")
    except:
        pass


def main():
    """Main function demonstrating all advanced topics"""
    print("🚀 ADVANCED PYTHON TOPICS TUTORIAL")
    print("This tutorial covers regex, databases, logging, configuration, and more.")

    demonstrate_regex_basics()

    # Demonstrate regex processor
    print("\\n5. Advanced Regex Processing:")
    processor = RegexProcessor()

    sample_text = """
    Contact information:
    - Email: john@example.com, support@company.org
    - Phone: +1-555-123-4567, (555) 987-6543
    - Website: https://example.com, http://company.org/about
    - Server IP: 192.168.1.1, 10.0.0.5
    """

    emails = processor.extract_emails(sample_text)
    urls = processor.extract_urls(sample_text)
    phones = processor.extract_phones(sample_text)
    ips = processor.extract_ips(sample_text)

    print(f"   Emails found: {emails}")
    print(f"   URLs found: {urls}")
    print(f"   Phones found: {phones}")
    print(f"   IPs found: {ips}")

    cleaned = processor.clean_text("  This   is  messy    text!!!  @#$%  ")
    print(f"   Cleaned text: '{cleaned}'")

    demonstrate_database_operations()
    demonstrate_logging_and_debugging()
    demonstrate_environment_and_config()

    print("\\n" + "=" * 60)
    print("ADVANCED TOPICS TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\\n💡 Key Advanced Concepts:")
    print("- Regular expressions for pattern matching and text processing")
    print("- Database operations with SQLite and ORMs")
    print("- Comprehensive logging and debugging techniques")
    print("- Environment variables and configuration management")
    print("- Security considerations and best practices")

    print("\\n🛠️ Essential Libraries:")
    print("- re: Regular expressions")
    print("- sqlite3: SQLite database")
    print("- logging: Logging framework")
    print("- os: Operating system interface")
    print("- configparser: Configuration file parsing")
    print("- secrets: Cryptographically strong random numbers")
    print("- hashlib: Secure hash and message digest algorithms")

    print("\\n📚 Next Steps:")
    print("- Learn about web scraping with BeautifulSoup")
    print("- Explore API development with FastAPI/Flask")
    print("- Study containerization with Docker")
    print("- Learn about testing strategies and frameworks")
    print("- Explore deployment and DevOps practices")


if __name__ == "__main__":
    main()