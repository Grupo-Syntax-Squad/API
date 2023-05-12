import pandas as pd

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

for ano in ANOS:
    for c in range(12):
        try:
            with open(f'src/Gráficos/Gastos/SJC/Gastos{ano}/{c+1}-{ano}.csv') as arquivo:
                print(arquivo.read().split(';'))
        except:
            pass