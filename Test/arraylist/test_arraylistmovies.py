import model.test_arraylist as arreglo
import App.app as app

lista_casting= app.loadCSVFile("MoviesCastingRaw-small.csv")
print(lista_casting)
lista_peliculas= app.loadCSVFile("SmallMoviesDetailsCleaned.csv")
print(lista_peliculas)