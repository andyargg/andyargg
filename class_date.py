import flet as ft

import datetime


class Date:
    def __init__(self,page:ft.Page) -> None:
        self.page = page
        
        self.page.theme_mode=ft.ThemeMode.LIGHT
        self.page.window_width=500
        self.page.window_min_height=200
        self.page.window_max_height=600

        

    def create_date_ui(self):
        date_picker = ft.DatePicker(
            first_date=datetime.datetime(2024, 1, 1),
            last_date=datetime.datetime(2100, 12, 1),
        )
        self.page.overlay.append(date_picker)

        container = ft.Container(
            
            bgcolor=ft.colors.BLUE,
            width=self.page.width,
            height=self.page.height,
            content=ft.Column(
                    spacing=100,
                    controls=[
                        ft.Container(
                            padding=ft.padding.only(top=10, left=5),
                            alignment=ft.alignment.top_left,
                            content=ft.ElevatedButton(
                                text="Atrás",
                                icon="arrow_back",
                                on_click=lambda _:self.page.go("/")
                                
                            ),
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            height=100,
                            content=ft.ElevatedButton(
                                height=50,
                                text="Selecciona la fecha actual",
                                icon="calendar_month",
                                on_click=lambda _: date_picker.pick_date()
                            ),
                        ),
                        ft.Container(
                            padding=ft.padding.only(top=10),
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                controls=[
                                    ft.ElevatedButton(
                                        "Comenzar",
                                        height=50,
                                        on_click=lambda _:self.page.go("/form")
                                        )
                                    ]
                                )
                            )
                        
                        ],
                    ),
                )
        
        return container

    def build(self):
        return self.create_date_ui()

# def main(page: ft.Page):
#     init = Date(page)
#     # add application's root control to the page
#     page.add(init.build())

# ft.app(target=main)


