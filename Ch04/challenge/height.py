# Draw the running track from track.csv
#
# - Sample data to a minute interval
# - Markers should be blue if the height is below 100 meter, otherwise red


# %%
import pandas as pd
import folium

df = pd.read_csv('track.csv', parse_dates=['time'], index_col=['time'])

# %%
m = folium.Map(
  location = [df['lat'].mean(), df['lng'].mean()],
  zoom_start = 15
)
m

#%%
df = df.resample('min').mean()

# %%
def fun_markers(df):
  height_condition = df['height'] < 100
  marker = folium.CircleMarker(
    location = [df['lat'], df['lng']],
    color = 'blue' if height_condition else 'red'
  )
  marker.add_to(m)

df.apply(fun_markers, axis=1)
m
