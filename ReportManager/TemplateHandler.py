from ReportManager.Utilities.StringUtilities import insertSubstring
from ReportManager.ChartManager import Chart

from typing import List


BODY = """<!DOCTYPE html>

<html>
    <head>
        <title>{{title}}</title>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        
        <style>
            #container {
                display: grid;
                width: 30%;
            }
        </style>
    </head>

    <body>
        <div id="container">{{content}}</div>
    </body>
</html>"""


class TemplateHandler:

    def __init__(self, title='ChartApp', charts: List[Chart] = []):
        self.title = title
        self.charts = charts


    def format_template(self):
        text = BODY

        text = insertSubstring(text, '{{title}}', self.title)

        charttext = ''
        for i in range(len(self.charts)):
            charttext += self.charts[i].html(i)

        text = insertSubstring(text, '{{content}}', charttext)

        return text

    
    def write_template(self, path):

        text = self.format_template()

        with open(path, 'w') as f:
            f.write(text)
