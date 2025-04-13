import flet as ft

class FirstColumn(ft.Control):
    def __init__(self):
        super().__init__()
        self.text_line1 = ft.Text("Строка 1")
        self.text_line2 = ft.Text("Строка 2")
        self.button = ft.ElevatedButton("Кнопка")

    def _get_control_name(self):
        return "firstcolumn"  # Уникальное имя для вашего контрола

    def _get_children(self):
        return [
            self.text_line1,
            self.text_line2,
            self.button
        ]

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=self._get_children(),
                spacing=5
            ),
            bgcolor=ft.colors.TEAL,
            padding=10,
            border_radius=5,
            expand=True
        )