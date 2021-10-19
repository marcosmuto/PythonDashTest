from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output

from app import app

df = px.data.stocks() #reading stock price dataset 

layout = html.Div([
    html.H3('Stocks Price Graph'),
    dcc.Dropdown(
        id='stocks_dropdown',
        options = [
                {'label':'Google', 'value':'GOOG' },
                {'label': 'Apple', 'value':'AAPL'},
                {'label': 'Amazon', 'value':'AMZN'},
                ],
        value = 'GOOG' 
    ),
    dcc.Graph(id = 'stocks_bar_plot')
])

@app.callback(Output(component_id='stocks_bar_plot', component_property= 'figure'),
              [Input(component_id='stocks_dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    # for debug
    print(dropdown_value)
        
    fig = go.Figure([go.Scatter(x = df['date'], y = df['{}'.format(dropdown_value)],\
                     line = dict(color = 'firebrick', width = 4))
                     ])
    
    fig.update_layout(title = 'Stock prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  
