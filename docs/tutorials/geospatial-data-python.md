# Working with Geospatial Data in Python

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Load, visualize, and analyze geospatial data using GeoPandas and Folium.

## Prerequisites

- Python 3.9+

## Step 1: Install Libraries

```bash
pip install geopandas folium shapely matplotlib
```

## Step 2: Load Geospatial Data

```python
import geopandas as gpd

# Load a shapefile or GeoJSON
gdf = gpd.read_file("regions.geojson")

print(f"CRS: {gdf.crs}")
print(f"Features: {len(gdf)}")
print(gdf.head())
```

## Step 3: Visualize on a Map

```python
import folium

m = folium.Map(location=[42.8864, -78.8784], zoom_start=10)

for _, row in gdf.iterrows():
    folium.GeoJson(row.geometry, tooltip=row["name"]).add_to(m)

m.save("map.html")
```

## Step 4: Spatial Analysis

```python
# Calculate area of each region
gdf["area_km2"] = gdf.geometry.area / 1e6

# Find which region contains a point
from shapely.geometry import Point
point = Point(-78.8784, 42.8864)
containing = gdf[gdf.contains(point)]
print(f"Point is in: {containing['name'].values}")
```

## Step 5: Export Results

```python
gdf.to_file("output.geojson", driver="GeoJSON")
gdf.to_csv("output_attributes.csv", index=False)
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
