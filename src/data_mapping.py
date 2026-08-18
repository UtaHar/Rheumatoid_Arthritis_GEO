import folium
import pandas as pd
from data_wrangling import get_df

#df = get_df()
#df.to_csv('../data/intermediate_df.csv',index=False)
df = (pd.read_csv('../data/intermediate_df.csv').dropna(subset="altitude")
#with pd.option_context("display.max_rows", 10):
#    print(df)
m = folium.Map(location=[df['latitude'].mean(),df['longitude'].mean()], tiles="OpenStreetMap", zoom_start=2)
for i in range(0,len(df)):
   folium.Marker(
      location=[df.iloc[i]['latitude'], df.iloc[i]['longitude']],
      popup=df.iloc[i]['Location'],
   ).add_to(m)
m.save("test.html")

