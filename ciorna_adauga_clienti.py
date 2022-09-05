
import sqlite3
import pathlib



ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db.db")
db_con = sqlite3.connect(DB_FILE)

def create_client_table(connection):
    bike = connection.cursor()
        
    bike.execute("""
            CREATE TABLE IF NOT EXISTS clienti (
            id INTEGER PRIMARY KEY,
            nume TEXT NOT NULL,
            prenume TEXT NOT NULL,
            adresa TEXT NOT NULL,
            telefon TEXT NOT NULL,
            cnp TEXT NOT NULL,
            email TEXT NOT NULL)"""
            )
    connection.commit()
    
create_client_table(db_con)

class Clients:

    def __init__(self, user_data):
        self.__nume = user_data["nume"]
        self.__prenume = user_data["prenume"]
        self.__adresa = user_data["adresa"]
        self.__telefon = user_data["telefon"]
        self.__cnp = user_data["cnp"]
        self.__email = user_data["email"]
        
        bike = db_con.cursor()
        
        bike.execute("""INSERT INFO clienti (nume, prenume, cnp, adresa, telefon, email) Values (?,?,?,?,?,?"""),
        (self.__nume,self.__prenume,self.__adresa,self.__telefon,self.__cnp,self.__email)
        db_con.commit()
        
