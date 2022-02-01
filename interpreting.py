from matplotlib.pyplot import bar
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("filtered_stars.csv")

bar1 = px.bar(x = df["Star_name"], y = df["Mass"])
bar1.show()

bar2 = px.bar(x = df["Star_name"], y = df["Radius"])
bar2.show()

bar3 = px.bar(x = df["Star_name"], y = df["Distance"])
bar3.show()

bar4 = px.bar(x = df["Star_name"], y = df["Gravity"])
bar4.show()