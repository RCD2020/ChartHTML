from ReportManager.Utilities.StringUtilities import insertSubstring


BODY = """<!DOCTYPE html>

<html>
    <head>
        <title>{{title}}</title>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        
        <style>
            #container {
                display: grid;
                height: 100vh;
                width: 100vw;
                overflow: hidden;
            }

            @media only screen and (orientation: portrait) {
                #container {
                    grid-template-columns: repeat(16, calc(100vh / 16));
                }
            }

            @media only screen and (orientation: landscape) {
                #container {
                    grid-template-columns: repeat(16, 1fr);
                }
            }

            .gridSquare {
                aspect-ratio: 1 / 1;
                background-color: black;
            }
        </style>
    </head>

    <body>
        <div id="container">{{contents}}</div>
    </body>
</html>"""


class TemplateHandler:

    def __init__(self, title='ChartApp'):
        self.title = title


    def format_template(self):
        text = BODY

        text = insertSubstring(text, '{{title}}', self.title)

        return text

    
    def write_template(self, path):

        text = self.format_template()

        with open(path, 'w') as f:
            f.write(text)
