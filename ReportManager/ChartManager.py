from typing import List, Tuple
from random import randint
from enum import Enum
    

class AxisFormat(Enum):
    DATE = (
        '{type: "time", time: {unit: "day", displayFormats: {day: "'
        'yyyy-MM-dd"}}}'
    )
    TIME = (
        '{type: "time", time: {unit: "hour", parser: "HH:mm", '
        'displayFormats: {hour: "hh:mm aa"}}}'
    )

class TooltipCallbacks(Enum):
    XY = (
        'label: function(context) { let label = context.dataset.label '
        '|| ""; if (label) {label += ": " + context.raw.x + " " + '
        'context.raw.y; } return label; }'
    )


class Chart:
    
    def toSetup(self) -> str:
        return 'empty chart'
    
    def toConfig(self, id) -> str:
        return 'empty chart'

    
    def html(self, id) -> str:
        text  = f'<canvas id="chart{id}"></canvas>\n'
        text += f'<script>const ctx{id} = document.getElementById("chart{id}");\n\n'
        text += f'const data{id} = ' + self.toSetup() + ';\n\n'
        text += f'new Chart(ctx{id}, ' + self.toConfig(id) + ');</script>'

        return text


class ScatterplotDataset:

    def __init__(self, label: str, rgb: Tuple[int, int, int], data: list):
        
        self.label = label
        self.rgb   = rgb
        self.data  = data

    
    def rgb2str(self):
        return f'"rgb({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]})"'


class Scatterplot(Chart):

    def __init__(
            self,
            data: List[ScatterplotDataset],
            x_format: AxisFormat = None,
            y_format: AxisFormat = None,
            tooltipCallbacks: List[TooltipCallbacks] = []
        ):
        self.data = data
        self.x_format = x_format
        self.y_format = y_format
        self.tooltipCallbacks = tooltipCallbacks

    
    def toSetup(self):
        text = '{datasets: ['

        for x in self.data:
            text += '{ label: "' + x.label + '", data: ['

            for y in x.data:
                text += '{' + f'x: {y[0]}, y: {y[1]}' + '},'
            
            text += '], backgroundColor: ' + x.rgb2str() + '}, '
        
        text += ']}'

        return text
    
    
    def toConfig(self, id):
        text = '{ type:"scatter", data: data' + f'{id}' + ', options: {'

        if self.x_format or self.y_format:
            text += 'scales: {'

            if self.x_format:
                text += 'x: ' + self.x_format.value
            if self.y_format:
                if self.x_format:
                    text += ', '
                text += 'y: ' + self.y_format.value

            text += '},'

        if self.tooltipCallbacks:
            text += 'plugins: { tooltip: { callbacks: {'

            for x in self.tooltipCallbacks:
                text += x.value + ','
            
            text += '}}},'

        text += '}}'

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