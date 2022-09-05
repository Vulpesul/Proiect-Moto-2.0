import sqlite3
import pathlib

ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db2.db")


class Menu:

    ans=True
    while ans:
        print ("""
    1.Adauga motocicleta
    2.Adauga client
    3.Adauga rezervare
    4.Vezi rezervari
    5.Anuleaza rezervarea
    6.Exit
    """)
    ans = input("Ce ai vrea sa descoperi? ") 
    if ans=="1": 
        print("\n Adauga motocicleta") 
    elif ans=="2":
        print("\n Adauga client") 
    elif ans=="3":
        print("\n Adauga rezervare") 
    elif ans=="4":
        print("\n Vezi rezervari") 
    elif ans=="5":
        print("\n Anuleaza rezervarea")
    elif ans=="6":
        print("\n Goodbye") 
    elif ans !="":
      print("\n Nu este o alegere valida, incearca alt numar") 
      exit()
    


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
    def add_rezervari_menu():
        return {
            "perioada": input("Adauga perioada dorita a rezervarii"),
        } 
