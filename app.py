# app.py
from dash import Dash, html, dcc
import dash

# Tailwind CSS
external_scripts = [
    {'src': 'https://cdn.tailwindcss.com'}
]

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_scripts=external_scripts
)

server = app.server

app.layout = html.Div(children=[
    html.Div(className='mx-auto max-w-7xl px-2 py-4 bg-blue-400', children=[
        html.Div(className='flex flex-col items-center gap-3', children=[
            html.Div(className='w-48 aspect-square overflow-hidden', children=[
                html.Img(className='w-full h-full object-cover', src="assets/dog.png")
            ]),
            dcc.Link(html.H1(className='font-bold text-3xl text-white', children="Mathematical Model of Brain Tumour"), href='/')
        ])
    ]), 
    html.Div(className='mx-auto max-w-7xl px-2 py-4', children=[
        html.Div(className='flex gap-6 justify-center', children=[
            #dcc.Link(html.Button('Por frecuencia', className='px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700'), href='/'),
        ]),
    ]),
    html.Div(className='mx-auto max-w-7xl px-2 py-4', children=[
        dash.page_container
    ]),
    html.Div(className='mx-auto max-w-7xl h-[16rem] mt-6 px-2 py-4 bg-blue-800', children=[
        html.Div(className='h-full flex flex-col justify-center items-center gap-3 text-white', children=[
            html.P(children=[
                html.Strong("Alumno: "),
                html.Span("Linares Rojas, Ander Rafael")
            ]),
            html.P(children=[
                html.Strong("Código: "),
                html.Span("22140367")
            ]),
            html.P(children=[
                html.Strong("Alumno: "),
                html.Span("Espinoza Huaman, Diego Alexhander")
            ]),
            html.P(children=[
                html.Strong("Código: "),
                html.Span("22140106")
            ]),
            html.P(children=[
                html.Strong("Alumno: "),
                html.Span("Vilchez Quispe, Yoshiro Cardich ")
            ]),
            html.P(children=[
                html.Strong("Código: "),
                html.Span("22140122")
            ]),
        ]),
    ]), 
])

if __name__ == '__main__':
    app.run(debug=True, port='1254')

