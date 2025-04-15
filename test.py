
def set_cap(list_cap,size):
    for cap in range(1, size+1):
        list_cap.append(cap)

capitulos = {}
capitulo_01 = []

set_cap(capitulo_01,25)
capitulos[1] = {'CAP_01_NAME' : capitulo_01}

print(capitulos)