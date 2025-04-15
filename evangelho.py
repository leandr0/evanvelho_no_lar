from History import History
from evangelho_db import EvangelhoDB
from static_data import StaticData


class Evangelho:
    __data_base = None
    __static_data = None

    def __init__(self):
        self.__data_base = EvangelhoDB()
        self.__static_data = StaticData()

    def get_leitura(self) -> History:
        data        = self.__static_data.getLeitura()
        item_data   = self.__get_item_leirura(data)

        self.__save_item_leirura(item_data)

        return item_data

    def __get_item_leirura(self, search_data: History) -> History:
        return self.__data_base.searchItem(search_data)

    def __save_item_leirura(self, save_data: History):
        self.__data_base.insert_history(save_data)


if __name__ == "__main__":
    evangelho = Evangelho()
    history = evangelho.get_leitura()

    print("Capítulo : ", end="\n * ")
    print(str(history.chapter_number) + " - " + str(history.chapter_title))

    print("Ítem : ", end="\n * ")
    print(str(history.item_number) + " - " + str(history.sub_chapter_title))

    print("Página : ", end="\n * ")
    print(history.item_page)