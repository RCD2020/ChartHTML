from ReportManager.TemplateHandler import TemplateHandler
from ReportManager.ChartManager import (
    Scatterplot, ScatterplotDataset, AxisFormat, TooltipCallbacks
)
from ReportManager.Utilities.DateUtilities import read_date
from ReportManager.Utilities.DataUtilities import random_rgb

import csv


# test = TemplateHandler(charts=[
#     random_scatterplot(), random_scatterplot(), random_scatterplot()
# ])
# # test.format_template()
# test.write_template('out.html')

data = {}

with open('out.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row['Agent'] in data:
            data[row['Agent']].append(row['Creation Date'])
        else:
            data[row['Agent']] = [row['Creation Date']]

# print(data)

datasets = []
for agent, dates in data.items():
    label = agent
    color = random_rgb()
    plot_data = []

    for x in dates:
        date_obj = read_date(x)

        date = date_obj.strftime('"%Y-%m-%d"')
        time = date_obj.strftime('"%H:%M"')

        plot_data.append((date, time))
    
    datasets.append(ScatterplotDataset(label, color, plot_data))
    
        

plot = Scatterplot(
    datasets, AxisFormat.DATE, AxisFormat.TIME, [TooltipCallbacks.XY]
)
html = TemplateHandler(charts=[plot])
html.write_template('out.html')
