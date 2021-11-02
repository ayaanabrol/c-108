import pandas as pd 
import csv
import plotly.figure_factory as pff

df=pd.read_csv('data.csv')
fig=pff.create_distplot([df["Avg Rating"].to_list()],["AvgRating"])
fig.show()