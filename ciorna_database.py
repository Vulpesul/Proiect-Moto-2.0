from secrets import choice
import sqlite3
import pathlib

from inchirieri_moto import Menu

ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db2.db")

class Menu:

    @staticmethod
    def add_car_flow():
        car_input = Menu.add_car_menu()
        make_table.insert_info_moto(car_input)

    @staticmethod
    def get_main_menu_choice():

        choice_ok = False
        menu_entries = {
            1:
        }

    @staticmethod
    def bike_menu():
        return {
            "marca": input("Adauga marca:"),
            "model": input("Adauga model:"),
            "an_fabricatie": input("Adauga anul fabricatiei:"),
            "tip_cadru_motocicleta": input("Adauga tipul cadrului:"),
            "seria_sasiu": input("Adauga seria de sasiu:"),
            "numar_inmatriculare": input("Adauga numarul de inmatriculare:")
        }

    @staticmethod
    def client_menu():
        return {
            "nume": input("Adauga numele:"),
            "prenume": input("Adauga prenumele:"),
            "adresa": input("Adauga adresa:"),
            "telefon": input("Adauga numarul de telefon:"),
            "cnp": input("Adauga CNP:"),
            "email": input ("Adauga email:")
        }
    @staticmethod
    def rezervari_menu():
        return {
            "perioada": input("Adauga perioada dorita a rezervarii:"),
        } 

user_input = Menu.client_menu()
bike_input = Menu.bike_menu()
rezervare_input = Menu.rezervari_menu()




class DataBase:

    def __init__(self, connection):
        self.conn = sqlite3.connect(connection)


    def create_client_table(self):
        self.conn.cursor()
        self.conn.execute(""" 
            CREATE TABLE IF NOT EXISTS clienti (
            id INTEGER PRIMARY KEY,
            nume TEXT NOT NULL,
            prenume TEXT NOT NULL,
            adresa TEXT NOT NULL,
            telefon TEXT NOT NULL,
            cnp TEXT NOT NULL,
            email TEXT NOT NULL)"""
            )
        self.conn.commit()


    def create_rezervation_table(self):
        self.conn.cursor()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS rezervari (
            id INTEGER PRIMARY KEY,
            data_start DATE,
            perioada INTEGER,
            FK car_id,
            FK client_id)""" )
        self.conn.commit()


    def create_moto_table(self):
        self.conn.cursor()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS motociclete(
            id INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            model TEXT NOT NULL,
            an_fabricatie INTEGER NOT NULL,
            tip_cadru_motocicleta TEXT NOT NULL,
            seria_sasiu TEXT NOT NULL,
            numar_inmatriculare TEXT NOT NULL)
                """)
        self.conn.commit()



    def insert_info_clienti(self, client_data):
        self.conn.cursor()
        self.conn.execute(
            client_data["nume"],
            client_data["prenume"],
            client_data["adresa"],
            client_data["telefon"],
            client_data["cnp"],
            client_data["email"]
            )
    
        
        self.conn.commit()

    def insert_info_moto(self, bike_data):
        self.conn.cursor()
        self.conn.execute(
            bike_data["marca"],
            bike_data["model"],
            bike_data["an_fabricatie"],
            bike_data["tip_cadru_motocicleta"],
            bike_data["seria_sasiu"],
            bike_data["nr_inmatriculare"]
            )
        self.conn.commit()

    def insert_info_rezervari(self, rezervari_data):
        self.conn.cursor()
        self.conn.execute(rezervari_data["perioada"])
        self.conn.commit()





class Client:

    def __init__(self, user_data):
        self.__nume = user_data["nume"]
        self.__prenume = user_data["prenume"]
        self.__adresa = user_data["adresa"]
        self.__telefon = user_data["telefon"]
        self.__cnp = user_data["cnp"]
        self.__email = user_data["email"]

class Bike:
    
    def __init__(self, bike_data):
        self.__marca = bike_data["marca"]
        self.__model = bike_data["model"]
        self.__an_fabricatie = bike_data["an_fabricatie"]
        self.__tip_cadru_motocicleta = bike_data["tip_cadru_motocicleta"]
        self.__seria_sasiu = bike_data["seria_sasiu"]
        self.__nr_inmatriculare = bike_data["nr_inmatriculare"]

class Rezervari:

    def __init__(self,rezervari_data):
        self.__perioada = rezervari_data["perioada"]


bike1 = Bike(bike_data)
user1 = Client(user_input)
rezervari1 = Rezervari(rezervare_input)

make_table = DataBase(DB_FILE)
make_table.create_client_table()
make_table.create_moto_table()
make_table.create_rezervation_table()

make_table.insert_info_clienti(user_input)
make_table.insert_info_moto(bike_input)
make_table.insert_info_rezervari(rezervare_input)