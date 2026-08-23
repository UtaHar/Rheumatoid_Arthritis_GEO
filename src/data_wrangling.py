import pandas as pd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
geopy.geocoders.options.default_timeout = None

def get_df():
    print("reading data csv")
    meta = pd.read_csv('../data/GBD-DATA-INPUT-SOURCES-1.zip')
    #pd.set_option('display.max_columns',None)
    #print(meta.head(2))
    #print(meta.tail(2))
    #print(meta.info())
    #print(meta.describe().T)

    print("dropping NA")
    meta.dropna(subset=['Location'])

    print("finding unique citation, location pairs")
    df = meta[['Citation', 'Location']].drop_duplicates().reset_index(drop=True)

    print("finding locations on map")
    geolocator = Nominatim(user_agent='RA_project')
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    df['name'] = df['Location'].apply(geocode)

    print("formatting data")
    df['point'] = df['name'].apply(lambda loc: tuple(loc.point) if loc else None)
    df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)

    print("dropping location NAs")
    df.dropna(subset=['altitude'])

    #GPS_meta = meta.set_index('Location').join(df.set_index('Location'))

    #with pd.option_context("display.max_rows",10):
    #    print(df)

    #return GPS_meta
    print("returning data frame")
    return df
