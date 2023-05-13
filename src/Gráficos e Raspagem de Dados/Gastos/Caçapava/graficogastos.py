import os
import pandas as pd
import plotly.express as px

MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
ANOS = ["2019", "2020", "2021", "2022"]

valoresanos = []

for ano in ANOS:
    valores = []
    df = pd.read_excel(f'C:/Users/Wellington/Documents/GitHub/API/src/Gráficos e Raspagem de Dados/Gastos/Caçapava/Gastos{ano}/{ano}.xlsx')
    total = df.sort_values('Quanto já foi realizado <br>(Empenhado ou Pago)')
    total.reset_index(drop=True, inplace=True)
    for valor in total['Quanto já foi realizado <br>(Empenhado ou Pago)'][-5:]:
        valores.append(valor)
    print(ano)
    print(sorted(valores, reverse=True))
    valoresanos.append(sorted(valores, reverse=True))

valoresanos = pd.DataFrame(valoresanos, index=ANOS)

fig = px.bar(valoresanos, text_auto=True, barmode="group", width=700, height=600, title="5 maiores gastos por ano de Caçapava", labels={
                     "value": "Gastos (R$)",
                     "index": "Anos"
                 })

fig.update_layout(showlegend=False, title_x=0.5)
fig.update_traces(textposition="inside")

fig.show()

fig.write_image('C:/Users/Wellington/Documents/GitHub/API/src/Gráficos e Raspagem de Dados/Gastos/Caçapava/GráficoGastosporAnoCaçapava.svg')