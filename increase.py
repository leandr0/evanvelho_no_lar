import random
from datetime import date
from History import History
from evangelho_db import EvangelhoDB


def set_cap(list_cap,size):
    for cap in range(1, size+1):
        list_cap.append(cap)

def set_items(name,page,items):
    return { 'name' :  name ,'page' : page , 'items' : items}
'''
def set_titles(name,item):
    return { 'name' :  name , 'item' : item}
'''


CAP_01_NAME = "Não vim destruir a lei"
CAP_02_NAME = "Meu Reino não é deste mundo"
CAP_03_NAME = "Há muitas moradas na casa de meu Pai"
CAP_04_NAME = "Ninguém poderá ver o Reino de Deus se não nascer de novo"
CAP_05_NAME = "Bem-aventurados os aflitos"
CAP_06_NAME = "O Cristo Consolador"
CAP_07_NAME = "Bem-aventurados os pobres de espírito"
CAP_08_NAME = "Bem-aventurados os que têm puro o coração"
CAP_09_NAME = "Bem-aventurados os que são brandos e pacíficos"
CAP_10_NAME = "Bem-aventurados os que são misericordiosos"
CAP_11_NAME = "Amar o próximo como a si mesmo"
CAP_12_NAME = "Amai os vossos inimigos"
CAP_13_NAME = "Não saiba a vossa mão esquerda o que dê a vossa mão direita"
CAP_14_NAME = "Honrai a vosso pai e a vossa mãe"
CAP_15_NAME = "Fora da caridade não há salvação"
CAP_16_NAME = "Não se pode servir a Deus e a Mamon"
CAP_17_NAME = "Sede perfeitos"
CAP_18_NAME = "Muitos os chamados, poucos os escolhidos"
CAP_19_NAME = "A fé transporta montanhas"
CAP_20_NAME = "Os trabalhadores da última hora"
CAP_21_NAME = "Haverá falsos cristos e falsos profetas"
CAP_22_NAME = "Não separeis o que Deus juntou"
CAP_23_NAME = "Estranha moral"
CAP_24_NAME = "Não ponhais a candeia debaixo do alqueire"
CAP_25_NAME = "Buscai e achareis"
CAP_26_NAME = "Dai gratuitamente o que gratuitamente recebestes"
CAP_27_NAME = "Pedi e obtereis"

capitulos = {}

capitulo_01 = []
set_cap(capitulo_01,11)

capitulos[1] = set_items(CAP_01_NAME ,41, capitulo_01)
"""

As três revelações: Moisés, Cristo, Espiritismo: 1 a 7. 
– Aliança da Ciência e da Religião: 8. 
– Instruções dos Espíritos: A nova era: 9 a 11.
"""

capitulo_02 = []
set_cap(capitulo_02,8)
capitulos[2] = set_items(CAP_02_NAME,51, capitulo_02)

capitulo_03 = []
set_cap(capitulo_03,19)
capitulos[3] = set_items(CAP_03_NAME ,57, capitulo_03)

capitulo_04 = []
set_cap(capitulo_04,26)
capitulos[4] = set_items(CAP_04_NAME ,67, capitulo_04)

capitulo_05 = []
set_cap(capitulo_05,31)
capitulos[5] = set_items(CAP_05_NAME ,79, capitulo_05)

capitulo_06 = []
set_cap(capitulo_06,8)
capitulos[6] = set_items(CAP_06_NAME ,105, capitulo_06)

capitulo_07 = []
set_cap(capitulo_07,13)
capitulos[7] = set_items(CAP_07_NAME ,111, capitulo_07)

capitulo_08 = []
set_cap(capitulo_08,21)
capitulos[8] = set_items(CAP_08_NAME ,123, capitulo_08)

capitulo_09 = []
set_cap(capitulo_09,10)
capitulos[9] = set_items(CAP_09_NAME ,135, capitulo_09)

capitulo_10 = []
set_cap(capitulo_10,21)
capitulos[10] = set_items(CAP_10_NAME ,141, capitulo_10)

capitulo_11 = []
set_cap(capitulo_11,15)
capitulos[11] = set_items(CAP_11_NAME ,153, capitulo_11)

capitulo_12 = []
set_cap(capitulo_12,16)
capitulos[12] = set_items(CAP_12_NAME ,165, capitulo_12)

capitulo_13 = []
set_cap(capitulo_13,20)
capitulos[13] = set_items(CAP_13_NAME ,177, capitulo_13)

capitulo_14 = []
set_cap(capitulo_14,9)
capitulos[14] = set_items(CAP_14_NAME ,197, capitulo_14)

capitulo_15 = []
set_cap(capitulo_15,10)
capitulos[15] = set_items(CAP_15_NAME ,207, capitulo_15)

capitulo_16 = []
set_cap(capitulo_16,15)
capitulos[16] = set_items(CAP_16_NAME ,215, capitulo_16)

capitulo_17 = []
set_cap(capitulo_17,11)
capitulos[17] = set_items(CAP_17_NAME ,231, capitulo_17)

capitulo_18 = []
set_cap(capitulo_18,16)
capitulos[18] = set_items(CAP_18_NAME ,243, capitulo_18)

capitulo_19 = []
set_cap(capitulo_19,12)
capitulos[19] = set_items(CAP_19_NAME ,257, capitulo_19)

capitulo_20 = []
set_cap(capitulo_20,5)
capitulos[20] = set_items(CAP_20_NAME ,261, capitulo_20)

capitulo_21 = []
set_cap(capitulo_21,11)
capitulos[21] = set_items(CAP_21_NAME ,267, capitulo_21)

capitulo_22 = []
set_cap(capitulo_22,5)
capitulos[22] = set_items(CAP_22_NAME ,277, capitulo_22)

capitulo_23 = []
set_cap(capitulo_23,18)
capitulos[23] = set_items(CAP_23_NAME ,281, capitulo_23)

capitulo_24 = []
set_cap(capitulo_24,19)
capitulos[24] = set_items(CAP_24_NAME ,291, capitulo_24)

capitulo_25 = []
set_cap(capitulo_25,11)
capitulos[25] = set_items(CAP_25_NAME ,299, capitulo_25)

capitulo_26 = []
set_cap(capitulo_26,10)
capitulos[26] = set_items(CAP_26_NAME ,305, capitulo_26)

capitulo_27 = []
set_cap(capitulo_27,23)
capitulos[27] = set_items(CAP_27_NAME ,311, capitulo_27)

def get_capitulo():
    today   = date.today()
    data    = today.strftime("%d/%m/%Y")
    cap     = random.randint(1, 27)

    print("Capítulo : ",end="\n * ")
    print(str(cap))

    cap_list = capitulos.get(cap)
    #print(cap_list)
    print(cap_list['name'])

    print("Página : ", end="\n * ")
    print(cap_list['page'])
    #print(len(cap_list['items']))
    item = random.randint(1, len(cap_list['items']))
    print("Ítem : ", end="\n * ")
    print(str(item))

    db = EvangelhoDB()
    history = History()

    history.chapter_number = cap
    history.item_number = item
    history.date = data

    insert_History = db.searchItem(history)

    #db.insert_history(insert_History)
'''
    f = open("evangelho_no_lar_2025.txt", "a")
    f.write("Dia do evangelho : "+str(data))
    f.write("\nCapítulo : " + str(cap))
    f.write("\nItem : " + str(item))
    f.write("\n")
    f.write("\n")
    f.close()
'''
get_capitulo()