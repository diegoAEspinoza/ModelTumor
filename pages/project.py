# pages/pages_project.py

import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/',
    name='Proyecto Modelos'
)

layout = html.Div(className="space-y-9", children=[
    html.Div(className="flex flex-col gap-9 items-center", children=[
        #html.Div(className="font-semibold text-2xl", children="Modelo virus informático"),
        html.Div(
            className='flex gap-6', children=[
                # Imagen 1
                html.Img(
                    className="w-[25rem]",
                    src='/assets/model.png', 
                    alt='Imagen de modelo', 
                ),
                # Imagen 2
                html.Img(
                    className="w-[25rem]",
                    src='/assets/model1.png', 
                    alt='Imagen de modelo', 
                )
            ]
        ),
    ]),
    html.Div(className="flex flex-col gap-6", children=[
        html.Div(className="space-y-3", children=[
            html.H2(className="font-semibold text-center text-2xl", children='Parámetros'),
            html.Div(className="flex gap-10", children=[
                # Parámetros generales
                html.Div(className='flex-1 space-y-1', children=[
                    html.Div([
                        html.H3(className="font-semibold", children='Glia'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=495, id='G', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Gliomas'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=3, id='C', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Neuronas'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=495, id='N', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Agente Quimioterapeutico'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=0, id='Q', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Tiempo (dias)'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=616, id='tiempo', debounce=True)
                    ]),
                    html.Div(className='div_button my-4', children=[
                        html.Button('Change Mode', id='toggle-button', n_clicks=0,         className='toggle-button bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg shadow-md transition-all duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50'),
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Dias Sin Medicamento'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=25, id='dia_sin_medicamento', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Dias con Medicamento'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value= 3, id='dia_con_medicamento', debounce=True)
                    ]),
                ]),
                # Parámetros adicionales
                html.Div(className="flex-1", children=[
                    html.Div([
                        html.H3(className="font-semibold", children='omega1'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=6.8e-3, id='omega1', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='omega2'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=1.2e-2, id='omega2', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Psi1'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=3.5e-5, id='Psi1', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='Psi2'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=3.5e-6, id='Psi2', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='P1'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=2.4e-5, id='P1', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='P2'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=2.4e-2, id='P2', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='P3'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=2.4e-5, id='P3', debounce=True)
                    ]),
                ]),
                html.Div(className="flex-1", children=[
                    html.Div([
                        html.H3(className="font-semibold", children='A1'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=500, id='A1', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='A2'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=500, id='A2', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='A3'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=500, id='A3', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='K1'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=500, id='K1', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='K2'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=510, id='K2', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='psi'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=2e-2, id='psi', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='varPhi'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=0, id='varPhi', debounce=True)
                    ]),
                    html.Div([
                        html.H3(className="font-semibold", children='zeta'),
                        dcc.Input(className="w-full text-sm px-2 py-1 border border-gray-400", type='number', value=0.2, id='zeta', debounce=True)
                    ]),
                ]),
            ]),
        ]),
        # Sección de gráfica
        html.Div(className="flex-1", children=[
            html.H2(className="font-semibold text-center text-2xl", children='Resultados'),
            html.Div(className='grid grid-cols-3 gap-6', children=[
                html.Div(className="col-span-3", children=dcc.Loading(type='default', children=dcc.Graph(id='COMPLETO'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='glia'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='glioma'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='neuronas'))),
                html.Div(className="col-span-1", children=dcc.Loading(type='default', children=dcc.Graph(id='quimio'))),
            ])
        ])
    ])
])

###################################################################################
#
# Callback principal
#
###################################################################################
@callback(
    Output('COMPLETO', 'figure'),
    Output('glia', 'figure'),
    Output('glioma', 'figure'),
    Output('neuronas', 'figure'),
    Output('quimio', 'figure'),
    
    Input('G', 'value'),
    Input('C', 'value'),
    Input('N', 'value'),
    Input('Q', 'value'),
    
    Input('tiempo', 'value'),
    Input('dia_sin_medicamento','value'),
    Input('dia_con_medicamento','value'),

    Input('omega1', 'value'),
    Input('omega2', 'value'),
    
    Input('Psi1', 'value'),
    Input('Psi2', 'value'),
    
    Input('P1', 'value'),
    Input('P2', 'value'),
    Input('P3', 'value'),
    
    Input('A1', 'value'),
    Input('A2', 'value'),
    Input('A3', 'value'),
    
    Input('K1', 'value'),
    Input('K2', 'value'),
    
    Input('psi', 'value'),
    Input('varPhi', 'value'),
    Input('zeta', 'value'),

    Input('toggle-button', 'n_clicks') 

)


def grafic_SIR_model(G, C, N, Q, t, t_sin, t_con, omega1, omega2, Psi1, Psi2, P1, P2, P3, A1, A2, A3, K1, K2, psi, varPhi, zeta, n_clicks):
    
    show_continuos = (n_clicks % 2 == 1)
    
    # Initial populations and parameters
    populations = [G, C, N, Q]
    t_total     = [t, t_con, t_sin+t_con]
    omega       = [omega1, omega2]
    Psi         = [Psi1, Psi2]
    P           = [P1, P2, P3]
    A           = [A1, A2, A3]
    K           = [K1, K2]
    
    # Generate the graphs
    fig = proyect(populations, t_total, omega, Psi, P, A, K, psi, varPhi, zeta, show_continuos)
    
    # Unpack the figures
    fig_t = fig[0]  # Combined figure
    individual_figs = fig[1]  # List of individual compartment figures

    # Return the combined figure for the 'COMPLETO' graph, and the individual graphs for the others
    return fig_t, individual_figs[0], individual_figs[1], individual_figs[2], individual_figs[3]