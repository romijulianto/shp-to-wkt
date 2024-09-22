import geopandas as gpd
from shapely import wkt
import pandas as pd
from tqdm import tqdm

# Load the shapefile
shapefile_path = 'data/provinsi.shp'  # Sesuaikan path jika berbeda
gdf = gpd.read_file(shapefile_path)

# Function to convert GeoDataFrame to WKT without modifying geometry
def convert_shapefile_to_wkt(gdf):
    wkt_list = []
    
    for index, row in tqdm(gdf.iterrows(), total=gdf.shape[0]):
        if pd.notnull(row['geometry']):
            wkt_value = wkt.dumps(row['geometry'])  # directly convert to WKT
            wkt_list.append(wkt_value)
        else:
            wkt_list.append(None)  # handle missing geometry
    
    gdf['WKT'] = wkt_list  # Add WKT column
    return gdf

# Convert the geometries to WKT and maintain all attributes
gdf_wkt = convert_shapefile_to_wkt(gdf)

# Export to CSV without the geometry column, but with all other attributes
output_csv_path = 'data/provinsi_wktasaas.csv'
gdf_wkt_df = pd.DataFrame(gdf_wkt.drop(columns='geometry'))  # drop the geometry column
gdf_wkt_df.to_csv(output_csv_path, index=False)

print("Proses konversi selesai dan data telah disimpan ke CSV.")
