# GEE-band-value-retrieval-for-shapefiles

These scripts help in retrieving time series band values for both Sentinel 1 and 2 for multi-feature polygon shapefiles. The scripts are in text files. To use the code, the user has to go to https://code.earthengine.google.com/ and paste the script there. The repository also contains a .py file that would reorganize the time series data in a way that each feature gets one row of data. Following are the functions of the scripts. 

1. The ROI is a multi-feature polygon shapefile
2. Can retrieve band values for both Sentinel 1 SAR and Sentinel 2 TOA
3. Output is numeric values saved in a CSV file
4. The output CSV file from GEE contains multiple rows for a single feature, each row represents a specific date. For the ease of use for data analysis, it's better to have the data organized in a way that each feature has a single row
5. The data_organize.py will help in organizing the data accordingly. 
