import sqlite3
import pathlib
import sys



ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db2.db")
db_con = sqlite3.connect(DB_FILE)


class Menu:
   
 
    @staticmethod
    def bike_flow():
        bike_input = Menu.bike_menu()
        make_table.insert_info_moto(bike_input)
        
        
        @staticmethod
        def menu_choice():
            
            choice_ok = False
            
            menu_entries = {
            1: ("text" "Adauga motocicleta",  Menu.bike_flow),
            2: ("text" "Adauga client",  Menu.client_menu ),
            3: ("text" "Adauga rezervare",  Menu.rezervari_menu),
            4: ("text" "Vezi rezervari",  DataBase.print_rezervari),
            5: ("text" "Anuleaza rezervarea", DataBase.anuleaza_rezervare),
            6: ("text" "Inchide programul", sys.exit)
        }
                
        
            while not choice_ok:
                for k, v in menu_entries.items():
                    print(k,",",v["text"], sep="")
                choice = input("Alege un numar: ")
                if not choice.insumeric() or int(choice) not in menu_entries.keys():
                    print("Erroare, Alege un numar din lista.\n\n")
                else:
                    choice_ok = True
            return menu_entries[int(choice)]
                
        



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
            "data_start":input("Data:"),
            "perioada": input("Adauga perioada dorita a rezervarii:"),
            "client_id": input("Adauga Used ID"),
            "bike_id": input("Bike ID")
        } 






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
            bike_id INTEGER,
            client_id INTEGER
            FOREIGN KEY (bike_id) REPLACES client(id)
            FOREIGN KEY (client_id) REPLACES bike(id)
            """ )
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
            numar_inmatriculare TEXT NOT NULL)"""
            )
        self.conn.commit()



    def insert_info_clienti(self, client_data):
        self.conn.cursor()
        self.conn.execute("""INSERT INFO CLIENTI (nume, prenume, adresa, telefon, cnp, email) VALUES (?,?,?,?,?,?)"""
            (
            client_data("nume"),
            client_data("prenume"),
            client_data("adresa"),
            client_data("telefon"),
            client_data("cnp"),
            client_data("email")
        ))
        self.conn.commit()

    def insert_info_moto(self, bike_data):
        self.conn.cursor()
        self.conn.execute("""INSERT INFO motociclete (marca, model, an_fabricatie, tip_cadru_motocicleta, seria_sasiu, numar_inmatriculare) VALUES (?,?,?,?,?,?)"""(
            bike_data("marca"),
            bike_data("model"),
            bike_data("an_fabricatie"),
            bike_data("tip_cadru_motocicleta"),
            bike_data("seria_sasiu"),
            bike_data("nr_inmatriculare")
            ))
        self.conn.commit()

    def insert_info_rezervari(self, rezervari_data):
        self.conn.cursor()
        self.conn.execute("""INSERT INFO rezervari (data_start,perioada,client_id,bike_id) Values (?,?,?,?)""",(
            rezervari_data("data_start"),
            rezervari_data("perioada"),
            rezervari_data("client_id"),
            rezervari_data("bike_id")))
        self.conn.commit()

    def print_rezervari(self):
        bike = self.conn.cursor()  
        rows = bike.execute('SELECT FROM rezervari')
        row_list = list(rows)
        
        for i in row_list:
            print(f"data_start {i[2]} | perioada {i[2]} | bike_id {i[3]} | client_id{i[4]} ")     
        self.conn.commit()


    def show_bikes(self):
        bike = self.conn.cursor()
        rows = bike.execute('SELECT FROM motociclete')
        row_list = list(rows)  
        for i in row_list:
            print(f"numar_inmatriculare: {i[6]} | marca {i[1]} | model {i[2]}")
        self.conn.execute()
        
    def arata_client(self):
        bike1 = self.conn.cursor()
        rows = bike1.execute('SELECT FROM clienti')
        row_list = list(rows)
        for i in row_list:
            print(f"nume {i[1]} | prenume {i[2]}")
        self.conn.commit()
        
    def anuleaza_rezervare(self, id):
        sql = 'DELETE FROM rezervari WHERE id-?'
        bike = self.conn.cursor()
        bike.execute(sql, (id,))
        self.conn.commit()
        
    def arata_revervari_motocicleta(self):
        bike1 = self.conn.cursor()
        rows = bike1.execute('SELECT FROM rezervari')
        row_list = list(rows)
        for i in row_list:
            print (f" data_start {i[1]} | perioada {i[2]} | bine_id {i[3]} client_id {i[4]}")
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
        self.__nr_inmatriculare = bike_data["numar_inmatriculare"]

class Rezervari:

    def __init__(self, rezervari_data):
        self.__perioada_rezervare = rezervari_data["data_start"] 
        self.__rezervare = rezervari_data["perioada"]
        self.__rezervare = rezervari_data["bike_id"]
        self.__rezervare = rezervari_data["client_id"]
        
    




make_table = DataBase(DB_FILE)

make_table.create_client_table()
make_table.create_moto_table()
make_table.create_rezervation_table()




user_input = Menu.client_menu()
bike_input = Menu.bike_menu()
rezervare_input = Menu.rezervari_menu()

user1 = Client(user_input)
rezervari1 = Rezervari(rezervare_input)

bike1 = Bike(bike_input)
user1 = Client(user_input)
rezervari1 = Rezervari(rezervare_input)

print(user_input)

make_table.insert_info_clienti(user_input)
make_table.insert_info_moto(bike_input)
make_table.insert_info_rezervari(rezervare_input)




make_table.print_rezervari()
make_table.show_bikes()
make_table.arata_client()
make_table.anuleaza_rezervare()
make_table.create_client_table()
make_table.create_rezervation_table()
make_table.create_moto_table()

menu1 = Menu()
while True:
    bike_choice = menu1.client_menu()
    bike_choice()





