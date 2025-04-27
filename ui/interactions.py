import flet as ft
from functions.process_file import get_matrix, to_print
from checkboxes import Checkboxes
from math_methods.gauss import Gauss
from math_methods.cramer import Cramer
from math_methods.gauss_jordan import GaussJordan
from math_methods.validation import Validation


class Interactive:
    def __init__(self, file_picker):

        self.btn_select_file = ft.IconButton(ft.Icons.FOLDER, on_click=self.pick_file)
        self.file_picker = file_picker
        self.file_picker.on_result = self.file_picker_result
        self.history = []
        self.valid_methods = None
        self.validation = None;
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
        self.btn_get_solution = ft.Button("Get solutions", color="white", on_click=self.get_solution, disabled=True)
        self.btn_clear = ft.ElevatedButton('Erase history',
                                           width=250,
                                           height=20,
                                           bgcolor="#181e15",
                                           on_click=self.erase_history)

        self.btn_analyze = ft.Button('Analyze', width=25, color="white", disabled=True,
                                     on_click=self.get_valid_methods)

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
            self.validation = Validation(self.matrix)
            if self.validation.valid:
                slae = to_print(self.matrix)
                self.update_output(slae[0], slae[1])
            else:
                self.update_output('Error: Invalid Matrix')

            self.unblock_analyses(self.validation.valid)
            self.checkboxes.clean_ckb()
            self.btn_get_solution.disabled = True
            self.btn_get_solution.update()
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
        if any(ckb_status['cramer']):
            self.cramer_results(ckb_status['cramer'])
        if any(ckb_status['gauss']):
            self.gauss_results(ckb_status['gauss'])
        if any(ckb_status['gauss_jordan']):
            self.gauss_jordan_results(ckb_status['gauss_jordan'])

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

    def gauss_jordan_results(self, status):
        a = ('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
             'GAUSS-JORDAN METHOD RESULTS:\n'
             '--------------------------------------------------------------------')
        self.update_output(a)
        match status:
            case [True, False, False]:
                gj = GaussJordan(self.matrix)
                gj.update_matrix()
                gj.upgrade_diagonal()
                gj.upgrade_top()
                self.update_output('\nROOTS:', gj.decorate_result())
            case [_, True, False]:
                gj = GaussJordan(self.matrix)
                gj.update_matrix()
                gj.upgrade_diagonal()
                gj.upgrade_top()
                gj.get_result()
                upd_matrix = gj.converted_matrix
                tp = to_print((upd_matrix, len(upd_matrix)))
                self.update_output('\nIN PROCESS STAGE:', tp[0], tp[1], '\nROOTS:', gj.decorate_result())
            case [_, False, True]:
                gj = GaussJordan(self.matrix)
                gj.update_matrix()
                gj.upgrade_diagonal()
                gj.upgrade_top()
                self.update_output('\nROOTS:', gj.decorate_result(), '\nCHECKUP:', gj.to_print_check())
            case [_, True, True]:
                gj = GaussJordan(self.matrix)
                gj.update_matrix()
                gj.upgrade_diagonal()
                gj.upgrade_top()
                gj.get_result()
                upd_matrix = gj.converted_matrix
                tp = to_print((upd_matrix, len(upd_matrix)))
                self.update_output('\nIN PROCESS STAGE:', tp[0], tp[1], '\nROOTS:', gj.decorate_result(),
                                   '\nCHECKUP:', gj.to_print_check())

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

    def unblock_analyses(self, valid):
        self.btn_get_solution.disabled = True
        self.checkboxes.clean_ckb()
        if valid:
            self.btn_analyze.disabled = False
            self.btn_analyze.update()
            self.update_output('Pre-validation - Ok!')
        else:
            self.btn_analyze.disabled = True
            self.btn_analyze.update()
            self.update_output('Pre-validation - Error!', self.validation.validate_error)

    def get_valid_methods(self, event):
        self.valid_methods = self.validation.validate_methods()
        if self.valid_methods['determinant'] == 0:
            self.update_output('Determinant = 0 \nSLAE do not has a single solution!!!')
            return
        self.btn_get_solution.disabled = False
        self.btn_get_solution.update()
        self.update_output(str(self.valid_methods))
        for key in self.valid_methods:
            if key == 'determinant':
                continue
            if self.valid_methods[key]:
                self.checkboxes.unblock_ckb(key)