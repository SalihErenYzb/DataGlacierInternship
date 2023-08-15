import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import os
# Loading the dataset to a dataframe
df = pd.read_csv('master_data.csv')

# Initializing the Dash app
app = dash.Dash(__name__)

# Age vs. Satisfaction Rate (Scatter Plot)
fig1 = px.scatter(df, x='Age', y='Satisfaction Rate', color='Satisfaction Rate',
                  title='Age vs. Satisfaction Rate',
                  labels={'Age': 'Age', 'Satisfaction Rate': 'Satisfaction Rate'},
                  trendline='ols')  # Add a trendline for linear regression

# Country vs. Satisfaction Rate (Histogram Plot)
fig2 = px.histogram(df, x='Country', y='Satisfaction Rate', histfunc='avg',
                  title='Country vs. Satisfaction Rate',
                  labels={'Country': 'Country'})

# Education Level vs. Satisfaction Rate (histogram Plot)
fig3 = px.histogram(df, x='Education Level', y='Satisfaction Rate', histfunc='avg',
                  title='Education Level vs. Satisfaction Rate',
                  labels={'Education Level': 'Education Level', 'Satisfaction Rate': 'Satisfaction Rate'})

# Number of Languages Spoken vs. Satisfaction Rate (histogram Plot)
fig4 = px.histogram(df, x='Number of Languages Spoken', y='Satisfaction Rate',histfunc='avg',
                  title='Number of Languages Spoken vs. Satisfaction Rate',
                  labels={'Number of Languages Spoken': 'Number of Languages Spoken', 'Satisfaction Rate': 'Satisfaction Rate'})

# Gender vs. Satisfaction Rate (Scatter Plot)
fig5 = px.histogram(df, x='Gender', y='Satisfaction Rate', histfunc='avg',
                  title='Gender vs. Satisfaction Rate',
                  labels={'Gender': 'Gender', 'Satisfaction Rate': 'Satisfaction Rate'})

# Marital Status vs. Satisfaction Rate (histogram Plot)
fig6 = px.histogram(df, x='Marital Status', y='Satisfaction Rate',histfunc='avg',
                  title='Marital Status vs. Satisfaction Rate',
                  labels={'Marital Status': 'Marital Status', 'Satisfaction Rate': 'Satisfaction Rate'})

# Number of Children vs. Satisfaction Rate (histogram Plot)
fig7 = px.histogram(df, x='Number of Children', y='Satisfaction Rate', histfunc='avg',
                  title='Number of Children vs. Satisfaction Rate',
                  labels={'Number of Children': 'Number of Children', 'Satisfaction Rate': 'Satisfaction Rate'})

# Arrange the subplots in a grid layout
fig = make_subplots(rows=4, cols=2, subplot_titles=('Age vs. Satisfaction Rate',
                                                    'Country vs. Satisfaction Rate',
                                                    'Education Level vs. Satisfaction Rate',
                                                    'Number of Languages Spoken vs. Satisfaction Rate',
                                                    'Gender vs. Satisfaction Rate',
                                                    'Marital Status vs. Satisfaction Rate',
                                                    'Number of Children vs. Satisfaction Rate'))

fig.add_trace(fig1['data'][0], row=1, col=1)
fig.add_trace(fig2['data'][0], row=1, col=2)
fig.add_trace(fig3['data'][0], row=2, col=1)
fig.add_trace(fig4['data'][0], row=2, col=2)
fig.add_trace(fig5['data'][0], row=3, col=1)
fig.add_trace(fig6['data'][0], row=3, col=2)
fig.add_trace(fig7['data'][0], row=4, col=1)

dropdown_options = [
    {'label': 'Age vs. Satisfaction Rate', 'value': 'age'},
    {'label': 'Country vs. Satisfaction Rate', 'value': 'country'},
    {'label': 'Education Level vs. Satisfaction Rate', 'value': 'education'},
    {'label': 'Number of Languages Spoken vs. Satisfaction Rate', 'value': 'languages'},
    {'label': 'Gender vs. Satisfaction Rate', 'value': 'gender'},
    {'label': 'Marital Status vs. Satisfaction Rate', 'value': 'marital_status'},
    {'label': 'Number of Children vs. Satisfaction Rate', 'value': 'children'}
]

dropdown_options = [
    {'label': 'Age vs. Satisfaction Rate', 'value': 'age'},
    {'label': 'Country vs. Satisfaction Rate', 'value': 'country'},
    {'label': 'Education Level vs. Satisfaction Rate', 'value': 'education'},
    {'label': 'Number of Languages Spoken vs. Satisfaction Rate', 'value': 'languages'},
    {'label': 'Gender vs. Satisfaction Rate', 'value': 'gender'},
    {'label': 'Marital Status vs. Satisfaction Rate', 'value': 'marital_status'},
    {'label': 'Number of Children vs. Satisfaction Rate', 'value': 'children'}
]

# Defining the layout of Dash app
app.layout = html.Div([
    html.H1('Satisfaction Rate Visualizations'),
    html.Div([
        html.Label('Select a visualization:'),
        dcc.Dropdown(
            id='dropdown',
            options=dropdown_options,
            value='age'
        )
    ]),
    html.Div([
        dcc.Graph(id='graph')
    ])
])

# Callback function to update the graph based on the dropdown selection
@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph(selected_value):
    if selected_value == 'age':
        return fig1
    elif selected_value == 'country':
        return fig2
    elif selected_value == 'education':
        return fig3
    elif selected_value == 'languages':
        return fig4
    elif selected_value == 'gender':
        return fig5
    elif selected_value == 'marital_status':
        return fig6
    elif selected_value == 'children':
        return fig7

if __name__ == '__main__':
    app.run_server(debug=False)

# References:   
# https://dash.plotly.com/
# https://plotly.com/python/plotly-express/
# https://plotly.com/python-api-reference/generated/plotly.subplots.make_subplots.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter_3d.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter_polar.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter_ternary.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter_mapbox.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter_carpet.html
# https://plotly.com/python-api-reference/generated/plotly.express.scatter_matrix.html
