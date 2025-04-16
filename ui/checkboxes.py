import flet as ft


class Checkboxes:
    def __init__(self):
        self.checkboxes = {
            'cramer': [ft.Checkbox(), ft.Checkbox(), ft.Checkbox()],
            'gauss': [ft.Checkbox(), ft.Checkbox(), ft.Checkbox()]
        }

        self.ckb_status = {
            'cramer': [False, False, False],
            'gauss': [False, False, False]
        }

        self.ckb_block = {
            'cramer': [self.wrap_ckb(self.checkboxes['cramer'][0]),
                       self.wrap_ckb(self.checkboxes['cramer'][1]),
                       self.wrap_ckb(self.checkboxes['cramer'][2])],
            'gauss': [self.wrap_ckb(self.checkboxes['gauss'][0]),
                      self.wrap_ckb(self.checkboxes['gauss'][1]),
                      self.wrap_ckb(self.checkboxes['gauss'][2])],
        }

    def wrap_ckb(self, ckb):
        return ft.DataCell(ft.Container(ckb, alignment=ft.alignment.center))

    def get_status(self):
        # 3. Обновляем статусы перед возвратом
        self.ckb_status['cramer'] = [ckb.value for ckb in self.checkboxes['cramer']]
        self.ckb_status['gauss'] = [ckb.value for ckb in self.checkboxes['gauss']]
        return self.ckb_status
