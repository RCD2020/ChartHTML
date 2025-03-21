TEMPLATE = """<!DOCTYPE html>

<html>
    <head>
        <title>{title}</title>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        
        <style>

        </style>
    </head>

    <body>
        
    </body>
</html>"""


class TemplateHandler:

    def __init__(self, title='ChartApp'):
        self.title = title

    
    def write_template(self, path):

        text = TEMPLATE.format(title=self.title)

        with open(path, 'w') as f:
            f.write(text)
