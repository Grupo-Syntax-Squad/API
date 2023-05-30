import os

CIDADES = ['Aparecida', 'Caçapava', 'Jacareí', 'SJC', 'Taubaté']
def maioresgastos():
    """Retorna um dicionário com os 5 maiores gastos de cada ano de cada cidade.
    """
    gastos = {}
    for cidade in CIDADES:
        cidadegastos = []
        with open(f"{os.path.dirname(os.path.abspath(__file__))}/Gráficos e Raspagem de Dados/Gastos/{cidade}/5maioresgastos.csv", "r") as arquivo:
            for linha in arquivo.readlines():
                cidadegastos.append(linha)
        gastos[cidade] = cidadegastos
    return gastos
    print(gastos)

maioresgastos()