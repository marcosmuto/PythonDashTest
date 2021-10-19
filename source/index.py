from dash import html
from dash import dcc
from dash.dependencies import Input, Output

from app import app
from apps import form_example, list_data, app2, stock_graph

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Nav(id='page-header', children=[
        html.Ul(style={'display': 'inline-block', 'padding': '2px 10px'}, children=[
            html.Li(style={'display': 'inline-block', 'padding': '2px 10px'}, children=[
                dcc.Link('Form Example', href='/apps/form_example')
            ]),
            html.Li(style={'display': 'inline-block', 'padding': '2px 10px'}, children=[
                dcc.Link('Go to App 2', href='/apps/app2')
            ]),
            html.Li(style={'display': 'inline-block', 'padding': '2px 10px'}, children=[
                dcc.Link('Stock Graph', href='/apps/stock_graph')
            ])
        ])
    ]),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/form_example':
        return form_example.layout
    elif pathname == '/apps/list_data':
        return list_data.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/stock_graph':
        return stock_graph.layout
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)
