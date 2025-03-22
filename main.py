from ReportManager.TemplateHandler import TemplateHandler
from ReportManager.ChartManager import random_scatterplot

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

print(data)
