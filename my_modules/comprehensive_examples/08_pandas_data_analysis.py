"""
Comprehensive Pandas Data Analysis Tutorial
==========================================

This module provides complete coverage of pandas library for data analysis:
- DataFrames and Series fundamentals
- Data loading, cleaning, and preprocessing
- Data manipulation and transformation
- Aggregation, grouping, and statistical analysis
- Handling big data with pandas
- Performance optimization techniques
- Real-world data analysis examples
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import json
import sqlite3
import io
import os
import time

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set pandas display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)


class PandasBasics:
    """Fundamental pandas concepts and operations"""

    def __init__(self):
        print("🐼 PANDAS FUNDAMENTALS")
        print("=" * 60)

    def series_basics(self):
        """Comprehensive Series operations"""
        print("\\n1. PANDAS SERIES - 1D Data Structure")
        print("-" * 40)

        # Creating Series
        print("\\nCreating Series:")

        # From list
        numbers = pd.Series([1, 2, 3, 4, 5], name='numbers')
        print(f"From list:\\n{numbers}\\n")

        # From dictionary
        scores = pd.Series({'Alice': 95, 'Bob': 87, 'Charlie': 92, 'Diana': 89})
        print(f"From dictionary:\\n{scores}\\n")

        # From numpy array with custom index
        temperatures = pd.Series(np.random.normal(25, 5, 7),
                               index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                               name='Temperature')
        print(f"From numpy with custom index:\\n{temperatures.round(1)}\\n")

        # Series operations
        print("\\nSeries Operations:")
        print(f"Mean: {scores.mean():.2f}")
        print(f"Standard deviation: {scores.std():.2f}")
        print(f"Maximum: {scores.max()}")
        print(f"Index of maximum: {scores.idxmax()}")

        # Boolean indexing
        high_scores = scores[scores > 90]
        print(f"\\nHigh scores (>90):\\n{high_scores}")

        # String operations
        names = pd.Series(['john doe', 'jane smith', 'bob johnson'])
        print(f"\\nString operations:")
        print(f"Capitalized: {names.str.title().tolist()}")
        print(f"Length: {names.str.len().tolist()}")

        return scores

    def dataframe_basics(self):
        """Comprehensive DataFrame operations"""
        print("\\n2. PANDAS DATAFRAME - 2D Data Structure")
        print("-" * 40)

        # Creating DataFrames
        print("\\nCreating DataFrames:")

        # From dictionary
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
            'Age': [25, 30, 35, 28, 32],
            'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
            'Salary': [70000, 80000, 75000, 85000, 78000],
            'Department': ['IT', 'Finance', 'IT', 'HR', 'Finance']
        }
        df = pd.DataFrame(data)
        print(f"From dictionary:\\n{df}\\n")

        # DataFrame info
        print("\\nDataFrame Information:")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print(f"Data types:\\n{df.dtypes}\\n")

        # Basic statistics
        print("\\nBasic Statistics:")
        print(df.describe())

        # Selecting data
        print("\\n\\nSelecting Data:")
        print(f"Single column:\\n{df['Name'].tolist()}")
        print(f"\\nMultiple columns:\\n{df[['Name', 'Salary']].head(3)}")
        print(f"\\nRow by index:\\n{df.iloc[0]}")
        print(f"\\nRows by condition:\\n{df[df['Age'] > 30]}")

        return df

    def data_indexing_and_selection(self, df):
        """Advanced indexing and selection techniques"""
        print("\\n3. ADVANCED INDEXING AND SELECTION")
        print("-" * 40)

        # loc and iloc
        print("\\n.loc (label-based) vs .iloc (position-based):")
        print(f"df.loc[0, 'Name']: {df.loc[0, 'Name']}")
        print(f"df.iloc[0, 0]: {df.iloc[0, 0]}")

        # Boolean indexing
        print("\\nBoolean Indexing:")
        high_salary = df.loc[df['Salary'] > 75000, ['Name', 'Salary']]
        print(f"High salary employees:\\n{high_salary}")

        # Query method
        print("\\nUsing query method:")
        it_employees = df.query("Department == 'IT' and Age > 25")
        print(f"IT employees over 25:\\n{it_employees[['Name', 'Age', 'Department']]}")

        # isin method
        print("\\nUsing isin method:")
        cities_filter = df[df['City'].isin(['New York', 'London'])]
        print(f"Employees in NY or London:\\n{cities_filter[['Name', 'City']]}")

        # String contains
        df_with_emails = df.copy()
        df_with_emails['Email'] = [f"{name.lower().replace(' ', '.')}@company.com"
                                 for name in df_with_emails['Name']]
        gmail_users = df_with_emails[df_with_emails['Email'].str.contains('gmail')]
        print(f"\\nEmails containing 'gmail': {len(gmail_users)}")


class DataLoadingAndCleaning:
    """Data loading and cleaning techniques"""

    def __init__(self):
        print("\\n\\n🧹 DATA LOADING AND CLEANING")
        print("=" * 60)

    def create_sample_data(self):
        """Create sample datasets for demonstration"""
        print("\\n1. CREATING SAMPLE DATASETS")
        print("-" * 40)

        # Sales data
        np.random.seed(42)
        dates = pd.date_range('2023-01-01', periods=365, freq='D')

        sales_data = pd.DataFrame({
            'Date': dates,
            'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Watch'], 365),
            'Region': np.random.choice(['North', 'South', 'East', 'West'], 365),
            'Sales_Amount': np.random.normal(1000, 300, 365).round(2),
            'Units_Sold': np.random.poisson(10, 365),
            'Customer_ID': np.random.randint(1000, 9999, 365)
        })

        # Add some missing values intentionally
        sales_data.loc[np.random.choice(sales_data.index, 20), 'Sales_Amount'] = np.nan
        sales_data.loc[np.random.choice(sales_data.index, 15), 'Region'] = np.nan

        print(f"Sales data created: {sales_data.shape}")
        print(f"Sample data:\\n{sales_data.head()}\\n")

        # Customer data
        customer_data = pd.DataFrame({
            'Customer_ID': range(1000, 2000),
            'Name': [f'Customer_{i}' for i in range(1000)],
            'Age': np.random.randint(18, 80, 1000),
            'Gender': np.random.choice(['M', 'F'], 1000),
            'City': np.random.choice(['NYC', 'LA', 'Chicago', 'Houston'], 1000),
            'Join_Date': pd.date_range('2020-01-01', periods=1000, freq='D')[:1000]
        })

        print(f"Customer data created: {customer_data.shape}")

        return sales_data, customer_data

    def data_cleaning_techniques(self, sales_data):
        """Comprehensive data cleaning techniques"""
        print("\\n2. DATA CLEANING TECHNIQUES")
        print("-" * 40)

        print("\\nOriginal data info:")
        print(f"Shape: {sales_data.shape}")
        print(f"Missing values:\\n{sales_data.isnull().sum()}")
        print(f"Data types:\\n{sales_data.dtypes}\\n")

        # Handle missing values
        print("\\nHandling Missing Values:")

        # Fill missing regions with mode
        mode_region = sales_data['Region'].mode()[0]
        sales_data['Region'] = sales_data['Region'].fillna(mode_region)
        print(f"Filled missing regions with mode: {mode_region}")

        # Fill missing sales with mean
        mean_sales = sales_data['Sales_Amount'].mean()
        sales_data['Sales_Amount'] = sales_data['Sales_Amount'].fillna(mean_sales)
        print(f"Filled missing sales with mean: {mean_sales:.2f}")

        # Remove duplicates
        initial_shape = sales_data.shape
        sales_data = sales_data.drop_duplicates()
        print(f"Removed duplicates: {initial_shape[0]} -> {sales_data.shape[0]} rows")

        # Data type conversion
        sales_data['Date'] = pd.to_datetime(sales_data['Date'])
        sales_data['Customer_ID'] = sales_data['Customer_ID'].astype(str)
        print("\\nConverted data types:")
        print(f"Date: {sales_data['Date'].dtype}")
        print(f"Customer_ID: {sales_data['Customer_ID'].dtype}")

        # Create new features
        sales_data['Year'] = sales_data['Date'].dt.year
        sales_data['Month'] = sales_data['Date'].dt.month
        sales_data['DayOfWeek'] = sales_data['Date'].dt.dayofweek
        sales_data['Revenue'] = sales_data['Sales_Amount'] * sales_data['Units_Sold']

        print("\\nNew features created: Year, Month, DayOfWeek, Revenue")

        # Outlier detection and handling
        Q1 = sales_data['Sales_Amount'].quantile(0.25)
        Q3 = sales_data['Sales_Amount'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = sales_data[(sales_data['Sales_Amount'] < lower_bound) |
                            (sales_data['Sales_Amount'] > upper_bound)]
        print(f"\\nOutliers detected: {len(outliers)} ({len(outliers)/len(sales_data)*100:.1f}%)")

        # Cap outliers instead of removing them
        sales_data['Sales_Amount'] = sales_data['Sales_Amount'].clip(lower_bound, upper_bound)
        print("Outliers capped to reasonable bounds")

        return sales_data


class DataManipulationAndTransformation:
    """Data manipulation and transformation techniques"""

    def __init__(self):
        print("\\n\\n🔄 DATA MANIPULATION AND TRANSFORMATION")
        print("=" * 60)

    def groupby_operations(self, sales_data):
        """Comprehensive groupby operations"""
        print("\\n1. GROUPBY OPERATIONS")
        print("-" * 40)

        # Basic groupby
        print("\\nBasic GroupBy Operations:")
        product_summary = sales_data.groupby('Product').agg({
            'Sales_Amount': ['count', 'sum', 'mean'],
            'Units_Sold': 'sum',
            'Revenue': 'sum'
        }).round(2)

        # Flatten column names
        product_summary.columns = ['_'.join(col).strip() for col in product_summary.columns]
        product_summary = product_summary.rename(columns={
            'Sales_Amount_count': 'Transaction_Count',
            'Sales_Amount_sum': 'Total_Sales',
            'Sales_Amount_mean': 'Avg_Sales',
            'Units_Sold_sum': 'Total_Units',
            'Revenue_sum': 'Total_Revenue'
        })

        print(f"Product Summary:\\n{product_summary}")

        # Multiple grouping
        print("\\n\\nMultiple Grouping (Product + Region):")
        region_product = sales_data.groupby(['Product', 'Region'])['Revenue'].sum().unstack(fill_value=0)
        print(f"Revenue by Product and Region:\\n{region_product}")

        # Time-based grouping
        print("\\n\\nTime-based Grouping:")
        monthly_sales = sales_data.groupby([sales_data['Date'].dt.to_period('M')])['Revenue'].sum()
        print(f"Monthly sales (first 6 months):\\n{monthly_sales.head(6)}")

        # Custom aggregation
        def revenue_stats(x):
            return pd.Series({
                'min_revenue': x.min(),
                'max_revenue': x.max(),
                'avg_revenue': x.mean(),
                'std_revenue': x.std()
            })

        custom_agg = sales_data.groupby('Region')['Revenue'].apply(revenue_stats).round(2)
        print(f"\\nCustom aggregation by Region:\\n{custom_agg}")

        return product_summary

    def data_merging_and_joining(self, sales_data, customer_data):
        """Data merging and joining operations"""
        print("\\n2. DATA MERGING AND JOINING")
        print("-" * 40)

        # Convert Customer_ID to string for proper joining
        customer_data['Customer_ID'] = customer_data['Customer_ID'].astype(str)

        # Inner join
        print("\\nInner Join (sales with customer data):")
        merged_inner = pd.merge(sales_data, customer_data, on='Customer_ID', how='inner')
        print(f"Inner join result: {merged_inner.shape}")
        print(f"Sample merged data:\\n{merged_inner[['Date', 'Product', 'Name', 'Age', 'City']].head(3)}")

        # Left join
        print("\\nLeft Join (all sales records):")
        merged_left = pd.merge(sales_data, customer_data, on='Customer_ID', how='left')
        print(f"Left join result: {merged_left.shape}")
        missing_customers = merged_left['Name'].isnull().sum()
        print(f"Sales records without customer data: {missing_customers}")

        # Concatenation
        print("\\nConcatenation:")
        df1 = sales_data.head(100)
        df2 = sales_data.tail(100)
        concatenated = pd.concat([df1, df2], ignore_index=True)
        print(f"Concatenated shape: {concatenated.shape}")

        return merged_inner

    def pivot_operations(self, sales_data):
        """Pivot table operations"""
        print("\\n3. PIVOT OPERATIONS")
        print("-" * 40)

        # Basic pivot table
        print("\\nBasic Pivot Table:")
        pivot_basic = sales_data.pivot_table(
            values='Revenue',
            index='Product',
            columns='Region',
            aggfunc='sum',
            fill_value=0
        ).round(0)
        print(f"Revenue by Product and Region:\\n{pivot_basic}")

        # Multi-level pivot
        print("\\n\\nMulti-level Pivot:")
        pivot_multi = sales_data.pivot_table(
            values=['Revenue', 'Units_Sold'],
            index='Product',
            columns='Region',
            aggfunc={'Revenue': 'sum', 'Units_Sold': 'mean'},
            fill_value=0
        ).round(2)
        print(f"Multi-metric pivot (showing first 2 products):\\n{pivot_multi.head(2)}")

        # Time-based pivot
        sales_data['Month_Name'] = sales_data['Date'].dt.month_name()
        monthly_pivot = sales_data.pivot_table(
            values='Revenue',
            index='Product',
            columns='Month_Name',
            aggfunc='sum',
            fill_value=0
        ).round(0)
        print(f"\\nMonthly Revenue Pivot (first 3 months):")
        print(monthly_pivot.iloc[:, :3])

        return pivot_basic


class AdvancedDataAnalysis:
    """Advanced data analysis techniques"""

    def __init__(self):
        print("\\n\\n📊 ADVANCED DATA ANALYSIS")
        print("=" * 60)

    def statistical_analysis(self, merged_data):
        """Statistical analysis and insights"""
        print("\\n1. STATISTICAL ANALYSIS")
        print("-" * 40)

        # Correlation analysis
        print("\\nCorrelation Analysis:")
        numeric_cols = ['Sales_Amount', 'Units_Sold', 'Revenue', 'Age']
        correlation_matrix = merged_data[numeric_cols].corr().round(3)
        print(f"Correlation Matrix:\\n{correlation_matrix}")

        # Distribution analysis
        print("\\n\\nDistribution Analysis:")
        print(f"Revenue Statistics:\\n{merged_data['Revenue'].describe()}")

        # Percentiles
        percentiles = [10, 25, 50, 75, 90, 95, 99]
        revenue_percentiles = merged_data['Revenue'].quantile([p/100 for p in percentiles])
        print(f"\\nRevenue Percentiles:")
        for p, value in zip(percentiles, revenue_percentiles):
            print(f"  {p}th percentile: ${value:,.2f}")

        # Skewness and Kurtosis
        print(f"\\nRevenue Skewness: {merged_data['Revenue'].skew():.3f}")
        print(f"Revenue Kurtosis: {merged_data['Revenue'].kurtosis():.3f}")

        return correlation_matrix

    def time_series_analysis(self, sales_data):
        """Time series analysis"""
        print("\\n2. TIME SERIES ANALYSIS")
        print("-" * 40)

        # Daily time series
        daily_sales = sales_data.groupby('Date')['Revenue'].sum().reset_index()
        daily_sales.set_index('Date', inplace=True)

        print("\\nDaily Sales Time Series:")
        print(f"Period: {daily_sales.index.min()} to {daily_sales.index.max()}")
        print(f"Total days: {len(daily_sales)}")

        # Rolling statistics
        daily_sales['7_day_avg'] = daily_sales['Revenue'].rolling(window=7).mean()
        daily_sales['30_day_avg'] = daily_sales['Revenue'].rolling(window=30).mean()

        print("\\nRolling Averages (last 5 days):")
        print(daily_sales[['Revenue', '7_day_avg', '30_day_avg']].tail().round(2))

        # Trend analysis
        daily_sales['trend'] = daily_sales['Revenue'].rolling(window=30, center=True).mean()
        print(f"\\nTrend Analysis:")
        print(f"Overall trend (first vs last 30 days):")
        first_month_avg = daily_sales['Revenue'].head(30).mean()
        last_month_avg = daily_sales['Revenue'].tail(30).mean()
        trend_change = ((last_month_avg - first_month_avg) / first_month_avg) * 100
        print(f"  First 30 days average: ${first_month_avg:,.2f}")
        print(f"  Last 30 days average: ${last_month_avg:,.2f}")
        print(f"  Trend change: {trend_change:+.1f}%")

        # Seasonality
        daily_sales['DayOfWeek'] = daily_sales.index.dayofweek
        daily_sales['Month'] = daily_sales.index.month

        weekly_pattern = daily_sales.groupby('DayOfWeek')['Revenue'].mean()
        monthly_pattern = daily_sales.groupby('Month')['Revenue'].mean()

        print(f"\\nWeekly Pattern (0=Monday, 6=Sunday):")
        for day, revenue in weekly_pattern.items():
            day_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][day]
            print(f"  {day_name}: ${revenue:,.2f}")

        return daily_sales

    def cohort_analysis(self, merged_data):
        """Customer cohort analysis"""
        print("\\n3. COHORT ANALYSIS")
        print("-" * 40)

        # Prepare cohort data
        cohort_data = merged_data.copy()
        cohort_data['Order_Period'] = cohort_data['Date'].dt.to_period('M')
        cohort_data['Cohort_Group'] = cohort_data.groupby('Customer_ID')['Date'].transform('min').dt.to_period('M')

        # Calculate period number
        def get_date_int(df, column):
            year = df[column].dt.year
            month = df[column].dt.month
            return year * 12 + month

        cohort_data['period_number'] = (
            get_date_int(cohort_data, 'Order_Period') -
            get_date_int(cohort_data, 'Cohort_Group')
        )

        # Cohort table
        cohort_table = cohort_data.groupby(['Cohort_Group', 'period_number'])['Customer_ID'].nunique().reset_index()
        cohort_sizes = cohort_data.groupby('Cohort_Group')['Customer_ID'].nunique()

        cohort_table = cohort_table.pivot(index='Cohort_Group', columns='period_number', values='Customer_ID')

        # Calculate retention rates
        cohort_table = cohort_table.divide(cohort_sizes, axis=0)

        print("Customer Retention Rates (first 6 periods):")
        print(cohort_table.iloc[:6, :7].round(3))

        return cohort_table


class BigDataHandling:
    """Handling big data with pandas"""

    def __init__(self):
        print("\\n\\n🚀 HANDLING BIG DATA WITH PANDAS")
        print("=" * 60)

    def memory_optimization(self):
        """Memory optimization techniques"""
        print("\\n1. MEMORY OPTIMIZATION")
        print("-" * 40)

        # Create a large dataset
        n_rows = 100000
        print(f"Creating dataset with {n_rows:,} rows...")

        large_df = pd.DataFrame({
            'id': range(n_rows),
            'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
            'value': np.random.randn(n_rows),
            'date': pd.date_range('2023-01-01', periods=n_rows, freq='H'),
            'flag': np.random.choice([True, False], n_rows)
        })

        # Memory usage before optimization
        memory_before = large_df.memory_usage(deep=True).sum() / 1024**2  # MB
        print(f"Memory usage before optimization: {memory_before:.2f} MB")
        print(f"Data types:\\n{large_df.dtypes}")

        # Optimize data types
        print("\\nOptimizing data types...")

        # Convert category to categorical
        large_df['category'] = large_df['category'].astype('category')

        # Downcast numeric types
        large_df['id'] = pd.to_numeric(large_df['id'], downcast='integer')
        large_df['value'] = pd.to_numeric(large_df['value'], downcast='float')

        # Memory usage after optimization
        memory_after = large_df.memory_usage(deep=True).sum() / 1024**2  # MB
        print(f"Memory usage after optimization: {memory_after:.2f} MB")
        print(f"Memory saved: {memory_before - memory_after:.2f} MB ({(1 - memory_after/memory_before)*100:.1f}%)")
        print(f"Optimized data types:\\n{large_df.dtypes}")

        return large_df

    def chunked_processing(self):
        """Process large files in chunks"""
        print("\\n2. CHUNKED PROCESSING")
        print("-" * 40)

        # Create a large CSV file for demonstration
        large_file = 'large_dataset.csv'

        print(f"Creating large CSV file: {large_file}")
        n_rows = 50000
        chunk_data = pd.DataFrame({
            'transaction_id': range(n_rows),
            'customer_id': np.random.randint(1000, 9999, n_rows),
            'amount': np.random.exponential(100, n_rows).round(2),
            'category': np.random.choice(['Food', 'Transport', 'Shopping', 'Entertainment'], n_rows),
            'date': pd.date_range('2023-01-01', periods=n_rows, freq='min')
        })
        chunk_data.to_csv(large_file, index=False)

        # Process in chunks
        print(f"\\nProcessing {large_file} in chunks...")
        chunk_size = 10000
        total_amount = 0
        category_counts = {}
        chunk_count = 0

        for chunk in pd.read_csv(large_file, chunksize=chunk_size):
            chunk_count += 1

            # Process each chunk
            total_amount += chunk['amount'].sum()

            # Count categories
            chunk_categories = chunk['category'].value_counts()
            for category, count in chunk_categories.items():
                category_counts[category] = category_counts.get(category, 0) + count

            print(f"  Processed chunk {chunk_count}: {len(chunk)} rows")

        print(f"\\nProcessing complete:")
        print(f"Total amount: ${total_amount:,.2f}")
        print(f"Category distribution:")
        for category, count in category_counts.items():
            print(f"  {category}: {count:,} transactions")

        # Clean up
        os.remove(large_file)
        print(f"\\nCleaned up {large_file}")

    def performance_tips(self):
        """Performance optimization tips"""
        print("\\n3. PERFORMANCE OPTIMIZATION TIPS")
        print("-" * 40)

        # Create test data
        df = pd.DataFrame({
            'A': np.random.randn(100000),
            'B': np.random.randn(100000),
            'C': np.random.choice(['X', 'Y', 'Z'], 100000),
            'D': pd.date_range('2023-01-01', periods=100000, freq='min')
        })

        # Timing different operations
        print("\\nPerformance Comparisons:")

        # 1. vectorized vs iterative operations
        print("\\n1. Vectorized vs Iterative Operations:")

        # Slow way (iterative)
        start_time = time.time()
        slow_result = []
        for value in df['A'][:1000]:  # Just 1000 for demo
            slow_result.append(value ** 2)
        slow_time = time.time() - start_time

        # Fast way (vectorized)
        start_time = time.time()
        fast_result = df['A'] ** 2
        fast_time = time.time() - start_time

        print(f"  Iterative (1000 rows): {slow_time:.4f}s")
        print(f"  Vectorized (100000 rows): {fast_time:.4f}s")
        print(f"  Vectorized is {slow_time/fast_time*100:.0f}x faster per row!")

        # 2. Query vs Boolean indexing
        print("\\n2. Query vs Boolean Indexing:")

        start_time = time.time()
        result1 = df.query("A > 0 and C == 'X'")
        query_time = time.time() - start_time

        start_time = time.time()
        result2 = df[(df['A'] > 0) & (df['C'] == 'X')]
        boolean_time = time.time() - start_time

        print(f"  Query method: {query_time:.4f}s")
        print(f"  Boolean indexing: {boolean_time:.4f}s")
        print(f"  Results equal: {len(result1) == len(result2)}")

        # 3. Memory-efficient operations
        print("\\n3. Memory Tips:")
        print("  ✅ Use categorical data for repeated strings")
        print("  ✅ Downcast numeric types when possible")
        print("  ✅ Process data in chunks for large files")
        print("  ✅ Use vectorized operations instead of loops")
        print("  ✅ Avoid chained operations that create copies")
        print("  ✅ Use inplace=True when modifying DataFrames")
        print("  ✅ Drop unnecessary columns early in processing")

        return df


class DataVisualizationWithPandas:
    """Data visualization using pandas plotting"""

    def __init__(self):
        print("\\n\\n📈 DATA VISUALIZATION WITH PANDAS")
        print("=" * 60)

    def basic_plotting(self, sales_data):
        """Basic plotting with pandas"""
        print("\\n1. BASIC PLOTTING")
        print("-" * 40)

        # Set up plotting
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Sales Data Analysis Dashboard', fontsize=16)

        # 1. Revenue by Product (Bar plot)
        product_revenue = sales_data.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
        product_revenue.plot(kind='bar', ax=axes[0,0], color='skyblue')
        axes[0,0].set_title('Total Revenue by Product')
        axes[0,0].set_ylabel('Revenue ($)')
        axes[0,0].tick_params(axis='x', rotation=45)

        # 2. Daily Revenue Trend (Line plot)
        daily_revenue = sales_data.groupby('Date')['Revenue'].sum()
        daily_revenue.plot(kind='line', ax=axes[0,1], color='green', alpha=0.7)
        axes[0,1].set_title('Daily Revenue Trend')
        axes[0,1].set_ylabel('Revenue ($)')

        # 3. Revenue Distribution (Histogram)
        sales_data['Revenue'].plot(kind='hist', bins=50, ax=axes[1,0], color='orange', alpha=0.7)
        axes[1,0].set_title('Revenue Distribution')
        axes[1,0].set_xlabel('Revenue ($)')
        axes[1,0].set_ylabel('Frequency')

        # 4. Revenue by Region (Pie chart)
        region_revenue = sales_data.groupby('Region')['Revenue'].sum()
        region_revenue.plot(kind='pie', ax=axes[1,1], autopct='%1.1f%%', startangle=90)
        axes[1,1].set_title('Revenue by Region')
        axes[1,1].set_ylabel('')  # Remove ylabel for pie chart

        plt.tight_layout()
        plt.show()

        print("✅ Basic plots created")

    def advanced_visualization(self, merged_data):
        """Advanced visualization techniques"""
        print("\\n2. ADVANCED VISUALIZATION")
        print("-" * 40)

        # Create advanced visualizations
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Advanced Sales Analytics Dashboard', fontsize=16)

        # 1. Revenue vs Age scatter plot with color by Product
        for i, product in enumerate(merged_data['Product'].unique()):
            product_data = merged_data[merged_data['Product'] == product]
            axes[0,0].scatter(product_data['Age'], product_data['Revenue'],
                            label=product, alpha=0.6, s=30)
        axes[0,0].set_xlabel('Customer Age')
        axes[0,0].set_ylabel('Revenue ($)')
        axes[0,0].set_title('Revenue vs Customer Age by Product')
        axes[0,0].legend()
        axes[0,0].grid(True, alpha=0.3)

        # 2. Box plot of Revenue by Region
        merged_data.boxplot(column='Revenue', by='Region', ax=axes[0,1])
        axes[0,1].set_title('Revenue Distribution by Region')
        axes[0,1].set_ylabel('Revenue ($)')

        # 3. Heatmap of correlation matrix
        numeric_cols = ['Sales_Amount', 'Units_Sold', 'Revenue', 'Age']
        correlation = merged_data[numeric_cols].corr()

        im = axes[1,0].imshow(correlation, cmap='coolwarm', aspect='auto')
        axes[1,0].set_xticks(range(len(numeric_cols)))
        axes[1,0].set_yticks(range(len(numeric_cols)))
        axes[1,0].set_xticklabels(numeric_cols, rotation=45)
        axes[1,0].set_yticklabels(numeric_cols)
        axes[1,0].set_title('Correlation Heatmap')

        # Add correlation values to heatmap
        for i in range(len(numeric_cols)):
            for j in range(len(numeric_cols)):
                text = axes[1,0].text(j, i, f'{correlation.iloc[i, j]:.2f}',
                                    ha="center", va="center", color="black" if abs(correlation.iloc[i, j]) < 0.5 else "white")

        # 4. Monthly revenue trend with moving average
        monthly_data = merged_data.groupby(merged_data['Date'].dt.to_period('M'))['Revenue'].sum()
        monthly_data.plot(kind='line', ax=axes[1,1], marker='o', linewidth=2, markersize=4)

        # Add moving average
        moving_avg = monthly_data.rolling(window=3, center=True).mean()
        moving_avg.plot(kind='line', ax=axes[1,1], color='red', linewidth=2, alpha=0.7, label='3-Month Moving Average')

        axes[1,1].set_title('Monthly Revenue with Moving Average')
        axes[1,1].set_ylabel('Revenue ($)')
        axes[1,1].legend()
        axes[1,1].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        print("✅ Advanced visualizations created")


def main():
    """Main function demonstrating all pandas concepts"""
    print("🐼 COMPREHENSIVE PANDAS DATA ANALYSIS TUTORIAL")
    print("Master pandas for data manipulation, analysis, and visualization!")

    try:
        # 1. Pandas Basics
        basics = PandasBasics()
        scores = basics.series_basics()
        df = basics.dataframe_basics()
        basics.data_indexing_and_selection(df)

        # 2. Data Loading and Cleaning
        data_loader = DataLoadingAndCleaning()
        sales_data, customer_data = data_loader.create_sample_data()
        clean_sales_data = data_loader.data_cleaning_techniques(sales_data)

        # 3. Data Manipulation
        manipulator = DataManipulationAndTransformation()
        product_summary = manipulator.groupby_operations(clean_sales_data)
        merged_data = manipulator.data_merging_and_joining(clean_sales_data, customer_data)
        pivot_results = manipulator.pivot_operations(clean_sales_data)

        # 4. Advanced Analysis
        analyzer = AdvancedDataAnalysis()
        correlation_matrix = analyzer.statistical_analysis(merged_data)
        time_series_data = analyzer.time_series_analysis(clean_sales_data)
        cohort_results = analyzer.cohort_analysis(merged_data)

        # 5. Big Data Handling
        big_data_handler = BigDataHandling()
        optimized_df = big_data_handler.memory_optimization()
        big_data_handler.chunked_processing()
        performance_df = big_data_handler.performance_tips()

        # 6. Data Visualization
        try:
            visualizer = DataVisualizationWithPandas()
            print("Creating visualizations...")
            print("Note: Close plot windows to continue...")
            visualizer.basic_plotting(clean_sales_data)
            visualizer.advanced_visualization(merged_data)
        except Exception as e:
            print(f"Visualization skipped (matplotlib not available or display issues): {e}")

    except ImportError as e:
        print(f"Some libraries not available: {e}")
        print("Install missing libraries with: pip install pandas numpy matplotlib seaborn")

    print("\\n" + "=" * 60)
    print("PANDAS TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\\n💡 Key Pandas Concepts Covered:")
    print("• Series and DataFrame fundamentals")
    print("• Data loading, cleaning, and preprocessing")
    print("• GroupBy operations and aggregations")
    print("• Merging, joining, and concatenating data")
    print("• Pivot tables and data reshaping")
    print("• Statistical analysis and time series")
    print("• Memory optimization for big data")
    print("• Performance optimization techniques")
    print("• Data visualization with pandas plotting")

    print("\\n🎯 When to Use Pandas:")
    print("✅ Data analysis and exploration")
    print("✅ Data cleaning and preprocessing")
    print("✅ Statistical analysis and reporting")
    print("✅ Time series analysis")
    print("✅ Data transformation and reshaping")
    print("✅ Working with structured data (CSV, Excel, databases)")

    print("\\n🚀 Next Steps:")
    print("• Learn advanced pandas techniques (multi-indexing, custom functions)")
    print("• Explore data visualization with matplotlib, seaborn, plotly")
    print("• Study machine learning with scikit-learn")
    print("• Learn big data processing with Dask or PySpark")
    print("• Practice with real-world datasets from Kaggle")

    print("\\n🔗 Pandas Ecosystem:")
    print("• NumPy: Numerical computing foundation")
    print("• Matplotlib/Seaborn: Data visualization")
    print("• Scikit-learn: Machine learning")
    print("• Jupyter: Interactive data analysis")
    print("• Dask: Parallel computing")


if __name__ == "__main__":
    main()