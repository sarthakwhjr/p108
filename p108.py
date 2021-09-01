import plotly.figure_factory as pff
import csv
import pandas as pd
data=pd.read_csv("data.csv")
graph=pff.create_distplot([data["Avg Rating"].tolist()],["Avg Ratings"],show_hist=True)
graph.show()