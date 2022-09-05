from multiprocessing import connection
import sqlite3
import pathlib

ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("bikes.db")
db_con = sqlite3.connect(DB_FILE)

def create_moto_table(self):
       bike = connection.cursor()
       bike.executede ("""
            CREATE TABLE IF NOT EXISTS motociclete(
            id INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            model TEXT NOT NULL,
            an_fabricatie INTEGER NOT NULL,
            tip_cadru_motocicleta TEXT NOT NULL,
            seria_sasiu TEXT NOT NULL,
            numar_inmatriculare TEXT NOT NULL)
            """)
            connection.commit()