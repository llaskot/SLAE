import flet as ft


class Checkboxes:
    def __init__(self):
        self.checkboxes = {
            'cramer': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],
            'gauss': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],
            'gauss_jordan': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],
            'jacoby': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],
            'seidel': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],

        }

        self.ckb_status = {
            'cramer': [False, False, False],
            'gauss': [False, False, False],
            'gauss_jordan': [False, False, False],
            'jacoby': [False, False, False],
            'seidel': [False, False, False]

        }

        self.ckb_block = {
            'cramer': [self.wrap_ckb(self.checkboxes['cramer'][0]),
                       self.wrap_ckb(self.checkboxes['cramer'][1]),
                       self.wrap_ckb(self.checkboxes['cramer'][2])],
            'gauss': [self.wrap_ckb(self.checkboxes['gauss'][0]),
                      self.wrap_ckb(self.checkboxes['gauss'][1]),
                      self.wrap_ckb(self.checkboxes['gauss'][2])],
            'gauss_jordan': [self.wrap_ckb(self.checkboxes['gauss_jordan'][0]),
                             self.wrap_ckb(self.checkboxes['gauss_jordan'][1]),
                             self.wrap_ckb(self.checkboxes['gauss_jordan'][2])],
            'jacoby': [self.wrap_ckb(self.checkboxes['jacoby'][0]),
                       self.wrap_ckb(self.checkboxes['jacoby'][1]),
                       self.wrap_ckb(self.checkboxes['jacoby'][2])],
            'seidel': [self.wrap_ckb(self.checkboxes['seidel'][0]),
                       self.wrap_ckb(self.checkboxes['seidel'][1]),
                       self.wrap_ckb(self.checkboxes['seidel'][2])],
        }

    @staticmethod
    def wrap_ckb(ckb):
        return ft.DataCell(ft.Container(ckb, alignment=ft.alignment.center,
                                        # bgcolor= "#46e602",
                                        padding=ft.padding.only(bottom=10)))

    def clean_ckb(self):
        for key in self.checkboxes:
            for elem in self.checkboxes[key]:
                elem.value = False
                elem.disabled = True
                elem.update()

    def unblock_ckb(self, key):
        for elem in self.checkboxes[key]:
            elem.disabled = False
            elem.update()

    def get_status(self):
        # 3. Обновляем статусы перед возвратом
        self.ckb_status['cramer'] = [ckb.value for ckb in self.checkboxes['cramer']]
        self.ckb_status['gauss'] = [ckb.value for ckb in self.checkboxes['gauss']]
        self.ckb_status['gauss_jordan'] = [ckb.value for ckb in self.checkboxes['gauss_jordan']]
        self.ckb_status['jacoby'] = [ckb.value for ckb in self.checkboxes['jacoby']]
        self.ckb_status['seidel'] = [ckb.value for ckb in self.checkboxes['seidel']]

        return self.ckb_status
