import flet as ft


# def main(page: ft.Page):
#     page.title = "SLAE solutions"
#     page.theme_mode = "dark"
#
#     page.add(ft.Row(
#         [
#             ft.Text('Fill in Manually'),
#
#             ft.IconButton(ft.Icons.KEYBOARD)
#         ],
#         alignment=ft.MainAxisAlignment.CENTER
#     ))
#
#
#     # def main(page: ft.Page):
#     # Создаем строку с 5 колонками
#     row = ft.Row(
#         controls=[
#             # Колонка 1 (2 строки, бирюзовый фон)
#             ft.Container(
#                 content=ft.Column([
#                     ft.Text("Строка 1", size=16, color="white"),
#                     ft.Text("Строка 2", size=16, color="white")
#                 ]),
#                 bgcolor=ft.colors.TEAL,
#                 padding=10,
#                 border_radius=5,
#                 expand=True
#             ),
#
#             # Колонка 2 (розовый фон)
#             ft.Container(
#                 content=ft.Text("Колонка 2", size=16, color="white"),
#                 bgcolor=ft.colors.PINK,
#                 padding=10,
#                 border_radius=5,
#                 expand=True
#             ),
#
#             # Колонка 3 (фиолетовый фон)
#             ft.Container(
#                 content=ft.Text("Колонка 3", size=16, color="white"),
#                 bgcolor=ft.colors.PURPLE,
#                 padding=10,
#                 border_radius=5,
#                 expand=True
#             ),
#
#             # Колонка 4 (оранжевый фон)
#             ft.Container(
#                 content=ft.Text("Колонка 4", size=16, color="white"),
#                 bgcolor=ft.colors.ORANGE,
#                 padding=10,
#                 border_radius=5,
#                 expand=True
#             ),
#
#             # Колонка 5 (зеленый фон)
#             ft.Container(
#                 content=ft.Text("Колонка 5", size=16, color="white"),
#                 bgcolor=ft.colors.GREEN,
#                 padding=10,
#                 border_radius=5,
#                 expand=True
#             )
#         ],
#         spacing=10,
#         expand=True
#     )
#
#     page.add(row)


# ft.app(target=main)


from first_column import FirstColumn

def main(page: ft.Page):
    row = ft.Row(
        controls=[
            FirstColumn(),  # Наша кастомная колонка
            # Остальные колонки...
        ],
        spacing=10
    )
    page.add(row)

ft.app(target=main)




if __name__ == "__main__":
    ft.app(target=main)
