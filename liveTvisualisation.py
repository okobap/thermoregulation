import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import random
import plotly.graph_objs as go
from collections import deque




X = deque(maxlen = 40)
X.append(1)

Y = deque(maxlen = 40)
Y.append(1)


app = dash.Dash(__name__)


app.layout = html.Div(
    [    
        dcc.Graph(id = 'live-graph',
                  animate = True),   # easily handle scroll animation for the graph
        dcc.Interval(
            id = 'graph-update',
            interval = 1000,  # time elapsed between two updations of data
            n_intervals = 0   # number of intervals completed from start of the server
        ),
    ]
)


# callback decorators 

@app.callback(
    Output('live-graph', 'figure'),
    [ Input('graph-update', 'n_intervals') ]
)




# update_graph method takes n_intervals as parameter

def update_graph_scatter(n):
    X.append(X[-1]+1)  # x axis is sequential 
    Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))  # y is random 

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
    )

    return {'data': [data],
            'layout' : go.Layout(xaxis=dict(
                    range=[min(X),max(X)]),yaxis = 
                    dict(range = [min(Y),max(Y)]),
                    )}



# run the server 

if __name__ == '__main__':
    app.run_server()