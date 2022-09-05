menu_options = {
    1: "Adauga motocicleta",
    2: "Adauga client",
    3: "Adauga rezervarea",
    4: "Vezi rezervari",
    5: "Anuleaza rezervarea"
    
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')
     
def option4():
     print('Handle option \'Option 4\'')

def option5():
     print('Handle option \'Option 5\'')
     
def option6():
     print('Handle option \'Option 6\'')
     
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Alegere introdusa: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
            
    
            print('Thanks message before exiting')
            exit()
        else:
            print('Optine invalida. Te rog alege un numar intre 1 si 5.')