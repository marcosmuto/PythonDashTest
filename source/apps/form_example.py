from flask import Flask
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State

from app import app
from apps import formDAO

layout = html.Div([
    html.H3('Form Example'),

    dcc.Link('See All', href='/apps/list_data'),
    
    html.Label('Name'),
    dcc.Input(id='app_form_name', value='', type='text'),
    html.Br(),

    html.Label('City'),
    dcc.Dropdown(
        id='app_form_city',
        options=[{'label': formDAO.states[id], 'value': id} for id in formDAO.states]
    ),
    html.Br(),

    html.Label('Gender'),
    dcc.RadioItems(
        id='app_form_gender',
        options=[{'label': formDAO.genders[id], 'value': id} for id in formDAO.genders]
    ),
    html.Br(),

    html.Label('Programming Language'),
    dcc.Dropdown(
        id='app_form_lang',
        options=[{'label': formDAO.languages[id], 'value': id} for id in formDAO.languages],
        multi=True
    ),
    html.Br(),

    html.Div(id='form_place_holder'),

    html.Button(id='submit-button', n_clicks=0, children='Submit')

], style={'columnCount': 1})

@app.callback(
    Output('form_place_holder', 'children'),
    Input('submit-button', 'n_clicks'),
    State('app_form_name', 'value'),
    State('app_form_city', 'value'),
    State('app_form_gender', 'value'),
    State('app_form_lang', 'value')
    )
def display_form_value(n_clicks, app_form_name, app_form_city, app_form_gender, app_form_lang):
    print("Name: {}, City: {}, Gender: {}, Language: {}".format(
        app_form_name, app_form_city, app_form_gender, app_form_lang
    ))

    if app_form_name == '':
        return ''
    else:
        message = formDAO.add_data(app_form_name, app_form_city, 
            app_form_gender, '|'.join(app_form_lang))

        if message == 'OK':
            return dcc.Location(pathname='/apps/list_data', id='redirect_to_list')
        else:
            return message
            

