import flet as ft


class Interactive:
    def __init__(self, file_picker):
        self.field_var_number = ft.TextField(
            value="2",
            width=60,
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=2,
            text_align=ft.TextAlign.CENTER,
            height=30,
            text_size=15,
            content_padding=ft.Padding(0, 4, 0, 0)
        )
        self.btn_manual_input = ft.IconButton(ft.Icons.KEYBOARD)
        self.btn_select_file = ft.IconButton(ft.Icons.FOLDER, on_click=self.pick_file)
        self.file_picker = file_picker
        self.file_picker.on_result = self.file_picker_result
        self.history = []
        self.output = ft.Text(
            # height=150,
        )

        self.scroll_column = ft.Column(controls=[
            self.output
        ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            width=None,
        )

    def pick_file(self, event):
        self.file_picker.pick_files(allowed_extensions=['txt'])

    def file_picker_result(self, event):
        if event.files:
            selected_file = event.files[0]
            self.update_output(f"Selected file: {selected_file.path}")
        else:
            self.update_output("No file selected.")

    def update_output(self, update):
        self.history.append(update)
        self.output.value = '\n\n'.join(self.history)
        self.scroll_column.scroll_to(offset=-1, duration=300)
        self.scroll_column.update()
