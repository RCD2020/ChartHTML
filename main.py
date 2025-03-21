from ReportManager.TemplateHandler import TemplateHandler
from ReportManager.ChartManager import random_scatterplot


test = TemplateHandler(charts=[
    random_scatterplot(), random_scatterplot(), random_scatterplot()
])
# test.format_template()
test.write_template('out.html')