import flet as ft
from class_search_bar import MySearchBar

class Form:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode=ft.ThemeMode.DARK
        self.page.window_width=500
        self.page.window_min_height=200
        self.page.window_max_height=600
        self.txt_number = ft.Text("1", weight=20)

    def button_next_clicked(self, e):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.page.update()

    def button_back_clicked(self, e):
        if self.txt_number.value == "1":
            self.txt_number.value = "1"
        else:
            self.txt_number.value = str(int(self.txt_number.value) - 1)

        self.page.update()

    def validate_form(self, e):

        flag_1 = False
        flag_2 = False
        for dropdown in  self.dropdowns:
            if not dropdown.value:
                dropdown.border_color='#fc0339'
                dropdown.error_text="Selecciona una opcion"
                # dropdown.label_style={
                #     'color':'red'
                # }
                dropdown.update()
            else:
                flag_1 = True
                dropdown.error_text=""
                dropdown.update()



        for search_boxes  in (self.search_bars):
            if not search_boxes.controls[0].value:
                search_boxes.obj.bar_bgcolor=ft.colors.RED
                search_boxes.obj.bar_hint_text="Completa esta casilla"

            else:
                flag_2 = True

            search_boxes.obj.update()

        if flag_1 and flag_2:
            self.button_next_clicked()
            self.page.update()

    def create_ui(self):
        container=ft.Container(
            alignment=ft.alignment.center,
            width=self.page.width,
            gradient=ft.LinearGradient([
                '#526a8e',
                '#52768e',
                '#3d768e',
            ]),
            padding=ft.padding.only(top=30, bottom=30,left=8),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Camioneta:"),
                            self.txt_number,
                        ]
                    ),
                    ft.Column(
                        controls=[
                            MySearchBar("Patentes"),#0
                            MySearchBar("Tecnico"),#1
                            ft.Dropdown(#2
                                border_radius=20,
                                label="Orden",
                                width=450,
                                options=[
                                    ft.dropdown.Option("Muy desordenado"),
                                    ft.dropdown.Option("Desordenado"),
                                    ft.dropdown.Option("Ordenado"),
                                    ft.dropdown.Option("Muy ordenado"),
                                ]
                            ),
                            ft.Dropdown(#3
                                label="Limpieza",
                                border_radius=20,
                                width=450,
                                options=[
                                    ft.dropdown.Option("Muy sucio"),
                                    ft.dropdown.Option("Sucio"),
                                    ft.dropdown.Option("Limpio"),
                                    ft.dropdown.Option("Muy limpio"),
                                ]
                            ),
                            ft.Dropdown(#4
                                label="Agua",
                                width=450,
                                border_radius=20,
                                options=[
                                    ft.dropdown.Option("Si"),
                                    ft.dropdown.Option("No")
                                ]
                            ),
                            ft.Dropdown(#5
                                label="Rueda de auxilio",
                                border_radius=20,
                                width=450,
                                options=[
                                    ft.dropdown.Option("Si"),
                                    ft.dropdown.Option("No")
                                ]
                            ),
                             ft.Dropdown(#6
                                label="Aceite",
                                border_radius=20,
                                width=450,
                                options=[
                                    ft.dropdown.Option("Si"),
                                    ft.dropdown.Option("No")
                                ]
                            ),
                             ft.Dropdown(#7
                                label="Crique",
                                border_radius=20,
                                width=450,
                                options=[
                                    ft.dropdown.Option("Si"),
                                    ft.dropdown.Option("No")
                                ]
                            ),
                            ft.Dropdown(#8
                                label="Llave cruz",
                                border_radius=20,
                                width=450,
                                options=[
                                    ft.dropdown.Option("Si"),
                                    ft.dropdown.Option("No")
                                ]
                            ),
                             ft.Dropdown(#9
                                label="Matafuego",
                                border_radius=20,
                                width=450,
                                options=[
                                    ft.dropdown.Option("Si"),
                                    ft.dropdown.Option("No")
                                ]
                            ),
                             ft.Dropdown(#10
                                label="Candado",
                                border_radius=20,
                                width=450,
                                options=[
                                    ft.dropdown.Option("Si"),
                                    ft.dropdown.Option("No")
                                ]
                            ),
                             ft.TextField(#11
                                label="Deja un comentario",
                                width=450,
                                border_radius=20,

                            ),
                             ft.Row(#
                                controls=[
                                    ft.ElevatedButton(
                                        text="Anterior",
                                        on_click=self.button_back_clicked
                                    ),
                                    ft.ElevatedButton(
                                        text="Siguiente",
                                        on_click=self.validate_form
                                    ),

                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND
                            ),
                        ]
                    ),
                ]
            )
        )

        

       
        self.dropdowns = [
            container.content.controls[1].controls[2],#Orden
            container.content.controls[1].controls[3],#Limpieza
            container.content.controls[1].controls[4],#Agua
            container.content.controls[1].controls[5],#Rueda
            container.content.controls[1].controls[6],#Aceite
            container.content.controls[1].controls[7],#Crique
            container.content.controls[1].controls[8],#Llave Cruz
            container.content.controls[1].controls[9],#Matafuego
            container.content.controls[1].controls[10],#Candado
            container.content.controls[1].controls[11],#Comentario
        ]
        self.search_bars = [
            container.content.controls[1].controls[0],#searchbar 1
            container.content.controls[1].controls[1],#searchbar 2
        ]



        self.list_view = ft.ListView(expand=1, auto_scroll=False)
        self.list_view.controls.append(container)

        return self.list_view

    def build(self):
        return self.create_ui()

# def main(page):
#     form = Form(page)
#     page.add(form.build())


# ft.app(target=main)