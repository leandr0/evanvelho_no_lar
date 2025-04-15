import sqlite3
from History import History
from datetime import date
class EvangelhoDB:
    
    db_conn = None
    
    def __init__(self):
        self.__get_db_connection__()
        #self.__create_tables__()
        
    def __get_db_connection__(self):
        if(not self.db_conn or not self.__get_status_cursor__()):
            self.db_conn = sqlite3.connect('data/evangelho.db')
            
    def __get_status_cursor__(self):
        try:
            self.db_conn.cursor()
            return True
        except:
            return False
        
    def __create_tables__(self):
        
        try:
           self.__create_table_history__()
           self.__create_table_chapter__()
           self.__create_table_sub_chapter__()
           self.__create_table_item__()


           
        except Exception as inst:
           
            #print(type(inst))    # the exception instance
            #print(inst.args)     # arguments stored in .args
            #print(inst)
            pass

    def __create_table_sub_chapter__(self):

        try:
            self.__get_db_connection__()
            cursor = self.db_conn.cursor()

            cursor.execute("""
                    CREATE TABLE sub_chapter (
                        sub_chapter_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        chapter_id INTEGER NOT NULL,
                        FOREIGN KEY (chapter_id) REFERENCES chapter (chapter_id)
                        )""")

            self.db_conn.commit()
        except Exception as inst:
            self.db_conn.rollback()
            # print(type(inst))    # the exception instance
            # print(inst.args)     # arguments stored in .args
            # print(inst)
            pass
        finally:
            self.db_conn.close()

    def __create_table_item__(self):
        
        try:
            self.__get_db_connection__()
            cursor = self.db_conn.cursor()
            
            cursor.execute("""
                    CREATE TABLE item (
                        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        number INTEGER NOT NULL,
                        page INTEGER NOT NULL,
                        sub_chapter_id INTEGER NOT NULL,
                        UNIQUE (sub_chapter_id, number),
                        FOREIGN KEY (sub_chapter_id) REFERENCES sub_chapter (sub_chapter_id)
                        )""")
        
            self.db_conn.commit()    
        except Exception as inst:
            self.db_conn.rollback()
            #print(type(inst))    # the exception instance
            #print(inst.args)     # arguments stored in .args
            #print(inst)
            pass
        finally:    
            self.db_conn.close()
    
    def __create_table_chapter__(self):
        
        try:
            self.__get_db_connection__()
            cursor = self.db_conn.cursor()
            
            
            cursor.execute("""
                    CREATE TABLE chapter (
                        chapter_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        number INTEGER NOT NULL,
                        title TEXT NOT NULL,
                        UNIQUE (number)
                        )""")
        
            self.db_conn.commit()    
        except Exception as inst:
            self.db_conn.rollback()
            #print(type(inst))    # the exception instance
            #print(inst.args)     # arguments stored in .args
            print(inst)
            pass  
        finally:    
            self.db_conn.close()


    def __create_table_history__(self):
        try:
            self.__get_db_connection__()
            cursor = self.db_conn.cursor()

            cursor.execute("""
                        CREATE TABLE _history (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT NOT NULL,
                            chapter INTEGER NOT NULL,
                            item INTEGER NOT NULL
                            )""")

            self.db_conn.commit()
        except Exception as inst:
            self.db_conn.rollback()
            # print(type(inst))    # the exception instance
            # print(inst.args)     # arguments stored in .args
            print(inst)
            pass
        finally:
            self.db_conn.close()

    def insert_history(self, history : History):

        self.__get_db_connection__()
        cursor = self.db_conn.cursor()

        try:

            cursor.execute(
                "INSERT INTO history (date,chapter ,item) VALUES (" +
                "'" + history.date + "'," + str(history.chapter_number) + "," + str(history.item_number) + ")"
                )

            self.db_conn.commit()

            return cursor.lastrowid
        except sqlite3.IntegrityError as error:

            # cursor.execute("SELECT item_id FROM item WHERE cnpj = '"+item.cnpj+"' AND data_incidencia = '"+item.dt_incidencia+"'")

            # row = cursor.fetchone()

            # return row[0]
            pass

        except Exception as inst:
            print(type(inst))
            print(inst)
            self.db_conn.rollback()
            pass

        finally:
            self.db_conn.close()

    def __row_to_history__(self, row):

        history = History()

        history.chapter_number      = row[0]
        history.chapter_title       = row[1]
        history.sub_chapter_title   = row[2]
        history.item_number         = row[3]
        history.item_page           = row[4]

        today = date.today()
        data = today.strftime("%d/%m/%Y")

        history.date = data

        return history

    def searchItem(self , history: History):

        self.__get_db_connection__()

        cursor = self.db_conn.cursor()

        try:

            query = """
            SELECT 
                chapter.number AS chapter_number,
                chapter.title AS chapter_title,
                sub_chapter.title AS sub_chapter_title,
                item.number AS item_number,
                item.page AS item_page
            FROM chapter
            INNER JOIN sub_chapter
                ON chapter.chapter_id = sub_chapter.chapter_id
            INNER JOIN item
                ON item.sub_chapter_id = sub_chapter.sub_chapter_id
            WHERE 
                item.number = ? AND 
                chapter.number = ?;
            """

            cursor.execute(query, (history.item_number, history.chapter_number))
            row = cursor.fetchone()

            return self.__row_to_history__(row)
        except Exception as inst:
            print(type(inst))
            print(inst)
            self.db_conn.rollback()
            pass
        finally:
            self.db_conn.close()


if __name__ == "__main__":
    db = EvangelhoDB()
    history = History()



    db.searchItem(history)
    ##db.insert_history()