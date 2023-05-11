import re

# ([0-9]{1,3}.[0-9]{3}.[0-9]{3},[0-9]{2})

anos = ["2019", "2020", "2021", "2022"]

for ano in anos:
    valores = []
    with open(f"relatorio{ano}.txt", encoding='latin') as arquivo:
        txt = arquivo.read()
        x = re.findall("([0-9]{1,3}.[0-9]{3}.[0-9]{3},[0-9]{2})", txt)

    for valor in x:
        if "\t" in valor:
            valor = valor[3:].replace(".", "").replace(",", ".")
            valores.append(float(valor))
        else:
            valor = valor.replace(".", "").replace(",", ".")
            valores.append(float(valor))
    
    with open(f"os5maioresgastos{ano}.csv", "a") as arquivo:
        c = 0
        for valor in sorted(valores, reverse=True)[:6]:
            arquivo.write(f"{valor}\n")
            print(c, valor)
            c += 1