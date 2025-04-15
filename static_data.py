import random
from History import History

class StaticData:
    
    __capitulos = {}

    def __set_cap(self,list_cap, size):
        for cap in range(1, size + 1):
            list_cap.append(cap)

    def __set_items(self,items):
        return {'items': items}

    def __get_capitulo(self,cap):

        #print("Capítulo : ", end="\n * ")
        #print(str(cap))

        cap_list = self.__capitulos.get(cap)
        #print(cap_list['name'])

        return cap_list


    def __get_item(self,cap_list):

        item = random.randint(1, len(cap_list['items']))
        #print("Ítem : ", end="\n * ")
        #print(str(item))

        return item

    def getLeitura(self):
        cap = random.randint(1, 27)
        cap_list    =  self.__get_capitulo(cap)
        item        =  self.__get_item(cap_list)
        history = History()
        history.chapter_number = cap
        history.item_number = item

        return history

    def __init__(self):
        capitulo_01 = []
        self.__set_cap(capitulo_01, 11)
        self.__capitulos[1] = self.__set_items(capitulo_01)

        capitulo_02 = []
        self.__set_cap(capitulo_02, 8)
        self.__capitulos[2] = self.__set_items(capitulo_02)

        capitulo_03 = []
        self.__set_cap(capitulo_03, 19)
        self.__capitulos[3] = self.__set_items( capitulo_03)

        capitulo_04 = []
        self.__set_cap(capitulo_04, 26)
        self.__capitulos[4] = self.__set_items(capitulo_04)

        capitulo_05 = []
        self.__set_cap(capitulo_05, 31)
        self.__capitulos[5] = self.__set_items(capitulo_05)

        capitulo_06 = []
        self.__set_cap(capitulo_06, 8)
        self.__capitulos[6] = self.__set_items(capitulo_06)

        capitulo_07 = []
        self.__set_cap(capitulo_07, 13)
        self.__capitulos[7] = self.__set_items(capitulo_07)

        capitulo_08 = []
        self.__set_cap(capitulo_08, 21)
        self.__capitulos[8] = self.__set_items(capitulo_08)

        capitulo_09 = []
        self.__set_cap(capitulo_09, 10)
        self.__capitulos[9] = self.__set_items(capitulo_09)

        capitulo_10 = []
        self.__set_cap(capitulo_10, 21)
        self.__capitulos[10] = self.__set_items(capitulo_10)

        capitulo_11 = []
        self.__set_cap(capitulo_11, 15)
        self.__capitulos[11] = self.__set_items(capitulo_11)

        capitulo_12 = []
        self.__set_cap(capitulo_12, 16)
        self.__capitulos[12] = self.__set_items(capitulo_12)

        capitulo_13 = []
        self.__set_cap(capitulo_13, 20)
        self.__capitulos[13] = self.__set_items(capitulo_13)

        capitulo_14 = []
        self.__set_cap(capitulo_14, 9)
        self.__capitulos[14] = self.__set_items(capitulo_14)

        capitulo_15 = []
        self.__set_cap(capitulo_15, 10)
        self.__capitulos[15] = self.__set_items(capitulo_15)

        capitulo_16 = []
        self.__set_cap(capitulo_16, 15)
        self.__capitulos[16] = self.__set_items(capitulo_16)

        capitulo_17 = []
        self.__set_cap(capitulo_17, 11)
        self.__capitulos[17] = self.__set_items(capitulo_17)

        capitulo_18 = []
        self.__set_cap(capitulo_18, 16)
        self.__capitulos[18] = self.__set_items(capitulo_18)

        capitulo_19 = []
        self.__set_cap(capitulo_19, 12)
        self.__capitulos[19] = self.__set_items(capitulo_19)

        capitulo_20 = []
        self.__set_cap(capitulo_20, 5)
        self.__capitulos[20] = self.__set_items(capitulo_20)

        capitulo_21 = []
        self.__set_cap(capitulo_21, 11)
        self.__capitulos[21] = self.__set_items(capitulo_21)

        capitulo_22 = []
        self.__set_cap(capitulo_22, 5)
        self.__capitulos[22] = self.__set_items(capitulo_22)

        capitulo_23 = []
        self.__set_cap(capitulo_23, 18)
        self.__capitulos[23] = self.__set_items(capitulo_23)

        capitulo_24 = []
        self.__set_cap(capitulo_24, 19)
        self.__capitulos[24] = self.__set_items(capitulo_24)

        capitulo_25 = []
        self.__set_cap(capitulo_25, 11)
        self.__capitulos[25] = self.__set_items(capitulo_25)

        capitulo_26 = []
        self.__set_cap(capitulo_26, 10)
        self.__capitulos[26] = self.__set_items(capitulo_26)

        capitulo_27 = []
        self.__set_cap(capitulo_27, 23)
        self.__capitulos[27] = self.__set_items(capitulo_27)