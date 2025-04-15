import random
from datetime import date

def set_cap(list_cap,size):
    for cap in range(1, size+1):
        list_cap.append(cap)

capitulos = {}


capitulo_01 = []
set_cap(capitulo_01,11)
capitulos[1] = capitulo_01

capitulo_02 = []
set_cap(capitulo_02,8)
capitulos[2] = capitulo_02

capitulo_03 = []
set_cap(capitulo_03,19)
capitulos[3] = capitulo_03

capitulo_04 = []
set_cap(capitulo_04,26)
capitulos[4] = capitulo_04

capitulo_05 = []
set_cap(capitulo_05,31)
capitulos[5] = capitulo_05

capitulo_06 = []
set_cap(capitulo_06,8)
capitulos[6] = capitulo_06

capitulo_07 = []
set_cap(capitulo_07,13)
capitulos[7] = capitulo_07

capitulo_08 = []
set_cap(capitulo_08,21)
capitulos[8] = capitulo_08

capitulo_09 = []
set_cap(capitulo_09,10)
capitulos[9] = capitulo_09

capitulo_10 = []
set_cap(capitulo_10,21)
capitulos[10] = capitulo_10

capitulo_11 = []
set_cap(capitulo_11,15)
capitulos[11] = capitulo_11

capitulo_12 = []
set_cap(capitulo_12,16)
capitulos[12] = capitulo_12

capitulo_13 = []
set_cap(capitulo_13,20)
capitulos[13] = capitulo_13

capitulo_14 = []
set_cap(capitulo_14,9)
capitulos[14] = capitulo_14

capitulo_15 = []
set_cap(capitulo_15,10)
capitulos[15] = capitulo_15

capitulo_16 = []
set_cap(capitulo_16,15)
capitulos[16] = capitulo_16

capitulo_17 = []
set_cap(capitulo_17,11)
capitulos[17] = capitulo_17

capitulo_18 = []
set_cap(capitulo_18,16)
capitulos[18] = capitulo_18

capitulo_19 = []
set_cap(capitulo_19,12)
capitulos[19] = capitulo_19

capitulo_20 = []
set_cap(capitulo_20,5)
capitulos[20] = capitulo_20

capitulo_21 = []
set_cap(capitulo_21,11)
capitulos[21] = capitulo_21

capitulo_22 = []
set_cap(capitulo_22,5)
capitulos[22] = capitulo_22

capitulo_23 = []
set_cap(capitulo_23,18)
capitulos[23] = capitulo_23

capitulo_24 = []
set_cap(capitulo_24,19)
capitulos[24] = capitulo_24

capitulo_25 = []
set_cap(capitulo_25,11)
capitulos[25] = capitulo_25

capitulo_26 = []
set_cap(capitulo_26,10)
capitulos[26] = capitulo_26

capitulo_27 = []
set_cap(capitulo_27,23)
capitulos[27] = capitulo_27

def get_capitulo():
    today = date.today()
    data = today.strftime("%d/%m/%Y")
    cap = random.randint(1, 27)
    print("Capítulo : ",end="\n * ")
    print(str(cap))
    cap_list = capitulos.get(cap)
    #print(cap_list)
    item = random.randint(1, len(cap_list))
    print("Ítem : ", end="\n * ")
    print(str(item))
    f = open("evangelho_no_lar_2023.txt", "a")
    f.write("Dia do evangelho : "+str(data))
    f.write("\nCapítulo : " + str(cap))
    f.write("\nItem : " + str(item))
    f.write("\n")
    f.write("\n")
    f.close()

get_capitulo()