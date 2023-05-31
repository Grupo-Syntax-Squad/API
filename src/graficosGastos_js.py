import os
import ast

ANOS = [2019, 2020, 2021, 2022]
CIDADES = ['Aparecida', 'Caçapava', 'Jacareí', 'SJC', 'Taubaté']
def maioresgastos():
    """Retorna um dicionário com os 5 maiores gastos de cada ano de cada cidade.
    """
    gastos = {}
    for cidade in CIDADES:
        cidadegastos = []
        with open(f"{os.path.dirname(os.path.abspath(__file__))}/Gráficos e Raspagem de Dados/Gastos/{cidade}/5maioresgastos.csv", "r") as arquivo:
            for linha in arquivo.readlines():
                cidadegastos.append(ast.literal_eval(linha)[0])
                cidadegastos.append(ast.literal_eval(linha)[1])
                cidadegastos.append(ast.literal_eval(linha)[2])
                cidadegastos.append(ast.literal_eval(linha)[3])
                cidadegastos.append(ast.literal_eval(linha)[4])
            gastos[cidade] = cidadegastos[0:5], cidadegastos[5:10], cidadegastos[10:15], cidadegastos[15:20]
    return gastos
