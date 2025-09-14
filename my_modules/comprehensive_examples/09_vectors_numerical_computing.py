"""
Comprehensive Vectors and Numerical Computing Tutorial
=====================================================

This module covers vectors and numerical computing in Python:
- Vector fundamentals and mathematical operations
- NumPy for high-performance numerical computing
- Vector arithmetic and linear algebra
- Scientific computing with SciPy
- Performance comparison: Lists vs NumPy arrays
- Real-world applications and examples
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union, Optional
import time
import math
import random
from dataclasses import dataclass
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Try to import optional scientific libraries
try:
    import scipy.linalg
    import scipy.spatial.distance
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print("SciPy not available - some advanced features will be skipped")

try:
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("Scikit-learn not available - some ML features will be skipped")


# ============================================================================
# VECTOR FUNDAMENTALS
# ============================================================================

@dataclass
class Vector2D:
    """Simple 2D Vector class for demonstration"""
    x: float
    y: float

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def dot(self, other: 'Vector2D') -> float:
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        """Vector magnitude (length)"""
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> 'Vector2D':
        """Return normalized vector (unit vector)"""
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)

    def angle_with(self, other: 'Vector2D') -> float:
        """Angle between two vectors in radians"""
        dot_product = self.dot(other)
        magnitudes = self.magnitude() * other.magnitude()
        if magnitudes == 0:
            return 0
        return math.acos(max(-1, min(1, dot_product / magnitudes)))

    def __str__(self) -> str:
        return f"Vector2D({self.x:.3f}, {self.y:.3f})"


class VectorBasics:
    """Demonstrate basic vector concepts"""

    def __init__(self):
        print("📐 VECTOR FUNDAMENTALS")
        print("=" * 60)

    def vector_operations_basic(self):
        """Basic vector operations using custom Vector2D class"""
        print("\\n1. BASIC VECTOR OPERATIONS")
        print("-" * 40)

        # Create vectors
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1, 2)
        v3 = Vector2D(-2, 1)

        print(f"Vector v1: {v1}")
        print(f"Vector v2: {v2}")
        print(f"Vector v3: {v3}")

        # Basic operations
        print("\\nVector Arithmetic:")
        print(f"v1 + v2 = {v1 + v2}")
        print(f"v1 - v2 = {v1 - v2}")
        print(f"v1 * 2 = {v1 * 2}")

        # Vector properties
        print("\\nVector Properties:")
        print(f"v1 magnitude: {v1.magnitude():.3f}")
        print(f"v2 magnitude: {v2.magnitude():.3f}")
        print(f"v1 normalized: {v1.normalize()}")

        # Dot product and angles
        print("\\nVector Relationships:")
        dot_product = v1.dot(v2)
        angle_rad = v1.angle_with(v2)
        angle_deg = math.degrees(angle_rad)

        print(f"v1 · v2 (dot product): {dot_product:.3f}")
        print(f"Angle between v1 and v2: {angle_deg:.2f}°")

        # Check orthogonality
        if abs(v1.dot(v3)) < 1e-10:
            print(f"v1 and v3 are orthogonal (perpendicular)")
        else:
            print(f"v1 · v3 = {v1.dot(v3):.3f} (not orthogonal)")

        return [v1, v2, v3]

    def list_based_vectors(self):
        """Demonstrate vectors using Python lists (inefficient but educational)"""
        print("\\n2. VECTORS WITH PYTHON LISTS")
        print("-" * 40)

        def vector_add(v1: List[float], v2: List[float]) -> List[float]:
            return [a + b for a, b in zip(v1, v2)]

        def vector_subtract(v1: List[float], v2: List[float]) -> List[float]:
            return [a - b for a, b in zip(v1, v2)]

        def scalar_multiply(v: List[float], scalar: float) -> List[float]:
            return [scalar * x for x in v]

        def dot_product(v1: List[float], v2: List[float]) -> float:
            return sum(a * b for a, b in zip(v1, v2))

        def magnitude(v: List[float]) -> float:
            return math.sqrt(sum(x**2 for x in v))

        # 3D vectors with lists
        vector_a = [1, 2, 3]
        vector_b = [4, 5, 6]
        vector_c = [2, -1, 0]

        print(f"Vector A: {vector_a}")
        print(f"Vector B: {vector_b}")
        print(f"Vector C: {vector_c}")

        print("\\nList-based operations:")
        print(f"A + B = {vector_add(vector_a, vector_b)}")
        print(f"A - B = {vector_subtract(vector_a, vector_b)}")
        print(f"2 * A = {scalar_multiply(vector_a, 2)}")
        print(f"A · B = {dot_product(vector_a, vector_b)}")
        print(f"|A| = {magnitude(vector_a):.3f}")

        # Performance measurement
        print("\\nPerformance test (10,000 operations):")
        large_vector_1 = [random.random() for _ in range(1000)]
        large_vector_2 = [random.random() for _ in range(1000)]

        start_time = time.time()
        for _ in range(10):
            result = vector_add(large_vector_1, large_vector_2)
        list_time = time.time() - start_time

        print(f"List-based addition time: {list_time:.4f}s")

        return large_vector_1, large_vector_2, list_time


# ============================================================================
# NUMPY FOR HIGH-PERFORMANCE COMPUTING
# ============================================================================

class NumPyVectors:
    """Comprehensive NumPy vector operations"""

    def __init__(self):
        print("\\n\\n🔢 NUMPY HIGH-PERFORMANCE VECTORS")
        print("=" * 60)

    def numpy_basics(self):
        """NumPy array basics and creation"""
        print("\\n1. NUMPY ARRAY CREATION AND BASICS")
        print("-" * 40)

        # Array creation methods
        print("Array creation methods:")

        # From lists
        list_array = np.array([1, 2, 3, 4, 5])
        print(f"From list: {list_array}")
        print(f"  Shape: {list_array.shape}, Dtype: {list_array.dtype}")

        # 2D array (matrix)
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(f"\\n2D array:\\n{matrix}")
        print(f"  Shape: {matrix.shape}, Size: {matrix.size}")

        # Special arrays
        zeros = np.zeros(5)
        ones = np.ones((2, 3))
        identity = np.eye(3)
        arange = np.arange(0, 10, 2)
        linspace = np.linspace(0, 1, 5)

        print(f"\\nSpecial arrays:")
        print(f"Zeros: {zeros}")
        print(f"Ones:\\n{ones}")
        print(f"Identity:\\n{identity}")
        print(f"Arange (0 to 10, step 2): {arange}")
        print(f"Linspace (0 to 1, 5 points): {linspace}")

        # Random arrays
        np.random.seed(42)  # For reproducibility
        random_array = np.random.random(5)
        normal_array = np.random.normal(0, 1, 5)

        print(f"\\nRandom arrays:")
        print(f"Random [0,1): {random_array.round(3)}")
        print(f"Normal (μ=0, σ=1): {normal_array.round(3)}")

        return matrix

    def numpy_operations(self):
        """NumPy vector and matrix operations"""
        print("\\n2. NUMPY VECTOR OPERATIONS")
        print("-" * 40)

        # Create vectors
        v1 = np.array([1, 2, 3])
        v2 = np.array([4, 5, 6])
        v3 = np.array([2, -1, 0])

        print(f"Vector v1: {v1}")
        print(f"Vector v2: {v2}")
        print(f"Vector v3: {v3}")

        # Element-wise operations (vectorized)
        print("\\nElement-wise operations:")
        print(f"v1 + v2 = {v1 + v2}")
        print(f"v1 - v2 = {v1 - v2}")
        print(f"v1 * v2 = {v1 * v2}")  # Element-wise multiplication
        print(f"v1 / v2 = {v1 / v2}")
        print(f"v1 ** 2 = {v1 ** 2}")
        print(f"sqrt(v1) = {np.sqrt(v1).round(3)}")

        # Scalar operations
        print("\\nScalar operations:")
        print(f"3 * v1 = {3 * v1}")
        print(f"v1 + 10 = {v1 + 10}")

        # Vector products
        print("\\nVector products:")
        dot_product = np.dot(v1, v2)
        print(f"v1 · v2 (dot product) = {dot_product}")

        # Cross product (3D vectors)
        cross_product = np.cross(v1, v2)
        print(f"v1 × v2 (cross product) = {cross_product}")

        # Vector norms and distances
        print("\\nNorms and distances:")
        v1_norm = np.linalg.norm(v1)
        v2_norm = np.linalg.norm(v2)
        distance = np.linalg.norm(v1 - v2)

        print(f"||v1|| = {v1_norm:.3f}")
        print(f"||v2|| = {v2_norm:.3f}")
        print(f"Distance between v1 and v2 = {distance:.3f}")

        # Unit vectors
        v1_unit = v1 / np.linalg.norm(v1)
        print(f"v1 unit vector: {v1_unit.round(3)}")

        # Angle between vectors
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        angle_rad = np.arccos(np.clip(cos_angle, -1, 1))
        angle_deg = np.degrees(angle_rad)
        print(f"Angle between v1 and v2: {angle_deg:.2f}°")

        return v1, v2, v3

    def matrix_operations(self):
        """NumPy matrix operations"""
        print("\\n3. MATRIX OPERATIONS")
        print("-" * 40)

        # Create matrices
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        v = np.array([1, 2])

        print(f"Matrix A:\\n{A}")
        print(f"Matrix B:\\n{B}")
        print(f"Vector v: {v}")

        # Matrix operations
        print("\\nMatrix operations:")
        print(f"A + B =\\n{A + B}")
        print(f"A * B (element-wise) =\\n{A * B}")
        print(f"A @ B (matrix multiplication) =\\n{A @ B}")

        # Matrix-vector multiplication
        Av = A @ v
        print(f"\\nA @ v (matrix-vector product) = {Av}")

        # Matrix properties
        print("\\nMatrix properties:")
        det_A = np.linalg.det(A)
        trace_A = np.trace(A)
        rank_A = np.linalg.matrix_rank(A)

        print(f"det(A) = {det_A:.3f}")
        print(f"trace(A) = {trace_A}")
        print(f"rank(A) = {rank_A}")

        # Matrix inverse and solving linear systems
        if det_A != 0:
            A_inv = np.linalg.inv(A)
            print(f"\\nA^(-1) =\\n{A_inv.round(3)}")

            # Solve Ax = b
            b = np.array([5, 11])
            x = np.linalg.solve(A, b)
            print(f"\\nSolving Ax = b where b = {b}")
            print(f"x = {x}")
            print(f"Verification: A @ x = {A @ x}")

        # Eigenvalues and eigenvectors
        eigenvals, eigenvecs = np.linalg.eig(A)
        print(f"\\nEigenvalues: {eigenvals.round(3)}")
        print(f"Eigenvectors:\\n{eigenvecs.round(3)}")

        return A, B

    def performance_comparison(self, large_vector_1, large_vector_2, list_time):
        """Compare NumPy performance with Python lists"""
        print("\\n4. PERFORMANCE COMPARISON")
        print("-" * 40)

        # Convert lists to NumPy arrays
        np_vector_1 = np.array(large_vector_1)
        np_vector_2 = np.array(large_vector_2)

        print(f"Vector size: {len(large_vector_1):,} elements")

        # NumPy performance
        start_time = time.time()
        for _ in range(10):
            result = np_vector_1 + np_vector_2
        numpy_time = time.time() - start_time

        print(f"\\nPerformance comparison (10 additions):")
        print(f"Python lists: {list_time:.4f}s")
        print(f"NumPy arrays: {numpy_time:.4f}s")
        print(f"NumPy speedup: {list_time/numpy_time:.1f}x faster!")

        # Memory usage comparison
        import sys
        list_memory = sys.getsizeof(large_vector_1) + sum(sys.getsizeof(x) for x in large_vector_1)
        numpy_memory = np_vector_1.nbytes

        print(f"\\nMemory usage:")
        print(f"Python list: {list_memory:,} bytes")
        print(f"NumPy array: {numpy_memory:,} bytes")
        print(f"Memory efficiency: {list_memory/numpy_memory:.1f}x more compact!")

        # Mathematical operations performance
        print("\\nMathematical operations performance:")

        operations = {
            "Addition": lambda x, y: x + y,
            "Multiplication": lambda x, y: x * y,
            "Square root": lambda x, y: np.sqrt(x),
            "Trigonometric": lambda x, y: np.sin(x) + np.cos(y),
        }

        for op_name, op_func in operations.items():
            start_time = time.time()
            if op_name == "Square root":
                result = op_func(np_vector_1, None)
            elif op_name == "Trigonometric":
                result = op_func(np_vector_1, np_vector_2)
            else:
                result = op_func(np_vector_1, np_vector_2)
            op_time = time.time() - start_time
            print(f"  {op_name}: {op_time:.4f}s")


# ============================================================================
# ADVANCED VECTOR OPERATIONS
# ============================================================================

class AdvancedVectorOperations:
    """Advanced vector operations and applications"""

    def __init__(self):
        print("\\n\\n🎯 ADVANCED VECTOR OPERATIONS")
        print("=" * 60)

    def vector_spaces_and_projections(self):
        """Vector spaces, projections, and orthogonality"""
        print("\\n1. VECTOR SPACES AND PROJECTIONS")
        print("-" * 40)

        # Create vectors
        u = np.array([3, 4])
        v = np.array([1, 0])

        print(f"Vector u: {u}")
        print(f"Vector v: {v}")

        # Vector projection
        # proj_v(u) = (u·v / v·v) * v
        projection = (np.dot(u, v) / np.dot(v, v)) * v
        print(f"\\nProjection of u onto v: {projection}")

        # Component of u perpendicular to v
        perpendicular = u - projection
        print(f"Perpendicular component: {perpendicular}")

        # Verify orthogonality
        dot_perp = np.dot(projection, perpendicular)
        print(f"Dot product of projection and perpendicular: {dot_perp:.10f}")

        # Gram-Schmidt orthogonalization
        print("\\n2. GRAM-SCHMIDT ORTHOGONALIZATION")
        print("-" * 40)

        def gram_schmidt(vectors):
            """Gram-Schmidt orthogonalization process"""
            ortho_vectors = []

            for v in vectors:
                # Start with the original vector
                u = v.copy()

                # Subtract projections onto all previous orthogonal vectors
                for ortho_v in ortho_vectors:
                    projection = (np.dot(v, ortho_v) / np.dot(ortho_v, ortho_v)) * ortho_v
                    u = u - projection

                # Normalize to get orthonormal vector
                if np.linalg.norm(u) > 1e-10:  # Avoid division by zero
                    u = u / np.linalg.norm(u)
                    ortho_vectors.append(u)

            return ortho_vectors

        # Example vectors (linearly independent)
        original_vectors = [
            np.array([1, 1, 0]),
            np.array([1, 0, 1]),
            np.array([0, 1, 1])
        ]

        orthonormal_vectors = gram_schmidt(original_vectors)

        print("Original vectors:")
        for i, v in enumerate(original_vectors):
            print(f"  v{i+1}: {v}")

        print("\\nOrthonormal vectors:")
        for i, v in enumerate(orthonormal_vectors):
            print(f"  u{i+1}: {v.round(3)}")

        # Verify orthonormality
        print("\\nVerification (dot products):")
        for i in range(len(orthonormal_vectors)):
            for j in range(len(orthonormal_vectors)):
                dot_prod = np.dot(orthonormal_vectors[i], orthonormal_vectors[j])
                print(f"  u{i+1}·u{j+1} = {dot_prod:.3f}", end="  ")
            print()

        return orthonormal_vectors

    def vector_similarity_and_distance(self):
        """Vector similarity measures and distance metrics"""
        print("\\n3. SIMILARITY MEASURES AND DISTANCE METRICS")
        print("-" * 40)

        # Create sample vectors (could represent documents, users, etc.)
        doc1 = np.array([1, 2, 0, 1, 3])  # Document word frequencies
        doc2 = np.array([0, 1, 1, 2, 1])
        doc3 = np.array([2, 3, 0, 2, 4])

        print(f"Document 1 vector: {doc1}")
        print(f"Document 2 vector: {doc2}")
        print(f"Document 3 vector: {doc3}")

        # Euclidean distance
        euclidean_12 = np.linalg.norm(doc1 - doc2)
        euclidean_13 = np.linalg.norm(doc1 - doc3)
        euclidean_23 = np.linalg.norm(doc2 - doc3)

        print(f"\\nEuclidean distances:")
        print(f"  doc1-doc2: {euclidean_12:.3f}")
        print(f"  doc1-doc3: {euclidean_13:.3f}")
        print(f"  doc2-doc3: {euclidean_23:.3f}")

        # Manhattan distance
        manhattan_12 = np.sum(np.abs(doc1 - doc2))
        manhattan_13 = np.sum(np.abs(doc1 - doc3))

        print(f"\\nManhattan distances:")
        print(f"  doc1-doc2: {manhattan_12:.3f}")
        print(f"  doc1-doc3: {manhattan_13:.3f}")

        # Cosine similarity
        def cosine_similarity(v1, v2):
            dot_product = np.dot(v1, v2)
            norms = np.linalg.norm(v1) * np.linalg.norm(v2)
            return dot_product / norms if norms != 0 else 0

        cosine_12 = cosine_similarity(doc1, doc2)
        cosine_13 = cosine_similarity(doc1, doc3)
        cosine_23 = cosine_similarity(doc2, doc3)

        print(f"\\nCosine similarities:")
        print(f"  doc1-doc2: {cosine_12:.3f}")
        print(f"  doc1-doc3: {cosine_13:.3f}")
        print(f"  doc2-doc3: {cosine_23:.3f}")

        # Interpretation
        print(f"\\nInterpretation:")
        similarities = [(cosine_12, "doc1-doc2"), (cosine_13, "doc1-doc3"), (cosine_23, "doc2-doc3")]
        similarities.sort(reverse=True)

        print(f"Most similar pair: {similarities[0][1]} (cosine = {similarities[0][0]:.3f})")
        print(f"Least similar pair: {similarities[-1][1]} (cosine = {similarities[-1][0]:.3f})")

        return [doc1, doc2, doc3]

    def dimensionality_and_pca_demo(self):
        """Dimensionality reduction demonstration"""
        print("\\n4. DIMENSIONALITY REDUCTION (PCA DEMO)")
        print("-" * 40)

        # Generate high-dimensional data with correlation
        np.random.seed(42)
        n_samples = 100

        # Create correlated 2D data
        x1 = np.random.randn(n_samples)
        x2 = 2 * x1 + 0.5 * np.random.randn(n_samples)  # Correlated with x1
        x3 = x1 + x2 + 0.3 * np.random.randn(n_samples)  # Correlated with both

        # Combine into matrix (each row is a sample)
        data = np.column_stack([x1, x2, x3])

        print(f"Original data shape: {data.shape}")
        print(f"Data statistics:")
        print(f"  Mean: {np.mean(data, axis=0).round(3)}")
        print(f"  Std:  {np.std(data, axis=0).round(3)}")

        # Center the data
        data_centered = data - np.mean(data, axis=0)

        # Compute covariance matrix
        cov_matrix = np.cov(data_centered.T)
        print(f"\\nCovariance matrix:\\n{cov_matrix.round(3)}")

        # Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

        # Sort by eigenvalues (descending)
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        print(f"\\nPrincipal components:")
        print(f"Eigenvalues: {eigenvalues.round(3)}")
        print(f"Explained variance ratio: {(eigenvalues / np.sum(eigenvalues)).round(3)}")

        # Project data onto first two principal components
        pca_data = data_centered @ eigenvectors[:, :2]

        print(f"\\nPCA-transformed data shape: {pca_data.shape}")
        print(f"Variance preserved: {np.sum(eigenvalues[:2]) / np.sum(eigenvalues):.3f}")

        return data, pca_data, eigenvalues


# ============================================================================
# REAL-WORLD APPLICATIONS
# ============================================================================

class RealWorldApplications:
    """Real-world vector applications"""

    def __init__(self):
        print("\\n\\n🌍 REAL-WORLD VECTOR APPLICATIONS")
        print("=" * 60)

    def recommendation_system_demo(self):
        """Simple recommendation system using vector similarity"""
        print("\\n1. RECOMMENDATION SYSTEM")
        print("-" * 40)

        # User-item rating matrix (rows=users, columns=items)
        # Rating scale: 0-5 (0 means not rated)
        users = ["Alice", "Bob", "Charlie", "Diana"]
        items = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]

        ratings = np.array([
            [5, 3, 0, 1, 4],  # Alice
            [4, 0, 0, 1, 4],  # Bob
            [1, 1, 0, 5, 1],  # Charlie
            [1, 0, 0, 4, 1],  # Diana
        ])

        print(f"Rating matrix (Users × Items):")
        print(f"Users: {users}")
        print(f"Items: {items}")
        print(f"Ratings:\\n{ratings}")

        # Find similar users using cosine similarity
        def find_similar_users(target_user_idx, ratings_matrix, top_k=2):
            target_ratings = ratings_matrix[target_user_idx]
            similarities = []

            for i, user_ratings in enumerate(ratings_matrix):
                if i != target_user_idx:
                    # Only consider items rated by both users
                    mask = (target_ratings > 0) & (user_ratings > 0)
                    if np.sum(mask) > 0:  # At least one common item
                        sim = np.dot(target_ratings[mask], user_ratings[mask]) / (
                            np.linalg.norm(target_ratings[mask]) * np.linalg.norm(user_ratings[mask])
                        )
                        similarities.append((i, sim))

            # Sort by similarity and return top_k
            similarities.sort(key=lambda x: x[1], reverse=True)
            return similarities[:top_k]

        # Recommend items for Alice (user 0)
        target_user = 0
        similar_users = find_similar_users(target_user, ratings)

        print(f"\\nFinding recommendations for {users[target_user]}:")
        print(f"Most similar users:")
        for user_idx, similarity in similar_users:
            print(f"  {users[user_idx]}: {similarity:.3f}")

        # Generate recommendations based on similar users
        target_ratings = ratings[target_user]
        unrated_items = np.where(target_ratings == 0)[0]

        print(f"\\nRecommendations for {users[target_user]}:")
        for item_idx in unrated_items:
            weighted_sum = 0
            similarity_sum = 0

            for user_idx, similarity in similar_users:
                user_rating = ratings[user_idx, item_idx]
                if user_rating > 0:  # User has rated this item
                    weighted_sum += similarity * user_rating
                    similarity_sum += similarity

            if similarity_sum > 0:
                predicted_rating = weighted_sum / similarity_sum
                print(f"  {items[item_idx]}: {predicted_rating:.2f}/5")

    def computer_graphics_vectors(self):
        """Vector applications in computer graphics"""
        print("\\n2. COMPUTER GRAPHICS APPLICATIONS")
        print("-" * 40)

        # 3D point transformations
        print("3D Transformations:")

        # Define a 3D point
        point = np.array([1, 2, 3, 1])  # Homogeneous coordinates
        print(f"Original point: {point[:3]}")

        # Translation matrix
        translation = np.array([
            [1, 0, 0, 5],  # Translate by (5, 3, -2)
            [0, 1, 0, 3],
            [0, 0, 1, -2],
            [0, 0, 0, 1]
        ])

        # Rotation matrix (around Z-axis, 45 degrees)
        angle = np.pi / 4  # 45 degrees in radians
        rotation_z = np.array([
            [np.cos(angle), -np.sin(angle), 0, 0],
            [np.sin(angle), np.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        # Scaling matrix
        scaling = np.array([
            [2, 0, 0, 0],  # Scale by 2x in X, 1.5x in Y, 0.5x in Z
            [0, 1.5, 0, 0],
            [0, 0, 0.5, 0],
            [0, 0, 0, 1]
        ])

        # Apply transformations
        translated = translation @ point
        rotated = rotation_z @ point
        scaled = scaling @ point
        combined = translation @ rotation_z @ scaling @ point

        print(f"After translation: {translated[:3].round(2)}")
        print(f"After rotation (45° Z): {rotated[:3].round(2)}")
        print(f"After scaling: {scaled[:3].round(2)}")
        print(f"Combined transform: {combined[:3].round(2)}")

        # Lighting calculations (Phong model demo)
        print("\\nLighting calculations:")

        # Surface normal vector
        normal = np.array([0, 0, 1])  # Surface facing up
        light_dir = np.array([1, 1, -1])  # Light coming from above-right
        light_dir = light_dir / np.linalg.norm(light_dir)  # Normalize

        # Viewer direction
        view_dir = np.array([0, 0, 1])  # Looking straight at surface

        # Diffuse lighting (Lambert)
        diffuse_intensity = max(0, np.dot(normal, light_dir))

        # Specular reflection
        reflect_dir = 2 * np.dot(normal, light_dir) * normal - light_dir
        specular_intensity = max(0, np.dot(reflect_dir, view_dir)) ** 32

        print(f"Surface normal: {normal}")
        print(f"Light direction: {light_dir.round(3)}")
        print(f"Diffuse intensity: {diffuse_intensity:.3f}")
        print(f"Specular intensity: {specular_intensity:.3f}")

    def data_science_vectors(self):
        """Vectors in data science applications"""
        print("\\n3. DATA SCIENCE APPLICATIONS")
        print("-" * 40)

        # Feature vectors for machine learning
        print("Feature vectors for classification:")

        # Sample data: [height, weight, age, income] for 6 people
        features = np.array([
            [170, 65, 25, 45000],  # Person 1
            [175, 70, 30, 55000],  # Person 2
            [165, 55, 22, 35000],  # Person 3
            [180, 80, 35, 75000],  # Person 4
            [160, 50, 20, 25000],  # Person 5
            [185, 85, 40, 85000],  # Person 6
        ])

        labels = np.array([0, 1, 0, 1, 0, 1])  # 0: Category A, 1: Category B

        print(f"Feature matrix shape: {features.shape}")
        print(f"Features (height, weight, age, income):")
        for i, (feature, label) in enumerate(zip(features, labels)):
            category = "A" if label == 0 else "B"
            print(f"  Person {i+1}: {feature} → Category {category}")

        # Feature normalization (standardization)
        features_normalized = (features - np.mean(features, axis=0)) / np.std(features, axis=0)

        print(f"\\nNormalized features:")
        print(f"Mean: {np.mean(features_normalized, axis=0).round(3)}")
        print(f"Std:  {np.std(features_normalized, axis=0).round(3)}")

        # Distance-based classification (k-nearest neighbors concept)
        new_person = np.array([172, 68, 28, 50000])
        new_person_norm = (new_person - np.mean(features, axis=0)) / np.std(features, axis=0)

        print(f"\\nClassifying new person: {new_person}")
        print(f"Normalized: {new_person_norm.round(3)}")

        # Calculate distances to all training samples
        distances = []
        for i, feature_vec in enumerate(features_normalized):
            distance = np.linalg.norm(new_person_norm - feature_vec)
            distances.append((distance, labels[i], i+1))

        # Sort by distance
        distances.sort()

        print(f"\\nNearest neighbors (k=3):")
        for i in range(min(3, len(distances))):
            dist, label, person_id = distances[i]
            category = "A" if label == 0 else "B"
            print(f"  Person {person_id}: distance={dist:.3f}, category={category}")

        # Majority vote for classification
        k = 3
        nearest_labels = [distances[i][1] for i in range(min(k, len(distances)))]
        prediction = 1 if sum(nearest_labels) > k/2 else 0
        category = "A" if prediction == 0 else "B"

        print(f"\\nPredicted category: {category}")


def main():
    """Main function demonstrating all vector concepts"""
    print("🔢 COMPREHENSIVE VECTORS AND NUMERICAL COMPUTING TUTORIAL")
    print("Master vectors, NumPy, and numerical computing in Python!")

    try:
        # 1. Vector Basics
        basics = VectorBasics()
        basic_vectors = basics.vector_operations_basic()
        large_vector_1, large_vector_2, list_time = basics.list_based_vectors()

        # 2. NumPy Vectors
        numpy_vectors = NumPyVectors()
        matrix = numpy_vectors.numpy_basics()
        v1, v2, v3 = numpy_vectors.numpy_operations()
        A, B = numpy_vectors.matrix_operations()
        numpy_vectors.performance_comparison(large_vector_1, large_vector_2, list_time)

        # 3. Advanced Operations
        advanced = AdvancedVectorOperations()
        orthonormal = advanced.vector_spaces_and_projections()
        documents = advanced.vector_similarity_and_distance()
        original_data, pca_data, eigenvalues = advanced.dimensionality_and_pca_demo()

        # 4. Real-world Applications
        applications = RealWorldApplications()
        applications.recommendation_system_demo()
        applications.computer_graphics_vectors()
        applications.data_science_vectors()

        # Optional: SciPy demonstrations
        if SCIPY_AVAILABLE:
            print("\\n\\n🔬 SCIPY EXTENSIONS")
            print("=" * 60)

            print("\\nSciPy linear algebra operations:")
            # More advanced linear algebra with SciPy
            matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])

            # LU decomposition
            P, L, U = scipy.linalg.lu(matrix)
            print(f"LU Decomposition available")

            # SVD
            U_svd, s, Vt = scipy.linalg.svd(matrix)
            print(f"SVD: singular values = {s.round(3)}")

            # Distance matrices
            points = np.random.rand(5, 2)  # 5 random 2D points
            distances = scipy.spatial.distance.pdist(points, metric='euclidean')
            distance_matrix = scipy.spatial.distance.squareform(distances)
            print(f"\\nDistance matrix shape: {distance_matrix.shape}")

        # Visualization attempt
        try:
            print("\\n\\nCreating visualizations...")
            print("Note: Close plot windows to continue...")

            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            fig.suptitle('Vector and Numerical Computing Visualizations')

            # 1. 2D vectors
            v1_2d = np.array([3, 4])
            v2_2d = np.array([1, 2])
            axes[0,0].arrow(0, 0, v1_2d[0], v1_2d[1], head_width=0.2, head_length=0.3, fc='blue', label='v1')
            axes[0,0].arrow(0, 0, v2_2d[0], v2_2d[1], head_width=0.2, head_length=0.3, fc='red', label='v2')
            axes[0,0].arrow(0, 0, (v1_2d+v2_2d)[0], (v1_2d+v2_2d)[1], head_width=0.2, head_length=0.3, fc='green', label='v1+v2')
            axes[0,0].set_xlim(-1, 6)
            axes[0,0].set_ylim(-1, 7)
            axes[0,0].grid(True)
            axes[0,0].legend()
            axes[0,0].set_title('2D Vector Addition')

            # 2. Performance comparison
            methods = ['Python Lists', 'NumPy Arrays']
            times = [list_time, list_time/50]  # Approximate NumPy speedup
            axes[0,1].bar(methods, times)
            axes[0,1].set_ylabel('Time (seconds)')
            axes[0,1].set_title('Performance Comparison')

            # 3. Eigenvalues visualization
            if 'eigenvalues' in locals():
                axes[1,0].bar(range(len(eigenvalues)), eigenvalues)
                axes[1,0].set_xlabel('Component')
                axes[1,0].set_ylabel('Eigenvalue')
                axes[1,0].set_title('Principal Component Analysis')

            # 4. Random data scatter
            if 'original_data' in locals() and 'pca_data' in locals():
                axes[1,1].scatter(pca_data[:, 0], pca_data[:, 1], alpha=0.6)
                axes[1,1].set_xlabel('First Principal Component')
                axes[1,1].set_ylabel('Second Principal Component')
                axes[1,1].set_title('PCA-Transformed Data')
                axes[1,1].grid(True, alpha=0.3)

            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Visualization skipped: {e}")

    except ImportError as e:
        print(f"Some libraries not available: {e}")
        print("Install missing libraries with: pip install numpy scipy matplotlib scikit-learn")

    print("\\n" + "=" * 60)
    print("VECTORS AND NUMERICAL COMPUTING TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\\n💡 Key Concepts Covered:")
    print("• Vector fundamentals and mathematical operations")
    print("• NumPy arrays for high-performance computing")
    print("• Matrix operations and linear algebra")
    print("• Vector spaces, projections, and orthogonality")
    print("• Similarity measures and distance metrics")
    print("• Dimensionality reduction (PCA)")
    print("• Real-world applications in ML, graphics, and data science")

    print("\\n🚀 Performance Benefits:")
    print(f"• NumPy is 50-100x faster than Python lists")
    print(f"• Vectorized operations eliminate Python loops")
    print(f"• Memory-efficient storage and operations")
    print(f"• Optimized BLAS/LAPACK libraries under the hood")

    print("\\n🛠️ Essential Libraries:")
    print("• NumPy: Fundamental numerical computing")
    print("• SciPy: Advanced scientific computing")
    print("• Matplotlib: Data visualization")
    print("• Scikit-learn: Machine learning")
    print("• Pandas: Data manipulation (built on NumPy)")

    print("\\n🎯 Use Cases:")
    print("✅ Machine learning and data science")
    print("✅ Scientific computing and simulations")
    print("✅ Computer graphics and game development")
    print("✅ Signal and image processing")
    print("✅ Financial modeling and risk analysis")
    print("✅ Recommendation systems")

    print("\\n📚 Next Steps:")
    print("• Learn advanced NumPy features (broadcasting, fancy indexing)")
    print("• Explore SciPy for specialized scientific functions")
    print("• Study linear algebra for machine learning")
    print("• Learn optimization techniques with SciPy.optimize")
    print("• Explore GPU computing with CuPy or JAX")


if __name__ == "__main__":
    main()