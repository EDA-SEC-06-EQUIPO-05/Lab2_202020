import App.app as app
import DataStructures.liststructure as lt

lista_casting= app.loadCSVFile("MoviesCastingRaw-small.csv")
print(lista_casting)
lista_peliculas= app.loadCSVFile("SmallMoviesDetailsCleaned.csv")
print(lista_peliculas)

lista_enc= lt.newList("")

def formar_lista_l_encadenada(lista_csv:list,lista_nueva:list)->dict:

    

    return lista_nueva