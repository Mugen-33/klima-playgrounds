import dash  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
import dash_extensions as de  # pip install dash-extensions

from components.disclaimer import short_disclaimer_row

url = "https://assets6.lottiefiles.com/packages/lf20_0ac4xdrp.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

layout = dbc.Container([
    dbc.Row([
        html.Div(html.Img(src=app.get_asset_url('Klima_PG_trans_no_box.png'),
                          style={'width': '50%',
                                 'height': '100%',
                                 'padding': '10px'}))]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Label('What is KlimaDAO',
                                  style={'color': 'white', 'fontSize': 15,
                                         'textAlign': 'center'}),
                    ]),
                    dbc.Row([
                        html.Div(
                            'Klima DAO aims to be the first building block for unlocking the carbon economy - '
                            'an economy where more economic activity leads to an acceleration in planetary '
                            'regeneration rather than more damage to our planet.',
                            style={'textAlign': 'center'})
                    ])
                ])
            ], style={'textAlign': 'center', 'height': '100%'})
        ], style={'padding': '10px'}, xs=12, sm=12, md=12, lg=6, xl=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Label('What is Klima Playground',
                                  style={'color': 'white', 'fontSize': 15,
                                         'textAlign': 'center'}),
                    ]),
                    dbc.Row([
                        html.Div(
                            'Klima Playgrounds is an ecosystem made by a community of Klimates.'
                            'Together, we seek to create a unique and powerful learning environment that '
                            'reduces the learning curve for interacting with the KlimaDAO protocol, '
                            'enhances the shared mental model of our community and '
                            'creates knowledge symmetry for all members. ',
                            style={'textAlign': 'center'})
                    ])
                ])
            ], style={'textAlign': 'center', 'height': '100%'})
        ], style={'padding': '10px'}, xs=12, sm=12, md=12, lg=6, xl=6)
    ]),
    short_disclaimer_row()
])
