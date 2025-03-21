from typing import List, Tuple
from random import randint


class Chart:
    
    def toSetup(self) -> str:
        return 'empty chart'
    
    def toConfig(self) -> str:
        return 'empty chart'

    
    def html(self) -> str:
        text  = '<canvas id="chart"></canvas>\n'
        text += '<script>const ctx = document.getElementById("chart");\n\n'
        text += 'const data = ' + self.toSetup() + ';\n\n'
        text += 'new Chart(ctx, ' + self.toConfig() + ');</script>'

        return text


class ScatterplotDataset:

    def __init__(self, label: str, rgb: Tuple[int, int, int], data: list):
        
        self.label = label
        self.rgb   = rgb
        self.data  = data

    
    def rgb2str(self):
        return f'"rgb({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]})"'


class Scatterplot(Chart):

    def __init__(self, data: List[ScatterplotDataset]):
        self.data = data

    
    def toSetup(self):
        text = '{datasets: ['

        for x in self.data:
            text += '{ label: "' + x.label + '", data: ['

            for y in x.data:
                text += '{' + f'x: {y[0]}, y: {y[1]}' + '},'
            
            text += '], backgroundColor: ' + x.rgb2str() + '}, '
        
        text += ']}'

        return text
    
    
    def toConfig(self):
        text = (
            '{ type:"scatter", data: data, options: { scales: {'
            'x: { type: "linear", position: "bottom" }}}}'
        )

        return text
    

def random_scatterplot():
    data = [
        ScatterplotDataset('a', (255, 0, 0), [
            (randint(0, 10), randint(0, 10)) for x in range(10)
        ]),
        ScatterplotDataset('b', (0, 255, 0), [
            (randint(0, 10), randint(0, 10)) for x in range(10)
        ]),
        ScatterplotDataset('c', (0, 0, 255), [
            (randint(0, 10), randint(0, 10)) for x in range(10)
        ])
    ]

    chart = Scatterplot(data)
    return chart


if __name__ == '__main__':
    chart = random_scatterplot()
    print(chart.toSetup())