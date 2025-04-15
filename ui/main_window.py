import flet as ft
from interactions import Interactive


def main(page: ft.Page):
    page.title = "SLAE solutions"
    page.theme_mode = "dark"
    file_picker = ft.FilePicker()
    page.add(file_picker)
    act = Interactive(file_picker)

    row = ft.Container(
        content=ft.Row(
            controls=[
                # Колонка 1

                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                [
                                    ft.Text('Fill in Manually', size=20),
                                    act.field_var_number,
                                    act.btn_manual_input
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                            ft.Row(
                                [
                                    ft.Text('Select local file', size=20),
                                    act.btn_select_file
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            )
                        ]
                    ),
                    bgcolor=ft.Colors.TEAL,
                    padding=5,
                    border_radius=5,
                    width=400,
                    height=100
                    # expand=True

                ),

                ft.Container(
                    content=ft.Button('Analise>', width=25, color="white"),
                    bgcolor=ft.Colors.PURPLE,
                    padding=10,
                    border_radius=5,
                    expand=True
                ),

                # Колонка 3 (фиолетовый фон)

                ft.Container(
                    content=ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Method")),
                            ft.DataColumn(ft.Text("On")),
                            ft.DataColumn(ft.Text("process")),
                            ft.DataColumn(ft.Text("check")),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text('row1')),
                                    ft.DataCell(ft.Checkbox()),
                                    ft.DataCell(ft.Checkbox()),
                                    ft.DataCell(ft.Checkbox()),
                                ]
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text('row2')),
                                    ft.DataCell(ft.Checkbox()),
                                    ft.DataCell(ft.Checkbox()),
                                    ft.DataCell(ft.Checkbox()),

                                ]
                            )

                        ],
                    ),
                    # bgcolor=ft.Colors.PURPLE,
                    border_radius=5,
                ),

                # Колонка 4 (оранжевый фон)
                ft.Container(
                    content=ft.Button("Get solutions", color="white"),
                    bgcolor=ft.Colors.ORANGE,
                    padding=10,
                    border_radius=5,
                    expand=True
                ),

            ],

        ),
        bgcolor="#2f2f2f",
        padding=5,
        height=250
    )

    page.add(row)

    page.add(ft.Container(
        content=act.scroll_column,
        width=page.width,
        height=page.height,
        expand=True,
        padding=5,
        margin=5,
        # bgcolor=ft.Colors.TEAL

    ))

    page.add(act.output)


if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER, port=64928)
