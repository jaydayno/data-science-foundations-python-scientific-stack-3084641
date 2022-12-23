# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data
# %%
import pandas as pd
import numpy as np
from pathlib import Path

csv_file = Path('taxi.parquet')
df = pd.read_parquet(csv_file)

# %%
df['VendorID']
# %%
df.loc[:,'trip_distance']

# %%df['tot_hour_diff'] = (df.from_date - df.to_date) / pd.Timedelta(hours=1)
mask = df['tpep_dropoff_datetime'] > df['tpep_pickup_datetime']
df = df[mask]


# %%
timeInHour = (df['tpep_dropoff_datetime'] -
                  df['tpep_pickup_datetime']) / pd.Timedelta(hours=1)
speed = df['trip_distance'] / timeInHour
# %%
speed.mean()

# %%

