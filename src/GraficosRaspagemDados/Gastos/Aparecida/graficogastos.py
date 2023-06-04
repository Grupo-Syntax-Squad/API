import pandas as pd
import os
import plotly.express as px
from pprint import pprint

MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
ANOS = ["2019", "2020", "2021", "2022"]

valoresanos = []

for ano in ANOS:
    valores = []
    df = pd.read_csv(f'C:\\Users\\Wellington\\Documents\\Trampos\\API\\src\\GraficosRaspagemDados\\Gastos\\Aparecida\\Gastos{ano}\\detalhamentoDespesas{ano}.csv', sep=';')
    total = df.sort_values('vl_total_pag')
    totalk = df[['natureza', 'elemento', 'vl_total_pag']]
    totalk.reset_index(drop=True, inplace=True)
    total.reset_index(drop=True, inplace=True)
    
    print((totalk["natureza"], totalk['elemento'], totalk['vl_total_pag']))
    valores = [valor for valor in total['vl_total_pag'][-5:]]
    valoresanos.append(sorted(valores, reverse=True))

print(valoresanos)

if os.path.exists(f"5maioresgastos.csv"):
    os.remove(f"5maioresgastos.csv")

with open("5maioresgastos.csv", "a") as arquivo:
    for ano in valoresanos:
        arquivo.write(f"{ano}\n")

# valoresanos = pd.DataFrame(valoresanos, index=ANOS)

# fig = px.bar(valoresanos, text_auto=True, barmode="group", width=700, height=600, title="5 maiores gastos por ano de Aparecida", labels={
#                      "value": "Gastos (R$)",
#                      "index": "Anos"
#                  })

# fig.update_layout(showlegend=False, title_x=0.5)
# fig.update_traces(textposition="inside")

# fig.show()

# fig.write_image('src/Gráficos e Raspagem de Dados/Gastos/Aparecida/GráficoGastosporAnoAparecida.svg')