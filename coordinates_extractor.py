import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from tqdm import tqdm
tqdm.pandas()

df = pd.read_csv('toto2.csv')  # Replace with the path to your file

geolocator = Nominatim(user_agent="geoapiExercises")

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def get_lat_lon(location):
    try:
        loc = geocode(location)
        if loc:
            return loc.latitude, loc.longitude
        else:
            return None, None
    except:
        return None, None


df['Latitude'], df['Longitude'] = zip(*df['Outlet'].progress_apply(get_lat_lon))


df.to_csv('toto_complete.csv', index=False)

print("Data with latitude and longitude saved as 'toto_complete.csv'")
