# GEE-band-value-retrieval-for-shapefiles

The provided scripts are designed to retrieve time series band values for both Sentinel-1 and Sentinel-2 datasets from multi-feature polygon shapefiles. The scripts are available as text files and can be executed by copying and pasting the code into the Google Earth Engine Code Editor at https://code.earthengine.google.com/. Additionally, the repository includes a Python file that reorganizes the time series data so that each feature is represented by a single row. The primary functionalities of these scripts include:

1. Input Data: Utilizes a multi-feature polygon shapefile as the region of interest (ROI).
2. Data Retrieval: Extracts band values from both Sentinel-1 Synthetic Aperture Radar (SAR) and Sentinel-2 Top-of-Atmosphere (TOA) datasets.
3. Output Format: Generates numeric values saved in a CSV file.
4. Data Organization: Transforms the default output—where multiple rows represent a single feature on different dates—into a format where each feature is consolidated into a single row, facilitating more efficient data analysis.
5. Data Reorganization Utility: The data_organize.py script automates the reorganization of the CSV output to meet the aforementioned data format requirements.
