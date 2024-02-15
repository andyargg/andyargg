import flet as ft

def main(page: ft.Page):
    # Crear un container con contenido en una columna
    mi_columna = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Elemento 1"),
                ft.Text("Elemento 2"),
                ft.Text("Elemento 3"),
            ]
        ),
        bgcolor=ft.colors.BLACK,  # Color de fondo opcional
        padding=5,  # Nuevo valor de padding (ajústalo según tus necesidades)
    )

    # Acceder al contenido del container
    print(mi_columna.content.controls[0].value)

    # Modificar el padding del contenido
      # Nuevo valor de padding

    page.add(mi_columna)

ft.app(target=main)