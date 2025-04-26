import flet as ft


class Checkboxes:
    def __init__(self):
        self.checkboxes = {
            'cramer': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],
            'gauss': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],
            'gauss_jordan': [ft.Checkbox(disabled=True), ft.Checkbox(disabled=True), ft.Checkbox(disabled=True)],

        }

        self.ckb_status = {
            'cramer': [False, False, False],
            'gauss': [False, False, False],
            'gauss_jordan': [False, False, False],
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
        }

    @staticmethod
    def wrap_ckb(ckb):
        return ft.DataCell(ft.Container(ckb, alignment=ft.alignment.center))

    def clean_ckb(self):
        for key in self.checkboxes:
            for elem in self.checkboxes[key]:
                elem.value = False
                elem.disabled = True
                elem.update()

    def get_status(self):
        # 3. Обновляем статусы перед возвратом
        self.ckb_status['cramer'] = [ckb.value for ckb in self.checkboxes['cramer']]
        self.ckb_status['gauss'] = [ckb.value for ckb in self.checkboxes['gauss']]
        self.ckb_status['gauss_jordan'] = [ckb.value for ckb in self.checkboxes['gauss_jordan']]
        return self.ckb_status
