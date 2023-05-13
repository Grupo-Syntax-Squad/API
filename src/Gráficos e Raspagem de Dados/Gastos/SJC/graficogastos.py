import pandas as pd
from pprint import pprint
import plotly.express as px

ANOS = ['2019', '2020', '2021', '2022']
valores = []

"""for ano in ANOS:
    for c in range(12):
        try:
            if c == 0:
                df = pd.read_csv(f'src/Gráficos/Gastos/SJC/Gastos{ano}/despesa_funcao.csv', sep=';', encoding='latin', on_bad_lines='skip')
            else:
                df = pd.read_csv(f'src/Gráficos/Gastos/SJC/Gastos{ano}/despesa_funcao ({c}).csv', sep=';', encoding='latin', on_bad_lines='skip')
            print(ano, c+1)
            df['Pago  (R$)'].to_csv(f'src/Gráficos/Gastos/SJC/Gastos{ano}/{c+1}-{ano}.csv', sep=";")
        except:
            pass"""

valoresanos = []
for ano in ANOS:
    valores = []
    for c in range(12):
        try:
            with open(f'src/Gráficos e Raspagem de Dados/Gastos/SJC/Gastos{ano}/{c+1}-{ano}.csv') as arquivo:
                for n in arquivo.read().split(';'):
                    valores.append(n)
        except:
            pass
    valoresanos.append(valores)


somaanos = []
valoresanos2 = []
c = 0
for ano in valoresanos:
    soma = 0
    valores = []
    for valor in ano:
        try:
            valores.append(float(valor[:-3].replace('.', '').replace(',', '.')))
            soma += float(valor[:-3].replace('.', '').replace(',', '.'))
        except:
            pass
    valoresanos2.append(sorted(valores, reverse=True)[:5])
    somaanos.append(soma)
    print(ANOS[c], soma)
    c += 1

pprint(somaanos)
pprint(valoresanos2)

df = pd.DataFrame(valoresanos2, index=ANOS)

fig = px.bar(df, text_auto=True, barmode="group", width=700, height=600, title="5 maiores gastos por ano de SJC", labels={
                     "value": "Gastos (R$)",
                     "index": "Anos"
                 })

fig.update_layout(showlegend=False)
fig.update_layout(title_x=0.5)

fig.write_image(f"src/Gráficos e Raspagem de Dados/Gastos/SJC/GráficoGastosporAnoSJC.svg")

fig.show()