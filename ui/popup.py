from fractions import Fraction
import flet as ft

from functions.process_file import to_print


class Popup:
    def __init__(self, page, act):
        self.act = act
        self.page = page
        self.field_names = []
        self.field_var_number = ft.TextField(
            value="2",
            width=60,
            keyboard_type=ft.KeyboardType.NUMBER,
            input_filter=ft.NumbersOnlyInputFilter(),
            max_length=2,
            text_align=ft.TextAlign.CENTER,
            height=30,
            text_size=15,
            content_padding=ft.Padding(0, 4, 0, 0)
        )

        self.matrix = []
        self.matrix_len = 0
        self.dialog = None  # Пока нет попапа
        self.fields = {}

    def open(self, e=None):  # e=None для вызова вручную
        self.matrix_len = int(self.field_var_number.value)
        self.create_matrix()
        self.create_popup()
        self.dialog.open = True
        self.page.update()

    def close(self, e):
        self.get_field_values()
        self.act.matrix = (self.matrix, self.matrix_len)
        slae = to_print(self.act.matrix)
        self.act.update_output(slae[0], slae[1])
        self.dialog.open = False
        self.page.update()
        self.dialog = None

    def cancel(self, e):
        self.dialog.open = False
        self.page.update()
        self.dialog = None

    def create_fields_column(self):
        """Создает колонку с текстовыми полями из self.field_names"""
        rows = []
        for i in range(self.matrix_len):
            temp = {}
            for ind, name in enumerate(self.field_names[i]):
                temp[name] = ft.TextField(
                    value="0",
                    width=60,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    input_filter=ft.InputFilter(
                        regex_string=r"^-?\d*\.?\d*$",  # Разрешает: -, ., цифры
                        allow=True,
                        replacement_string=""  # Запрещает невалидные символы
                    ),
                    max_length=7,
                    text_align=ft.TextAlign.CENTER,
                    height=30,
                    text_size=13,
                    content_padding=ft.Padding(0, 4, 0, 0)
                )
                if ind < self.matrix_len - 1:
                    temp[f'text_{name}'] = ft.Text(f'* X{ind + 1} +', size=18)
                elif ind == self.matrix_len - 1:
                    temp[f'text_{name}'] = ft.Text(f'* X{ind + 1} =', size=18)

            rows.append(list(temp.values()))
            self.fields |= temp
        return ft.Column(controls=[ft.Row(controls=row) for row in rows],
                         scroll=ft.ScrollMode.AUTO)

    def get_field_values(self):
        """
        gets matrix from popup
        :return: [[]]
        """
        self.matrix.clear()

        for i in range(self.matrix_len):
            res = []
            for name in self.field_names[i]:
                res.append(Fraction(self.fields[name].value))
            self.matrix.append(res)

    def create_popup(self):
        """Создает попап"""
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Input index values"),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=self.create_fields_column(),
                        width=147 * self.matrix_len,
                        padding=0
                    )
                ],
                scroll=ft.ScrollMode.AUTO
            ),
            actions=[ft.TextButton("Confirm and close", on_click=self.close),
                     ft.TextButton("Cancel and close", on_click=self.cancel)],
            inset_padding=0,  # Убираем стандартные отступы AlertDialog
        )
        self.page.overlay.append(self.dialog)
        self.page.update()

    def create_matrix(self):
        self.field_names.clear()
        for i in range(self.matrix_len):

            temp = []
            for j in range(self.matrix_len):
                temp.append(f'{i}X{j + 1}')
            temp.append(f'{i}res')

            self.field_names.append(temp)
