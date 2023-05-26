import pandas as pd
import os
from pprint import pprint

CAPS = ['Cap 06', 'Cap 09', 'Cap 10', 'Cap 11']
CAPSDESC = ['Doenças do sistema nervoso', 'Doenças do aparelho circulatório', 'Doenças do aparelho respiratório', 'Doenças do aparelho digestivo']
ANOS = [2019, 2020, 2021, 2022]
CIDADES = ['350250 APARECIDA', '350850 CACAPAVA', '352440 JACAREI', '354990 SAO JOSE DOS CAMPOS', '355410 TAUBATE']
CIDADESNOME = ['APARECIDA', 'CACAPAVA', 'JACAREI', 'SJC', 'TAUBATE']

def dados_internacoes():
    dados_internacoes = {}
    for cidade in CIDADES:
        dados_city = []
        for cap in CAPS:
            dados = []
            ANOSG = []
            for ano in ANOS:
                df = pd.read_csv(f"{os.getcwd()}/Gráficos e Raspagem de Dados/.Tabelas Internações/dados cid10 {ano}.csv", sep=";", encoding="utf-8")
                cidadedados = df.loc[df['Munic�pio'] == cidade]
                dados.append(cidadedados.loc[CIDADES.index(cidade), cap])
                ANOSG.append(ano)
                if len(ANOSG) == 4:
                    dados_city.append([cap, ANOSG, dados])
                dados_internacoes[CIDADESNOME[CIDADES.index(cidade)]] = dados_city
    return dados_internacoes
