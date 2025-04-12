import flet as ft


def main(page: ft.Page):
    page.title = "SLAE solutions"
    page.theme_mode = "dark"
    page.add(ft.Row(
        [
            ft.TextSpan(text='Fill in Manually'),
            ft.TextField(value='2', width=40, border_color='gray'),
            ft.IconButton(ft.Icons.KEYBOARD)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ))


ft.app(target=main)
