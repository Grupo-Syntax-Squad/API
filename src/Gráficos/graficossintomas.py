import pandas as pd
import plotly.express as px
import os

if not os.path.exists("src/Gráficos/Gráficos Sintomas"):
    os.mkdir("src/Gráficos/Gráficos Sintomas")

caps = ['Cap 06', 'Cap 09', 'Cap 10', 'Cap 11']
capsdesc = ['Doenças do sistema nervoso', 'Doenças do aparelho circulatório', 'Doenças do aparelho respiratório', 'Doenças do aparelho digestivo']
anos = ['2019', '2020', '2021', '2022']
cidades = ['350250 APARECIDA', '350850 CACAPAVA', '352440 JACAREI', '354990 SAO JOSE DOS CAMPOS', '355410 TAUBATE']
cidadesnome = ['APARECIDA', 'CACAPAVA', 'JACAREI', 'SJC', 'TAUBATE']
for cidade in cidades:
    for cap in caps:
        dados = []
        anosg = []
        for ano in anos:
            df = pd.read_csv(f"src/Gráficos/.Tabelas Internações/dados cid10 {ano}.csv", sep=";", encoding="utf-8")
            cidadedados = df.loc[df['Munic�pio'] == cidade]
            dados.append(cidadedados.loc[cidades.index(cidade), cap])
            anosg.append(ano)
            if len(anosg) == 4:
                graficodict = {
                    'Ano': anosg,
                    'Quantidade de Internações': dados
                }
                df = pd.DataFrame.from_dict(graficodict)
                fig = px.bar(df, x='Ano', y='Quantidade de Internações', color='Ano', title=f'Casos de Internações {capsdesc[caps.index(cap)]} - {cidadesnome[cidades.index(cidade)]}', width=700, height=600)
                fig.show()
                fig.write_image(f"src/Gráficos/Gráficos Sintomas/Casos de Internações_{capsdesc[caps.index(cap)]}-{cidade[7:]}.png")
            else:
                pass
