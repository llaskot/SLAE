import flet as ft
from interactions import Interactive
from popup import Popup


def main(page: ft.Page):
    page.title = "SLAE solutions"
    page.theme_mode = "dark"
    file_picker = ft.FilePicker()
    page.add(file_picker)
    act = Interactive(file_picker)
    popup = Popup(page, act)
    btn_manual_input = ft.IconButton(ft.Icons.KEYBOARD, on_click=popup.open)
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
                                    popup.field_var_number,
                                    btn_manual_input
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
                    content=act.btn_analyze,
                    bgcolor=ft.Colors.PURPLE,
                    padding=10,
                    border_radius=5,
                    expand=True
                ),

                ft.Container(
                    content=ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Method", text_align=ft.TextAlign.CENTER)),
                            ft.DataColumn(ft.Text("Roots only", text_align=ft.TextAlign.CENTER)),
                            ft.DataColumn(ft.Text("Process", text_align=ft.TextAlign.CENTER)),
                            ft.DataColumn(ft.Text("Check", text_align=ft.TextAlign.CENTER)),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text('Cramer\'s', text_align=ft.TextAlign.CENTER)),
                                    act.checkboxes.ckb_block['cramer'][0],
                                    act.checkboxes.ckb_block['cramer'][1],
                                    act.checkboxes.ckb_block['cramer'][2],
                                ],

                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text('Gauss\'s', text_align=ft.TextAlign.CENTER)),
                                    act.checkboxes.ckb_block['gauss'][0],
                                    act.checkboxes.ckb_block['gauss'][1],
                                    act.checkboxes.ckb_block['gauss'][2],

                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text('Gauss-Jordan', text_align=ft.TextAlign.CENTER)),
                                    act.checkboxes.ckb_block['gauss_jordan'][0],
                                    act.checkboxes.ckb_block['gauss_jordan'][1],
                                    act.checkboxes.ckb_block['gauss_jordan'][2],

                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text('Jacoby', text_align=ft.TextAlign.CENTER)),
                                    act.checkboxes.ckb_block['jacoby'][0],
                                    act.checkboxes.ckb_block['jacoby'][1],
                                    act.checkboxes.ckb_block['jacoby'][2],
                                ],
                            ),
                        ],
                    ),
                    # bgcolor=ft.Colors.PURPLE,
                    border_radius=5,
                ),

                # Колонка 4 (оранжевый фон)
                ft.Container(
                    content=act.btn_get_solution,
                    bgcolor=ft.Colors.ORANGE,
                    padding=10,
                    border_radius=5,
                    expand=True
                ),

            ],

        ),
        bgcolor="#181e15",
        padding=5,
        height=250
    )

    page.add(row)

    page.add(ft.Container(
        content=act.scroll_column,
        # width=page.width,
        height=page.height,
        expand=True,
        padding=5,
        margin=5,
    ))
    page.add(act.btn_clear)





if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER, port=64928)
