import folium
import pandas as pd
from data_wrangling import get_df

def map_df():
    #df = get_df()
    #df.to_csv('../data/intermediate_df.csv',index=False)
    print("reading intermediate data frame")
    df = pd.read_csv('../data/intermediate_df.csv').dropna(subset="altitude")
    #with pd.option_context("display.max_columns", None):
    #    print(df)
    print("creating map")
    m = folium.Map(location=[df['latitude'].mean(),df['longitude'].mean()], tiles="OpenStreetMap", zoom_start=3)
    print("adding study locations")
    for i in range(0,len(df)):
       folium.Marker(
          location=[df.iloc[i]['latitude'], df.iloc[i]['longitude']],
          popup=df.iloc[i]['Citation'],
       ).add_to(m)
    print("saving html")
    m.save("mapped_studies.html")


