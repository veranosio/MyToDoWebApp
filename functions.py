PATH = "Agenda.txt"

def plik_load(path=PATH):
    """Reads in the list from the file
    and returns the content in form of a list"""
    with open(path,"r") as plik_local:
        tablica_local = plik_local.readlines()
    return tablica_local

def plik_write(tablica,path=PATH):
    """Open a file in write mode and saves
    the list into the file"""
    with open(path,"w") as plik_local:
        plik_local.writelines(tablica)


if __name__ == "__main__":
    print("DSADASDA")