# Create a Data Pipeline with Pandas

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Build a reusable ETL pipeline to load, clean, transform, and export data using Pandas.

## The Pipeline

```
Raw Data → Load → Clean → Transform → Validate → Export
```

## Step 1: Load Data from Multiple Sources

```python
import pandas as pd

# CSV
df_csv = pd.read_csv("data/raw/sensors.csv")

# Excel
df_excel = pd.read_excel("data/raw/metadata.xlsx", sheet_name="Sheet1")

# JSON
df_json = pd.read_json("data/raw/api_response.json")

# SQL
from sqlalchemy import create_engine
engine = create_engine("mysql://user:pass@localhost/db")
df_sql = pd.read_sql("SELECT * FROM readings", engine)
```

## Step 2: Clean

```python
def clean_dataframe(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df["temperature"] = df["temperature"].fillna(df["temperature"].median())
    df = df.dropna(subset=["timestamp", "sensor_id"])  # Required fields
    
    # Fix data types
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["sensor_id"] = df["sensor_id"].astype(str)
    
    # Remove outliers (values beyond 3 std deviations)
    for col in ["temperature", "humidity"]:
        mean, std = df[col].mean(), df[col].std()
        df = df[(df[col] >= mean - 3*std) & (df[col] <= mean + 3*std)]
    
    return df
```

## Step 3: Transform

```python
def transform_dataframe(df):
    # Aggregate by hour
    df["hour"] = df["timestamp"].dt.floor("H")
    hourly = df.groupby(["sensor_id", "hour"]).agg(
        avg_temp=("temperature", "mean"),
        avg_humidity=("humidity", "mean"),
        readings_count=("temperature", "count")
    ).reset_index()
    
    return hourly
```

## Step 4: Validate and Export

```python
def validate_and_export(df, output_path):
    assert len(df) > 0, "DataFrame is empty"
    assert df.isnull().sum().sum() == 0, "Null values remain"
    
    df.to_csv(output_path, index=False)
    print(f"Exported {len(df)} rows to {output_path}")

# Run the pipeline
df = pd.read_csv("data/raw/sensors.csv")
df = clean_dataframe(df)
df = transform_dataframe(df)
validate_and_export(df, "data/processed/hourly_readings.csv")
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
