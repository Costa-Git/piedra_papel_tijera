import flet as ft
import random


def main(page: ft.Page):

    
    # Funcion del boton que ejecuta el programa
    def button_clicked(e):

        # Ejecucion solo si existe eleccion en desplegable
        if opcion_jugador.value != None:

            resultado = ""

            # Guardamos la seleccion del usuario y del ordenador
            usuario = opcion_jugador.value
            ordenador = random.choice(['piedra','papel','tijeras'])

            # Evaluamos el resultado y lo guardamos en la variable resultado
            if usuario == ordenador:
                resultado = "EMPATE !"
            else:
                if victoria(usuario,ordenador):
                    resultado = "GANASTE !"
                else:
                    resultado = "PERDISTE !"

            # Abrimos el dialog para mostrar el resultado
            page.dialog = dlg
            dlg.bgcolor="green"
            dlg.title = ft.Text(f"Elección usuario: {usuario}\
                            \nEleccion ordenador: {ordenador}\
                            \n\nResultado: {resultado}")
            dlg.open=True
            page.update()
            page.add(dlg)
            
    # Funcion que evalua si ha ganado el usuario o el ordenador    
    def victoria(jug, cpu):
        if(jug == 'piedra' and cpu == "tijeras") or (jug == 'papel' and cpu == "piedra") or (jug == 'tijeras' and cpu == "papel"):
            return True
    
    ###############################################################################################
    #           ZONA DE DISEÑO Y PINTADO DE LA INTERFAZ Y COMPONENTES
    ###############################################################################################

    # Dimensiones y alineacion pagina
    page.title = "Juego de Piedra Papel o Tijera"
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # Cabecera
    titulo = ft.Text("PIEDRA, PAPEL o TIJERA", size=20, color=ft.colors.GREEN, text_align="CENTER")

    # Desplegable de seleccion usuario.
    opcion_jugador = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("piedra"),
            ft.dropdown.Option("papel"),
            ft.dropdown.Option("tijeras"),
        ],
    )

    # Boton ejecucion de seleccion del usuario
    boton_juego = ft.ElevatedButton(text="JUGAR", on_click=button_clicked, icon="casino", icon_color="red")

    # Dialogo emergente con el resultado final
    dlg = ft.AlertDialog(title=ft.Text(""))

    # Distribucion de los tres contenedores de widgets
    cabecera = (ft.Container(content=titulo,width=500, height=40, margin=ft.margin.only(top=5)))
    cuerpo = (ft.Container(content=opcion_jugador, width=500, height=60, margin=ft.margin.only(top=20)))
    botonera = (ft.Container(content=boton_juego, width=200, height=40, margin=ft.margin.only(top=20)))
    
    page.add(
        cabecera,
        cuerpo,
        botonera,
    )

ft.app(target=main)