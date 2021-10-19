from dash import html
from dash import dcc
from dash import dash_table
from dash.dependencies import Input, Output

import pandas as pd

from app import app
from apps import formDAO

# GOOD EXAMPLES TO WORK WITH DASH TABLE
# https://dash.plotly.com/datatable/interactivity

df = formDAO.get_all()

#format data to show
df = df.fillna('')
df.city = df.city.map(lambda state_id: formDAO.states[state_id] if state_id else '')
df.gender = df.gender.map(lambda gender_id: formDAO.genders[gender_id] if gender_id else '')

def get_languages(row):
    language_ids = row.languages.split('|')
    languages = []
    for id in language_ids:
        languages.append(formDAO.languages[id])
    row.languages = ", ".join(languages)
    return row
df.apply(get_languages, axis='columns')

df.columns = df.columns.map(lambda name : name.capitalize())

layout = html.Div([
    html.H3('All Data Entered in Form'),

    dash_table.DataTable(
        id='form_table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="single",
        selected_rows=[]
    ),

    html.Div('dummy')
])

@app.callback(
    Output('dummy', 'children'),
    Input('form_table', 'derived_virtual_row_ids'),
    Input('form_table', "derived_virtual_data"),
    Input('form_table', 'selected_row_ids')
)
def check_selected_rows(row_ids, rows, selected_row_ids):
    print("sdasd")
    selected_id_set = set(selected_row_ids or [])
    print(row_ids)
    print(selected_id_set)

    return ""
