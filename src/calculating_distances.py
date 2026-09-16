import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

coastline_path = "../data/coastlines-split-4326/lines.shp"
coast = gpd.read_file(coastline_path)
print(coast.head())

fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)
ax.set_title("Coastlines", fontsize=9)
coast.plot(ax=ax, edgecolor="red", linewidth=1.0)
ax.axis("off")
plt.show()
