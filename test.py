import pandas as pd
from LPS import LorenzPhaseSpace


sample_file = 'sample_results.csv'
df = pd.read_csv(sample_file, parse_dates={'Datetime': ['Date', 'Hour']}, date_format='%Y-%m-%d %H')
df = df.drop(['Unnamed: 0'], axis=1)

x_axis = df['Ck']
y_axis = df['Ca']
marker_color = df['Ge']
marker_size = df['Ke']

title = 'sample'
datasource = 'sample'
start = pd.to_datetime(df['Datetime'].iloc[0]).strftime('%Y-%m-%d %H:%M')
end = pd.to_datetime(df['Datetime'].iloc[-1]).strftime('%Y-%m-%d %H:%M')

lps_mixed = LorenzPhaseSpace(x_axis, y_axis, marker_color, marker_size, title=title, datasource=datasource, start=start, end=end)
fig, ax = lps_mixed.plot()
assert fig