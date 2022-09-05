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
      print("\n Nu este o alegere valida, incearca din nou") 