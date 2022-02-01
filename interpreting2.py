import csv
import plotly.express as px

stars = []

Star_name = []
Mass = []
Radius = []
Distance = []
Gravity = []

with open("filtered_stars.csv") as row:
    stars.append(row)
    
    for rows in stars[1:]:
        Star_names = Star_name.append(rows[2])
        Masses = Mass.append(rows[4])
        Radiuses = Radius.append(rows[5])
        Distances = Distance.append(rows[3])
        Gravities = Gravity.append(rows[6])

        bar1 = px.bar(x = Star_names, y = Masses)
        bar1.show()

        bar2 = px.bar(x = Star_names, y = Radiuses)
        bar2.show()

        bar3 = px.bar(x = Star_names, y = Distances)
        bar3.show()

        bar4 = px.bar(x = Star_names, y = Gravities)
        bar4.show()