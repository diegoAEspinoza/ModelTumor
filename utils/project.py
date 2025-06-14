# utils/utils_project.py

import numpy as np 
import plotly.graph_objects as go
import plotly.figure_factory as ff
from scipy.integrate import odeint

def dosis(t, varPhi, dias_con_medicamento, ciclo):
        dia_en_ciclo = t % ciclo

        if dia_en_ciclo < dias_con_medicamento: return varPhi
        else:  return 0


def model(populations, t, omega, Psi, P, A,K, psi, varPhi, zeta, show_continuos, dias_con_medicamento, ciclo):
        
        if show_continuos: VarPhi = varPhi
        else: VarPhi = dosis(t,varPhi, dias_con_medicamento, ciclo)

        H = lambda x: 0 if x < 0 else (1/2 if x == 0 else 1)

        G, C, N, Q = populations

        dGdt = omega[0]*G*(1-G/K[0]) - Psi[0]*G*C - (P[0]*G*Q)/(A[0]+G)
        dCdt = omega[1]*C*(1-C/K[1]) - Psi[1]*G*C - (P[1]*C*Q)/(A[1]+C)
        dNdt = psi*dGdt*H(-dGdt)*N             - (P[2]*N*Q)/(A[2]+N)
        dQdt = VarPhi                - zeta*Q
        
        return dGdt, dCdt,dNdt,dQdt



def proyect (populations, t_total, omega, Psi, P, A, K, psi, varPhi, zeta, show_continuos):
    
    t = np.linspace(0,t_total[0],100*t_total[0])
    solution = odeint(model, populations, t, args=(omega, Psi, P, A, K, psi, varPhi, zeta, show_continuos, t_total[1], t_total[2]))

    G, C, N, Q = solution.T

    # Create Plotly figure
    fig_t = go.Figure()

    fig_t.add_trace(go.Scatter(x=t, y=G, mode='lines', name='Células Gliales (G)', line=dict(color='blue')))
    fig_t.add_trace(go.Scatter(x=t, y=C, mode='lines', name='Células de Glioma (C)', line=dict(color='orange')))
    fig_t.add_trace(go.Scatter(x=t, y=N, mode='lines', name='Neuronas (N)', line=dict(color='red')))
    fig_t.add_trace(go.Scatter(x=t, y=Q, mode='lines', name='Agente Quimioterapéutico (Q)', line=dict(color='green')))

    fig_t.update_layout(
        title='Evolución Temporal de las Concentraciones Celulares y Agente Quimioterapéutico',
        xaxis_title='Tiempo (dias)',
        yaxis_title='Concentración (kg/m³)',
        template='plotly_white'
    )

    fig = [go.Figure(), go.Figure(), go.Figure(), go.Figure()]
    fig[0].add_trace(go.Scatter(x=t, y=G, mode='lines', name='Celulas Gliales', line=dict(color='blue')))
    fig[1].add_trace(go.Scatter(x=t, y=C, mode='lines', name='Celulas Glioma', line=dict(color='orange')))
    fig[2].add_trace(go.Scatter(x=t, y=N, mode='lines', name='Neuronas', line=dict(color='red')))
    fig[3].add_trace(go.Scatter(x=t, y=Q, mode='lines', name='Agente Quimioterapeutico', line=dict(color='green')))
    

    fig[0].update_layout(
        title='Evolución de la Concentración de Células Gliales (G)',
        xaxis_title='Tiempo (dias)',
        yaxis_title='Concentración de Células Gliales (kg/m³)',
        template='plotly_white'
        
    )
    fig[1].update_layout(
        title='Evolución de la Concentración de Células de Glioma (C)',
        xaxis_title='Tiempo (dias)',
        yaxis_title='Concentración de Células de Glioma (kg/m³)',
        template='plotly_white'
    )
    fig[2].update_layout(
        title='Evolución de la Concentración de Neuronas (N)',
        xaxis_title='Tiempo (días)',
        yaxis_title='Concentración de Neuronas (kg/m³)',
        template='plotly_white'
    )
    fig[3].update_layout(
        title='Evolución de la Concentración del Agente Quimioterapéutico (Q)',
        xaxis_title='Tiempo (días)',
        yaxis_title='Concentración del Agente Quimioterapéutico (kg/m³)',
        template='plotly_white'
    )


    return [fig_t, fig]