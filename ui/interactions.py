import flet as ft
from functions.process_file import get_matrix, to_print
from checkboxes import Checkboxes
from math_methods.gauss import Gauss
from math_methods.cramer import Cramer


class Interactive:
    def __init__(self, file_picker):

        self.btn_select_file = ft.IconButton(ft.Icons.FOLDER, on_click=self.pick_file)
        self.file_picker = file_picker
        self.file_picker.on_result = self.file_picker_result
        self.history = []
        self.output = ft.Text(
            color=ft.colors.GREEN_ACCENT_400,  # Зеленый как в Матрице
            font_family="Courier New",  # Моноширинный шрифт
            size=18,  # Оптимальный размер
            selectable=True  # Возможность выделения текста
        )
        self.scroll_column = ft.Column(controls=[
            self.output
        ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            width=None,
        )

        self.matrix = None
        self.checkboxes = Checkboxes()
        self.btn_get_solution = ft.Button("Get solutions", color="white", on_click=self.get_solution)
        self.btn_clear = ft.ElevatedButton('Erase history',
                                           width=250,
                                           height=20,
                                           bgcolor="#181e15",
                                           on_click=self.erase_history)

    def erase_history(self, e):
        self.history.clear()
        self.update_output('')

    def pick_file(self, event):
        self.file_picker.pick_files()

    def file_picker_result(self, event):
        if event.files:
            selected_file = event.files[0]
            self.update_output(f"Selected file: {selected_file.path}")
            self.matrix = get_matrix(selected_file.path)
            slae = to_print(self.matrix)
            self.update_output(slae[0])
            self.update_output(slae[1])
        else:
            self.update_output("No file selected.")

    def update_output(self, *update):
        for up in update:
            self.history.append(up)
        self.output.value = '\n\n'.join(self.history)
        self.scroll_column.scroll_to(offset=-1, duration=300)
        self.scroll_column.update()

    def get_solution(self, event):
        ckb_status = self.checkboxes.get_status()
        print(ckb_status)
        if any(ckb_status['gauss']):
            self.gauss_results(ckb_status['gauss'])
        if any(ckb_status['cramer']):
            self.cramer_results(ckb_status['cramer'])

    def gauss_results(self, status):
        a = ('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
             'GAUSS\'s METHOD RESULTS:\n'
             '--------------------------------------------------------------------')
        self.update_output(a)
        match status:
            case [True, False, False]:
                gs = Gauss(self.matrix)
                gs.update_matrix()
                self.update_output('\nROOTS:', gs.decorate_result())
            case [_, True, False]:
                gs = Gauss(self.matrix)
                gs.update_matrix()
                upd_matrix = gs.converted_matrix
                tp = to_print((upd_matrix, len(upd_matrix)))
                self.update_output('\nIN PROCESS STAGE:', tp[0], tp[1], '\nROOTS:', gs.decorate_result())
            case [_, False, True]:
                gs = Gauss(self.matrix)
                gs.update_matrix()
                self.update_output('\nROOTS:', gs.decorate_result(), '\nCHECKUP:', gs.to_print_check())
            case [_, True, True]:
                gs = Gauss(self.matrix)
                gs.update_matrix()
                upd_matrix = gs.converted_matrix
                tp = to_print((upd_matrix, len(upd_matrix)))
                self.update_output('\nIN PROCESS STAGE:', tp[0], tp[1], '\nROOTS:', gs.decorate_result(),
                                   '\nCHECKUP:', gs.to_print_check())

    def cramer_results(self, status):
        a = ('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
             'CRAMER\'s METHOD RESULTS:\n'
             '--------------------------------------------------------------------')
        self.update_output(a)
        match status:
            case [True, False, False]:
                cr = Cramer(self.matrix)
                self.update_output('\nROOTS:', cr.decorate_result())
            case [_, True, False]:
                cr = Cramer(self.matrix)
                cr.get_result()
                self.update_output('\nIN PROCESS STAGE:\n', cr.show_process(), '\nROOTS:', cr.decorate_result())
            case [_, False, True]:
                cr = Cramer(self.matrix)
                self.update_output('\nROOTS:', cr.decorate_result(), '\nCHECKUP:', cr.to_print_check())
            case [_, True, True]:
                cr = Cramer(self.matrix)
                cr.get_result()
                self.update_output('\nIN PROCESS STAGE:', cr.show_process(), '\nROOTS:', cr.decorate_result(),
                                   '\nCHECKUP:', cr.to_print_check())
