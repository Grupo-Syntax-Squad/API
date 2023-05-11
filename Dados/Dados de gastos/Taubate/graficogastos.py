import plotly.express as px
import pandas as pd

anos = ["2019", "2020", "2021", "2022"]
valores = []
for ano in anos:
    print(ano)
    valoresano =[]
    with open(f"os5maioresgastos{ano}.csv") as arquivo:
        for linha in arquivo.readlines():
            print(linha, end="")
            valoresano.append(float(linha))
        valoresano.pop(0)
        valores.append(valoresano)

print(anos, valores)

graficodict = {
    "Anos":anos,
    "Gasto":valores
}

df = pd.DataFrame.from_dict(graficodict)

fig = px.bar(df, x="Anos", y="Gasto")

fig.show()
