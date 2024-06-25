import fun
from os import system

op = 0
peliculas = [] #lista
#codigo,nombre,categoria,director,actores,año

while op !=4:
    system("cls")
    fun.mostrar_menu()
    op = fun.get_opcion()

    if op == 1:
        system("cls")
        peliculas.append(fun.agregar_pelicula())
    elif op == 2:
        system("cls")
        fun.listar_peliculas(peliculas)
        system("pause")
    elif op == 3:
        system("cls")
        fun.buscar_pelicula(peliculas)
        system("pause")

fun.crear_archivo(peliculas)

