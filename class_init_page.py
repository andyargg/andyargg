import flet as ft

class InitPage:
    def __init__(self, page:ft.Page) -> None:
        self.page = page
        self.page.theme_mode=ft.ThemeMode.LIGHT
        self.page.window_width=500
        self.page.window_min_height=200
        self.page.window_max_height=600
    

    def create_init_ui(self):
        container = ft.Container(
            bgcolor=ft.colors.BLUE,
            width=self.page.width,
            height=self.page.height,
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=250),
            content=ft.Column(
                    spacing=20,
                    controls=[
                        ft.Text("Bienvenido", size=20),
                        ft.ElevatedButton("Empezar", on_click=lambda _:self.page.go("/date"), height=40),
                        ]
                    )
                )
        
        return container
    
    def build(self):
        return self.create_init_ui()
    

# def main(page):
#     init = InitPage(page)
#     page.add(init.build())


# ft.app(target=main)